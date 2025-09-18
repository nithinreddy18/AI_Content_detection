# AI Content Detection

A Django-based web application that uses NLP models (such as RoBERTa with Hugging Face Transformers) to detect whether a given text is **AI-generated** or **human-written**.  

---

## 🚀 Features
- User-friendly web interface built with **Django**.  
- Text classification using **Transformers** (RoBERTa).  
- Simple and clean project structure for extensibility.  
- SQLite database for quick setup (default).  

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x, Python 3.13  
- **AI Model:** Hugging Face Transformers (RoBERTa)  
- **Frontend:** Django Templates, Bootstrap 5  
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)  

---

## 📂 Project Structure
```AI_Content_Detect/
│── AI_Content_Detect/ # Main Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
│── app_ai/ # Main application
│ ├── templates/ # HTML templates
│ ├── static/ # Static files (CSS, JS)
│ ├── views.py # App logic
│ └── models.py # Database models
│
│── env/ # Virtual environment
│── db.sqlite3 # Default database
│── manage.py # Django project manager



