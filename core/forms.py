from django import forms
from core.models import Post

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'publish': forms.CheckboxInput(),
        }
class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'publish': forms.CheckboxInput(),
        }