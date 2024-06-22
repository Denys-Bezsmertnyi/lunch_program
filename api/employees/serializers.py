from rest_framework import serializers
from apps.employees.models import Employee
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'gender', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        employee = Employee.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            password=validated_data['password']
        )
        return employee


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'password2', 'phone_number', 'age', 'gender']

    def save(self, **kwargs):
        employee = Employee(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            age=self.validated_data['age'],
            gender=self.validated_data['gender']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        employee.set_password(password)
        employee.save()
        return employee


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['age'] = user.age
        token['gender'] = user.gender
        return token
