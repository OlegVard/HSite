from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    music = models.TextField()
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
