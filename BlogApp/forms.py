from django import forms
from django.contrib.auth.models import User
from .models import Blog

class loginForm(forms.ModelForm):

    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput()) # Because we need to edit the password before save in db.
    class Meta:
        model = User
        fields = ('username','password')
    


class registerForm(forms.ModelForm):

    username = forms.CharField(help_text=False)
    email = forms.CharField(label="Email:")
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username','email','password')

    def clean(self):
        formData = super().clean()
        email = formData['email']
        password = formData['password']
        password_confirm = formData['password_confirm']

        # Check passwords are match
        if password != password_confirm:
            raise forms.ValidationError("Passwords not match")

        # Check if email exist
        exist = User.objects.filter(email=email)
        if exist:
            raise forms.ValidationError("Email Exist")




class createBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','blog_picture']

    def __init__(self, user, *args, **kwargs): # Add the init method request.user
        self.user = user
        super().__init__(*args, **kwargs)


    def clean(self):
        # Check if the user have blog
        blog = Blog.objects.filter(user=self.user)
        if blog:
            raise forms.ValidationError("You already have a blog, you can update it in your profile")


class updateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','blog_picture']






