from django.contrib import admin

# Register your models here.
from .models import Customer, User, UserProfile, Employee

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Employee)
