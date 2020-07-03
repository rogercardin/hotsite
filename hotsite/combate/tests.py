from django.forms import ModelForm
from combate.models import Post

Class PostForm(ModelForm):
    Class Meta:
        model = POst
        fields = ['titulo','texto']
