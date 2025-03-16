from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'กรอกชื่องาน'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'รายละเอียด'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }