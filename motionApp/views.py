from django.shortcuts import render
from rest_framework import generics

from .serializers import OrderSerializers, CreateStaffSerializers, JobsSerializers, FeedbackSerializers
from .models import Order, CreateStaff, Jobs, Feedback


class OrderCreateListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    
    
class OrderDeleteView(generics.DestroyAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()
    

class CreateStaffCreateListView(generics.ListCreateAPIView):
    serializer_class = CreateStaffSerializers
    queryset = CreateStaff.objects.all()
    
    
class CreateSteffDeleteView(generics.DestroyAPIView):
    serializer_class = CreateStaffSerializers
    queryset = CreateStaff.objects.all()
    
    
class JobsCreateListView(generics.ListCreateAPIView):
    serializer_class = JobsSerializers
    queryset = Jobs.objects.all()


class JobsDeleteView(generics.DestroyAPIView):
    serializer_class = JobsSerializers
    queryset = Jobs.objects.all()
    
    
class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()
    
    
class FeedbackDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackSerializers()
    queryset = Feedback.objects.all()