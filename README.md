# Social Media Feed

A beginner-friendly Flask project demonstrating local development, Git/GitHub, database integration, and cloud deployment.

## Features

- Create posts with username and content
- Responsive professional interface
- Like posts
- Delete posts
- SQLite database using Flask-SQLAlchemy
- Flash messages and server-side validation
- Render-ready production start command

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5
- CSS3
- Git/GitHub
- Render
- Gunicorn

## Run locally

### 1. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Render deployment

Use these settings for a Render Web Service:

- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

Connect the GitHub repository and deploy the `main` branch.

## Note about SQLite

SQLite is used here for learning and simple deployment practice. For a production-style application with persistent cloud data, migrate to PostgreSQL in a later version.

## Project structure

```text
social-media-feed/
├── app.py
├── requirements.txt
├── .python-version
├── .gitignore
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   └── error.html
└── static/
    └── style.css
```
