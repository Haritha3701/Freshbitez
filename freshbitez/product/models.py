from django.db import models

# Create your models here.

class products(models.Model):
    productname=models.CharField(max_length=300)
    img=models.ImageField(upload_to="pictures")
    orgprice=models.FloatField()
    discount=models.FloatField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date",)

class comments(models.Model):
    pro=models.ForeignKey(products,related_name="cmt",on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    msg=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    