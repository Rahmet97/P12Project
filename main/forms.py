from django.forms import (
    Form,
    ModelForm,
    CharField,
    Textarea,
    TextInput,
    EmailField,
    EmailInput
)


class CommentForm(Form):
    name = CharField(widget=TextInput(attrs={
        'placeholder': 'Name',
        'class': 'email-bt'
    }))
    email = EmailField(widget=EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'email-bt'
    }))
    phone = CharField(widget=TextInput(attrs={
        'placeholder': 'Phone number',
        'class': 'email-bt'
    }))
    message = CharField(widget=Textarea(attrs={
        'placeholder': 'Message',
        'class': 'massage-bt',
        'rows': 5,
        'id': 'comment'
    }))