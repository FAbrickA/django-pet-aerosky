from django import forms
from main.models import Message


class MessageForm(forms.ModelForm):
    _opt = Message._meta

    name = forms.CharField(
        max_length=_opt.get_field('name').max_length,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name",
        }),
    )
    email = forms.EmailField(
        max_length=_opt.get_field('email').max_length,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email address",
        }),
    )
    phone = forms.CharField(
        max_length=_opt.get_field('phone').max_length,
        required=not _opt.get_field('phone').blank,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Phone number",
        }),
    )
    subject = forms.CharField(
        max_length=_opt.get_field('subject').max_length,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject",
        }),
    )
    message = forms.CharField(
        max_length=_opt.get_field('message').max_length,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Write you message here...",
            "style": "height:100px;",
        }),
    )

    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'subject', 'message')
