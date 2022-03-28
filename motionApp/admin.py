from django.contrib import admin
from .models import Order, CreateStaff, Jobs, Feedback


admin.site.register(Order)
admin.site.register(CreateStaff)
admin.site.register(Jobs)
admin.site.register(Feedback)