from django.db import models


class Student(models.Model):
    """
    Student Model
    
    This model is used to store student information.
    
    Fields:
    - name: Student Name
    - email: Student Email
    - age: Student Age
    - created_at: Creation Time
    - updated_at: Update Time
    """
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    age = models.IntegerField(verbose_name="Age")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Time")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update Time")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email})"

    def get_absolute_url(self):
        return f"/api/students/{self.id}/"
