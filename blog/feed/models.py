from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='blog_photos/', blank=True, null=True)
    author_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    likes = models.ManyToManyField(User, related_name='liked_blogs', blank=True)
    favorites = models.ManyToManyField(User, related_name='favorited_blogs', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from title if not provided
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def like_count(self):
        return self.likes.count()

    def favorite_count(self):
        return self.favorites.count()

    def __str__(self):
        return self.title
