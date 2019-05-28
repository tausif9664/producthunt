from django.db import models
from django.contrib.auth.models import User
# Create your models with title,date,image, text.
class Product(models.Model):
    title = models.CharField(max_length=250)
    pub_date= models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    def summry(self):
        return self.body[0:100]

    def __str__(self):
        return self.title