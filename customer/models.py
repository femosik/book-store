from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Purchase(models.Model):
    customer = models.ForeignKey(to='customer.Customer', related_name='customer', on_delete=models.CASCADE,)
    book = models.ForeignKey(to='books.Book', related_name='book', on_delete=models.CASCADE, )
