from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()

    def __str__(self):
        return self.title
