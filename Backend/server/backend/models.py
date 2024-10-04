from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    email = models.EmailField(unique= True)
    language = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class UserPost(models.Model):
    img = models.URLField(null = True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    #post_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    likes = models.IntegerField()
    

    def __str__(self):
        return self.username

class Market_prod(models.Model):
    title = models.CharField(max_length=255)
    img = models.URLField()
    price = models.IntegerField()
    description = models.TextField()
    duration = models.IntegerField()
    type = models.CharField(max_length = 255) #Renting or buying



