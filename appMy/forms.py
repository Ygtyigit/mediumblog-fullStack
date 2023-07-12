from django import forms   
from .models import Post  

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields =('title','content')
    
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for name, field  in self.fields.items():
            field.widget.attrs.update({'class':'cardinput'})
            field.label = ""
        self.fields['title'].widget.attrs.update({'placeholder': 'TITLE'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Tell Your Story'})