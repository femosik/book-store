from django.contrib import admin

from customer.models import Customer, Purchase

admin.site.register(Customer)

admin.site.register(Purchase)
