from django.urls import path
from .views import CustomerList, CustomerDetail, EmployeeList, EmployeeDetail, UserProfileList, UserProfileDetail

urlpatterns = [
    path('users/user_profiles/', UserProfileList.as_view(), name='user_profile-list'),
    path('users/user_profiles/<int:pk>/', UserProfileDetail.as_view(), name='user_profile-detail'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
]