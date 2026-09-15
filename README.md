
# Social Media Feed

🌐 **Live Application:** https://social-media-feed-134a.onrender.com/

A simple and professional **Social Media Feed web application** developed using Python Flask with SQLite database integration, automated testing, CI/CD, and cloud deployment.

## 🚀 Features

- Create and publish posts
- Display posts in latest-first order
- Like posts
- Delete posts
- Username and post content validation
- SQLite database storage
- Responsive web interface
- Automated testing using Pytest
- CI/CD using GitHub Actions
- Cloud deployment using Render

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| Database | SQLite, Flask-SQLAlchemy |
| Frontend | HTML, CSS |
| Testing | Pytest |
| Version Control | Git, GitHub |
| CI/CD | GitHub Actions |
| Cloud | Render |
| Production Server | Gunicorn |

## 📁 Project Structure

```text
social-media-feed/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── error.html
│
├── tests/
│   └── test_app.py
│
├── app.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── .python-version
└── README.md
````

## 🏗️ Application Architecture

```text
User
  ↓
HTML / CSS Frontend
  ↓
Flask Application
  ↓
Flask-SQLAlchemy
  ↓
SQLite Database
```

## 🔄 DevOps & CI/CD Workflow

```text
Local Development
       ↓
      Git
       ↓
    GitHub
       ↓
GitHub Actions
   Automated Tests
       ↓
    Render
  Cloud Deployment
       ↓
Live Application
```

When changes are pushed to the `main` branch:

1. GitHub Actions automatically runs the tests.
2. If the deployment configuration is valid, Render automatically deploys the latest code.
3. The updated application becomes available through the live URL.

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/mohammad-724/social-media-feed.git
cd social-media-feed
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🧪 Testing

Run the automated tests with:

```bash
pytest
```

The project currently includes tests for the main application functionality.

## ☁️ Cloud Deployment

The application is deployed on **Render** using **Gunicorn** as the production WSGI server.

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

### Live Application

[https://social-media-feed-134a.onrender.com/](https://social-media-feed-134a.onrender.com/)

## 📌 Project Objective

This project demonstrates the complete lifecycle of a Flask web application:

**Development → Database Integration → Testing → Git/GitHub → CI/CD → Cloud Deployment**

It provides practical exposure to **Web Development, DevOps, CI/CD, Git, GitHub Actions, and Cloud Computing**.

## 👨‍💻 Author

**Mohammad Azmath Ali**

GitHub: [https://github.com/mohammad-724](https://github.com/mohammad-724)

```

