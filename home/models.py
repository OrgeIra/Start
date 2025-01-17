from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    

    
