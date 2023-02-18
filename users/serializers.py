from rest_framework import serializers
from .models import Customer, Employee, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    @staticmethod
    def get_name(obj):
        user_profile = UserProfile.objects.get(user=obj.user)
        return f'{user_profile.last_name} {user_profile.first_name}'

    class Meta:
        model = Customer
        fields = '__all__'
        extra_fields = ['name']


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    @staticmethod
    def get_name(obj):
        user_profile = UserProfile.objects.get(user=obj.user)
        return f'{user_profile.last_name} {user_profile.first_name}'

    class Meta:
        model = Employee
        fields = '__all__'
        extra_fields = ['name']
