from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Title','Subtitle','Title_image','Introduction_text','First_paragraph_title','First_paragraph_date','First_paragraph_text','First_paragraph_image','Second_paragraph_title','Second_paragraph_date','Second_paragraph_text','Second_paragraph_image')
        #docfile = forms.FileField(label='Select a file',)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
