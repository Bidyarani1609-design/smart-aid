# Smart Aid — Team Setup Guide

This guide explains how to run the Smart Aid project locally on Windows.

---

# System Requirements

## Recommended

- Windows 10/11
- Python 3.10 or 3.11
- Node.js v18+
- VS Code
- Internet connection for dependency installation

---

# Required Software

## Install Python

Download:
https://www.python.org/downloads/

IMPORTANT:
During installation check:

```txt
Add Python to PATH
```

Verify installation:

```bash
python --version
```

---

# Install Node.js

Download:
https://nodejs.org/

Verify installation:

```bash
node -v
npm -v
```

---

# Project Setup

Extract project ZIP:

```bash
smart-aid.zip
```

Open project in VS Code.

---

# Backend Setup

## Open terminal

```bash
cd backend
```

---

## Install backend dependencies

```bash
npm install
```

---

## Run backend server

```bash
npm start
```

Backend runs at:

```bash
http://localhost:5000
```

---

# AI API Setup

## Open new terminal

Go to project root folder.

---

## Create virtual environment

```bash
python -m venv .venv
```

---

## Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

---

## Install AI dependencies

```bash
pip install -r ai_model/requirements.txt
```

---

## Run FastAPI AI server

```bash
uvicorn ai_model.ai_api:app --reload --host 127.0.0.1 --port 8000
```

AI API runs at:

```bash
http://localhost:8000
```

---

# Frontend Setup

## Open new terminal

```bash
cd frontend
```

---

## Install frontend dependencies

```bash
npm install
```

---

## Run frontend

```bash
npm run dev
```

Frontend runs at:

```bash
http://localhost:5173
```

---

# Full System Run Order

Always start servers in this order:

1. FastAPI AI Server
2. Backend Server
3. Frontend Server

---

# Testing the Project

1. Open browser
2. Go to:

```bash
http://localhost:5173
```

3. Upload child image
4. Enter height
5. Enter weight
6. Click Analyze

---

# Supported Image Formats

Allowed:

- JPG
- PNG

Not Allowed:

- PDF
- TXT
- DOCX
- EXE

---

# Common Errors & Solutions

---

## Error: TensorFlow not found

Solution:

```bash
pip install tensorflow
```

---

## Error: npm not recognized

Solution:
Install Node.js properly and restart terminal.

---

## Error: Port already in use

Solution:

Stop previous process or change port.

---

## Error: Module not found

Solution:

```bash
npm install
```

or

```bash
pip install -r ai_model/requirements.txt
```

---

## Error: Prediction failed

Possible reasons:

- Invalid image
- Corrupted image
- AI API not running
- TensorFlow issue

---

# Recommended VS Code Extensions

- Python
- Pylance
- ES7 React Snippets
- Tailwind CSS IntelliSense

---

# Notes

- Run all servers locally
- Do not delete model file
- Keep folder structure unchanged
- Use proper image files only

---

# Final Project Checklist

Before submission verify:

- Frontend runs
- Backend runs
- AI API runs
- Prediction works
- README exists
- TEAM_SETUP_GUIDE exists
- ZIP cleaned
- node_modules removed
- __pycache__ removed

---

# Academic Use

This project is for educational and academic demonstration purposes.