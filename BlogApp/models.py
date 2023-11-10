from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Blog(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    blog_picture = models.ImageField(upload_to='blogPicture/',blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self): # Allow the creation of URLs based on an instance of each object Make your absolute URLs unique to each instance object in your Django application using a unique primary key
        return reverse('blog', kwargs={'pk': self.pk})
