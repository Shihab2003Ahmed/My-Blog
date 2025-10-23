from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('trending', 'Trending'),
        ('military', 'Military'),
        ('lifestyle', 'Lifestyle'),
        ('tech', 'Tech'),
    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='trending')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

