from django.db import models
from django.utils import timezone

class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

# News Model
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    year_of_release=models.DateField(default=timezone.now)
    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title

# Upcoming movies
class Upcoming(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    year_of_release=models.DateField(default=timezone.now)
    class Meta:
        verbose_name_plural='Upcoming Movies'

    def __str__(self):
        return self.title

# Comments
class Comment(models.Model):
    news=models.ForeignKey(News,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    comment=models.TextField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.comment



class Actor(models.Model):
    name = models.CharField(max_length=80)
    news = models.ForeignKey(News, on_delete=models.CASCADE)