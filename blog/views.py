from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Post, PostImages
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from .forms import PostForm, PostImagesFormSet

def index(request):
	num_posts = Post.objects.all().count()
	num_img = PostImages.objects.all().count()
	return render(request,'index.html', context={'num_posts':num_posts,'num_img':num_img},)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 6


class PostDetailView(generic.DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        post_form = PostImagesFormSet()
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        post_form = PostImagesFormSet(self.request.POST, self.request.FILES)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def form_valid(self, form, post_form):
        form.instance.user = self.request.user
        self.object = form.save()
        post_form.instance = self.object
        post_form.save()
        return redirect(self.success_url)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        post_form = PostImagesFormSet(instance = self.object)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        post_form = PostImagesFormSet(self.request.POST, self.request.FILES, instance=self.object)
        if (form.is_valid() and post_form.is_valid()):
            return self.form_valid(form, post_form)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def form_valid(self, form, post_form):
        self.object = form.save()
        post_form.instance = self.object
        post_form.save()
        return redirect(self.success_url)  