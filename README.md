# Django REST Framework CRUD API Project

## Project Description

This is a simple Django REST Framework CRUD API project created to manage student information. In this project, you can add, read, update, and delete student information using CRUD operations.

## Installation Process

### 1. Clone the Project
```bash
git clone <repository-url>
cd crud_project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Linux/Mac
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

## CRUD Operations

### Create (Add New Student)

**Usage:**
```bash
curl -X POST http://127.0.0.1:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rajesh Patel",
    "email": "rajesh@example.com",
    "age": 20
  }'
```

**Response:**
```json
{
  "message": "Student created successfully",
  "data": {
    "id": 1,
    "name": "Rajesh Patel",
    "email": "rajesh@example.com",
    "age": 20,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z"
  }
}
```

### Read (Get Student List)

**Get All Students:**
```bash
curl http://127.0.0.1:8000/api/students/
```

**Get Specific Student:**
```bash
curl http://127.0.0.1:8000/api/students/1/
```

**Response:**
```json
{
  "message": "All students list",
  "data": [
    {
      "id": 1,
      "name": "Rajesh Patel",
      "email": "rajesh@example.com",
      "age": 20,
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-01T10:00:00Z"
    }
  ],
  "count": 1
}
```

### Update (Update Student Information)

**Usage:**
```bash
curl -X PUT http://127.0.0.1:8000/api/students/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rajesh Kumar Patel",
    "email": "rajesh.kumar@example.com",
    "age": 21
  }'
```

**Response:**
```json
{
  "message": "Student Rajesh Kumar Patel updated successfully",
  "data": {
    "id": 1,
    "name": "Rajesh Kumar Patel",
    "email": "rajesh.kumar@example.com",
    "age": 21,
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T11:00:00Z"
  }
}
```

### Delete (Remove Student)

**Usage:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/students/1/
```

**Response:**
```json
{
  "message": "Student Rajesh Kumar Patel deleted successfully"
}
```

## Project Structure

```
crud_project/
├── manage.py                 # Django management script
├── requirements.txt          # List of required packages
├── crud_project/            # Main project directory
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
└── api/                     # API application
    ├── __init__.py
    ├── admin.py             # Admin configuration
    ├── apps.py              # Application config
    ├── models.py            # Student model
    ├── serializers.py       # API serializer
    ├── views.py             # API views
    ├── urls.py              # API URL configuration
    └── tests.py             # Test cases
```

## Model Description

### Student Model

**Fields:**
- `name` (CharField): Student name (max 100 characters)
- `email` (EmailField): Student email (unique)
- `age` (IntegerField): Student age
- `created_at` (DateTimeField): Creation time (auto)
- `updated_at` (DateTimeField): Update time (auto)

## API Endpoints

| Method | Endpoint | Description |
|------|----------|------|
| GET | `/api/students/` | List all students |
| POST | `/api/students/` | Create new student |
| GET | `/api/students/<id>/` | Get specific student |
| PUT | `/api/students/<id>/` | Update student |
| DELETE | `/api/students/<id>/` | Delete student |

## Testing

**To Run Tests:**
```bash
python manage.py test api
```

**Test Cases Include:**
- Get all students
- Create new student
- Get specific student
- Update student
- Delete student

## Admin Panel

**To Use Admin Panel:**

1. **Create Superuser:**
```bash
python manage.py createsuperuser
```

2. **Access Admin Panel:**
```
http://127.0.0.1:8000/admin/
```

3. **What you can do in Admin:**
- View student list
- Add new students
- Edit student information
- Delete students

## Additional Information

### Useful Commands

**Create Migration:**
```bash
python manage.py makemigrations
```

**Apply Migration:**
```bash
python manage.py migrate
```

**Run Development Server:**
```bash
python manage.py runserver
```

**Open Shell:**
```bash
python manage.py shell
```

### Supported Features

- ✅ CRUD operations
- ✅ RESTful API
- ✅ JSON responses
- ✅ English messages
- ✅ Validation
- ✅ Error handling
- ✅ Admin panel
- ✅ Testing

### Future Improvements

- 🔄 Authentication and authorization
- 🔄 Pagination
- 🔄 Filtering and search
- 🔄 File upload
- 🔄 API documentation (Swagger/OpenAPI)

## Contact

If you have any questions, please contact.

---

**Thank You!** 🙏
