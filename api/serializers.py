from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Student Serializer
    
    This serializer is used to convert the Student model to JSON format.
    
    CRUD Operations:
    - Create: Create new student
    - Read: Read student information
    - Update: Update student information
    - Delete: Delete student
    """
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'age', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_email(self, value):
        """
        Email Validation
        Check if email is valid
        """
        # Exclude current student when updating
        if self.instance and self.instance.email == value:
            return value
            
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists")
        return value
    
    def validate_age(self, value):
        """
        Age Validation
        Age should be between 0 and 150
        """
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age should be between 0 and 150")
        return value
