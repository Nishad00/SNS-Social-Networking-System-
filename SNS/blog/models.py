# python manage.py sqlmigrate blog 0001
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now_add= True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default = None,upload_to='post_pics')


    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (550,550)
            img.thumbnail(output_size)
            img.save(self.image.path)

    
    def snippet(self):
        return self.content[:300] + '....'


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    