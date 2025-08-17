📝 Django Blog API
A Django REST Framework powered API for creating, reading, updating, and deleting blog posts.
Built with Python, Django, and DRF to demonstrate clean code, API design, and backend development skills.

---

🚀 Features
Create, Read, Update, and Delete blog posts (CRUD)

RESTful API with JSON responses

Auto-generated API documentation using Django REST Framework

Database support (SQLite by default, easily switchable to PostgreSQL/MySQL)

Modular and maintainable code structure

---

🛠️ Tech Stack
Backend: Django, Django REST Framework

Database: SQLite (default) / PostgreSQL

Language: Python 3.x

Tools: Git, Pipenv/venv, Postman (for testing)

---

📦 Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/kumar-kaushal-dev/django-blog-api.git
cd django-blog-api

2️⃣ Create Virtual Environment

python -m venv env
source env/bin/activate   # On Mac/Linux
env\Scripts\activate      # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py migrate

5️⃣ Create Superuser (Optional)

python manage.py createsuperuser

6️⃣ Run the Development Server

python manage.py runserver

---
## 🚀 API Endpoints

| Method  | Endpoint          | Description          |
|---------|------------------|----------------------|
| GET     | `/api/posts/`    | List all blog posts  |
| POST    | `/api/posts/`    | Create new post      |
| GET     | `/api/posts/{id}/` | Retrieve a post     |
| PUT     | `/api/posts/{id}/` | Update a post       |
| DELETE  | `/api/posts/{id}/` | Delete a post       |

---

🧪 Example API Request
POST /api/posts/
{
    "title": "My First Blog Post",
    "content": "This is my first blog post using Django REST Framework!"
}

Response:
{
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is my first blog post using Django REST Framework!",
    "published_date": "2025-08-08T10:00:00Z"
}

🤝 Contributing
Pull requests are welcome! Please open an issue to discuss changes before submitting.

---

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.


