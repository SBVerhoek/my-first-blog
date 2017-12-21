from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','docfile')
        #docfile = forms.FileField(label='Select a file',)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
