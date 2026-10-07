# Cloud FastAPI Deployment

> Module 03 – Basic Building Monolith API with FastAPI  
> Final Exam: Deploy FastAPI Application to AWS Cloud

## 📋 Overview

A CRUD User API built with **FastAPI** and **PostgreSQL**, designed to be deployed on **AWS Cloud** using EC2, RDS, S3, and GitHub Actions CI/CD.

## 🏗️ Architecture

```
GitHub Actions → SSH Deploy → EC2 Instance (Docker) → RDS (PostgreSQL)
                                    ↕
                              S3 (File Storage)
```

## 🚀 Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL 15.x (Amazon RDS)
- **ORM**: SQLAlchemy
- **File Storage**: Amazon S3 (boto3)
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EC2, RDS, S3, IAM, VPC)

## 📁 Project Structure

```
cloud-fastapi-deployment/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── config.py        # Environment variables configuration
│   ├── db.py            # Database connection (SQLAlchemy)
│   ├── models.py        # Database models (User)
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   ├── s3_service.py    # S3 file upload service
│   └── routers/
│       ├── __init__.py
│       ├── users.py     # User CRUD endpoints
│       └── upload.py    # File upload endpoint
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline
├── .env.example         # Environment variables template
├── .gitignore
├── .dockerignore
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Local development setup
├── requirements.txt     # Python dependencies
└── README.md
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Health status |
| GET | `/users/` | List all users (paginated) |
| GET | `/users/{id}` | Get user by ID |
| POST | `/users/` | Create new user |
| PUT | `/users/{id}` | Update user |
| DELETE | `/users/{id}` | Delete user |
| POST | `/upload/` | Upload file to S3 |

## 🏃 Quick Start (Local Development)

### Option 1: Docker Compose (Recommended)
```bash
# Copy environment file
cp .env.example .env

# Build and run
docker-compose up --build

# Access API docs at http://localhost:8000/docs
```

### Option 2: Manual Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your database credentials

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Deploy to AWS

See the exam instructions for detailed deployment steps:
1. **Part 1**: IAM Configuration
2. **Part 2**: Database Setup with Amazon RDS
3. **Part 3**: File Storage with Amazon S3
4. **Part 4**: Containerization with Docker
5. **Part 5**: Deploy to Amazon EC2
6. **Part 6**: CI/CD Pipeline with GitHub Actions

## 📝 GitHub Actions Secrets Required

| Secret | Description |
|--------|-------------|
| `EC2_HOST` | EC2 public IP address |
| `EC2_USER` | SSH username (ec2-user or ubuntu) |
| `SSH_PRIVATE_KEY` | EC2 key pair private key |
| `DB_USER` | RDS master username |
| `DB_PASSWORD` | RDS master password |
| `DB_HOST` | RDS endpoint |
| `DB_NAME` | Database name |
| `AWS_ACCESS_KEY_ID` | IAM access key |
| `AWS_SECRET_ACCESS_KEY` | IAM secret key |
| `AWS_REGION` | AWS region |
| `S3_BUCKET_NAME` | S3 bucket name |
