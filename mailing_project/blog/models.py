from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
