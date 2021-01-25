from django import forms
from core.models import Post

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']
        widgets = {
            'publish': forms.CheckboxInput(),
        }
        
class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']
        widgets = {
            'publish': forms.CheckboxInput(),
        }