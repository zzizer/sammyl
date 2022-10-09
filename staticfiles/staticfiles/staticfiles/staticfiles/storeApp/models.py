from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categorie'
    
class Product(models.Model):
    name = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    unitPrice = models.FloatField(default=0,null=True)
    description = models.TextField(max_length=200, null=True)
    is_digital = models.BooleanField(null=True, default=False)
    img = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url    
    
    class Meta:
        verbose_name = 'All Product'
    
class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True,max_length=254)
    #telnumber = models.CharField(null=True,max_length=50)
    #address = models.CharField(null=True, max_length=50)
    #city = models.CharField(null=True, max_length=50)
    #state = models.CharField(null=True, max_length=50)
    #zip_code = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        verbose_name = 'Customer'    
    
class Order(models.Model):
    customer =models.ForeignKey(Customer,blank=True, null=True,on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete  = models.BooleanField(default = False)
    transaction_id = models.CharField(null=True, max_length=100)
    
    def __str__(self):
        return str(self.date_ordered)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product =models.ForeignKey(Product,blank=True, null=True,on_delete=models.SET_NULL)
    order = models.ForeignKey(Order,blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default = 0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date_added
    
    @property
    def get_total(self):
        total = self.product.unitPrice * self.quantity
        return total