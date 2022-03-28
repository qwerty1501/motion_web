from django.urls import path
from .views import OrderCreateListView, CreateStaffCreateListView, JobsCreateListView, FeedbackCreateListView
from .views import OrderDeleteView, CreateSteffDeleteView, JobsDeleteView, FeedbackDeleteView

urlpatterns = [
    path('order/', OrderCreateListView.as_view()),
    path('createstaff/', CreateStaffCreateListView.as_view()),
    path('jobs/', JobsCreateListView.as_view()),
    path('feedback/', FeedbackCreateListView.as_view()),
    # Delete
    path('order/delete/<int:pk>/', OrderDeleteView.as_view()),
    path('createstaff/delete/<int:pk>', CreateSteffDeleteView.as_view()),
    path('jobs/delete/<int:pk>', JobsDeleteView.as_view()),
    path('feedback/delete/<int:pk>', FeedbackDeleteView.as_view()),
]