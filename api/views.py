from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def student_list_create(request):
    """
    Student List and Create
    
    GET: Get all students list
    POST: Create new student
    """
    if request.method == 'GET':
        # Get all students
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            'message': 'All students list',
            'data': serializer.data,
            'count': students.count()
        })
    
    elif request.method == 'POST':
        # Create new student
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Student created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error: Failed to create student',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    """
    Student Details, Update and Delete
    
    GET: Get specific student details
    PUT: Update student information
    DELETE: Delete student
    """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({
            'message': f'Student with ID {pk} not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Get student details
        serializer = StudentSerializer(student)
        return Response({
            'message': f'Details of student {student.name}',
            'data': serializer.data
        })
    
    elif request.method == 'PUT':
        # Update student information
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f'Student {student.name} updated successfully',
                'data': serializer.data
            })
        return Response({
            'message': 'Error: Failed to update student',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Delete student
        student_name = student.name
        student.delete()
        return Response({
            'message': f'Student {student_name} deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)


def home(request):
    """
    Serve the HTML frontend page
    """
    return render(request, 'index.html')
