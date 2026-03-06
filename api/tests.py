from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Student


class StudentAPITestCase(TestCase):
    """
    વિદ્યાર્થી API ટેસ્ટ કેસ - Student API Test Case
    
    CRUD ઓપરેશન્સની ચકાસણી કરવા માટે ટેસ્ટ કેસ
    Test case to verify CRUD operations
    """
    
    def setUp(self):
        self.client = APIClient()
        self.student_data = {
            'name': 'ટેસ્ટ વિદ્યાર્થી',
            'email': 'test@example.com',
            'age': 20
        }
        self.student = Student.objects.create(**self.student_data)
    
    def test_get_all_students(self):
        """બધા વિદ્યાર્થીઓ મેળવવાનો ટેસ્ટ - Test to get all students"""
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
    
    def test_create_student(self):
        """નવા વિદ્યાર્થી બનાવવાનો ટેસ્ટ - Test to create new student"""
        new_student_data = {
            'name': 'નવો વિદ્યાર્થી',
            'email': 'new@example.com',
            'age': 22
        }
        response = self.client.post('/api/students/', new_student_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
    
    def test_get_single_student(self):
        """એક વિદ્યાર્થી મેળવવાનો ટેસ્ટ - Test to get single student"""
        response = self.client.get(f'/api/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], 'ટેસ્ટ વિદ્યાર્થી')
    
    def test_update_student(self):
        """વિદ્યાર્થી અપડેટ કરવાનો ટેસ્ટ - Test to update student"""
        updated_data = {
            'name': 'અપડેટેડ વિદ્યાર્થી',
            'email': 'updated@example.com',
            'age': 21
        }
        response = self.client.put(f'/api/students/{self.student.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'અપડેટેડ વિદ્યાર્થી')
    
    def test_delete_student(self):
        """વિદ્યાર્થી કાઢી નાખવાનો ટેસ્ટ - Test to delete student"""
        response = self.client.delete(f'/api/students/{self.student.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)
