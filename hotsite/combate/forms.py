from django.forms import ModelForm
from combate.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']
