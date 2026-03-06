"""
API URL Configuration - API URL રૂપરેખા

આ ફાઇલ API એન્ડપોઇન્ટ્સ માટે URL રૂપરેખા નક્કી કરે છે.
This file defines the URL configuration for API endpoints.

CRUD ઓપરેશન્સ માટે URL પેટર્ન - URL Patterns for CRUD Operations:
- GET/POST /api/students/ - બધા વિદ્યાર્થીઓની સૂચિ અને નવા વિદ્યાર્થીની રચના
- GET/PUT/DELETE /api/students/<id>/ - ચોક્કસ વિદ્યાર્થીની વિગતો, અપડેટ અને કાઢી નાખવો
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Student CRUD Operations
    path('students/', views.student_list_create, name='student-list-create'),
    path('students/<int:pk>/', views.student_detail_update_delete, name='student-detail-update-delete'),
]

# API એન્ડપોઇન્ટ્સની સમજૂતી - API Endpoints Explanation:
"""
API એન્ડપોઇન્ટ્સ અને તેમનો ઉપયોગ - API Endpoints and Their Usage:

1. GET /api/students/
   - બધા વિદ્યાર્થીઓની સૂચિ મેળવવી
   - Get list of all students
   - ઉદાહરણ: curl http://127.0.0.1:8000/api/students/

2. POST /api/students/
   - નવા વિદ્યાર્થીની રચના કરવી
   - Create new student
   - ઉદાહરણ: curl -X POST http://127.0.0.1:8000/api/students/ \
                 -H "Content-Type: application/json" \
                 -d '{"name": "રાજુ", "email": "raju@example.com", "age": 20}'

3. GET /api/students/<id>/
   - ચોક્કસ વિદ્યાર્થીની માહિતી મેળવવી
   - Get specific student information
   - ઉદાહરણ: curl http://127.0.0.1:8000/api/students/1/

4. PUT /api/students/<id>/
   - વિદ્યાર્થીની માહિતી અપડેટ કરવી
   - Update student information
   - ઉદાહરણ: curl -X PUT http://127.0.0.1:8000/api/students/1/ \
                 -H "Content-Type: application/json" \
                 -d '{"name": "રાજુ પટેલ", "email": "raju.patel@example.com", "age": 21}'

5. DELETE /api/students/<id>/
   - વિદ્યાર્થીને કાઢી નાખવો
   - Delete student
   - ઉદાહરણ: curl -X DELETE http://127.0.0.1:8000/api/students/1/
"""
