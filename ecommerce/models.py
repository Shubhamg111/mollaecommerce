from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    slug=models.SlugField(max_length=100,unique=True)  
    description =RichTextUploadingField(blank=True, null=True) 
    

    def __str__(self):
        return self.name  
    
    def total_products(self):
        if self.product_set.count():
            return self.product_set.count()
        else:
            return "No Products"
        
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    name=models.CharField(max_length=256,null=False, blank=False)
    slug=models.SlugField(max_length=256,unique =True)
    image=models.ImageField(upload_to='media/products')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    isAvailable=models.BooleanField(default=True)
    quantity=models.IntegerField(default=1)
    description=RichTextUploadingField(blank=True, null=True)
   
    def __str__(self):
       return self.name
   
class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to ='media/products')

    def  __str__(self):
        return self.product.name
    
class Banner(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="media/banners")
    is_active=models.BooleanField(default=True)
    description =  RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Settings(models.Model):
    name=models.CharField(max_length=100, unique=True)
    email=models.EmailField(max_length=200,unique=True)
    address=models.CharField(max_length=100, unique=True)
    phone=models.CharField(max_length=16, unique=True)
    favicon=models.ImageField(upload_to='media/favicon')
    logo=models.ImageField(upload_to='media/logo')
    description=RichTextUploadingField(blank=True,null=True)

    def __str__(self) -> str:
        return  self.name
