from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Order(models.Model):
    

    SIZE=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large')
    )

    ORDER_STATUS = (
        ('PNDING','pending'),
        ('DELIVERING','delivering'),
        ('DELIVERED','delivered')
    )
    customer =models.ForeignKey(User,on_delete=models.CASCADE)
    size = models.CharField(max_length=20,choices=SIZE,default=SIZE[0][0])
    order_status = models.CharField(max_length=20,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"ORDER {self.size} by {self.customer.id}"
