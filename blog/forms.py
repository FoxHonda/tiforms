from django.forms import ModelForm, inlineformset_factory
from .models import Post, PostImages

class PostImagesForm(ModelForm):
    
    
    class Meta:
        model = PostImages
        fields = ['image','order']

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['text']


PostImagesFormSet = inlineformset_factory(Post, PostImages, form=PostImagesForm, fields=('__all__'), extra=1, max_num=4)
