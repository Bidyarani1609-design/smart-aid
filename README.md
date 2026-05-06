# Smart Aid — AI-Based Early Detection of Child Malnutrition

## Project Overview

Smart Aid is an AI-powered healthcare project designed to assist in the early detection of child malnutrition using image analysis and BMI-based health evaluation.

The system takes:

- Child image
- Height
- Weight

and provides:

- AI prediction
- BMI calculation
- Risk level assessment
- Health result

This project was developed as an academic AI + Full Stack project using React, FastAPI, TensorFlow, and CNN/ResNet50.

---

# Features

- Child image upload
- AI-based malnutrition prediction
- BMI calculation
- Risk level detection
- FastAPI AI backend
- React frontend interface
- TensorFlow/Keras model integration
- Frontend + Backend API communication
- Localhost execution support

---

# Tech Stack

## Frontend
- React
- Vite
- Tailwind CSS

## Backend
- Node.js
- Express.js
- FastAPI

## AI / Machine Learning
- TensorFlow
- Keras
- CNN
- ResNet50

---

# Project Architecture

Child Image + Height + Weight
↓
React Frontend
↓
Express Backend
↓
FastAPI AI API
↓
TensorFlow Model Prediction
↓
BMI Logic
↓
Final Health Result

---

# Folder Structure

```bash
smart-aid/
│
├── frontend/
├── backend/
├── ai_model/
├── dataset/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── docs/
├── results/
├── screenshots/
├── README.md
└── TEAM_SETUP_GUIDE.md
```

---

# Installation Guide

## 1. Clone or Extract Project

```bash
unzip smart-aid.zip
```

---

# Backend Setup

## Install dependencies

```bash
cd backend
npm install
```

## Run backend

```bash
npm start
```

Backend runs on:

```bash
http://localhost:5000
```

---

# AI API Setup

## Create virtual environment

```bash
python -m venv .venv
use python --version3.11.9 
```

## Activate environment

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Python dependencies

```bash
pip install -r ai_model/requirements.txt
```

---

## Run FastAPI server

```bash
uvicorn ai_model.ai_api:app --reload --host 127.0.0.1 --port 8000
```

AI API runs on:

```bash
http://localhost:8000
```

---

# Frontend Setup

## Install dependencies

```bash
cd frontend
npm install
```

---

## Run frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# System Workflow

1. User uploads child image
2. User enters height and weight
3. Frontend sends data to backend
4. Backend forwards request to FastAPI AI server
5. TensorFlow model predicts malnutrition category
6. BMI is calculated
7. Final health result is returned

---

# Safety Features Added

- File type validation
- Backend image validation
- Prediction crash prevention
- Error handling system
- Loading state protection

---

# Future Improvements

- Larger dataset
- Better model accuracy
- Cloud deployment
- Real-time webcam support
- Mobile application
- Doctor dashboard
- Multi-language support

---

# Academic Purpose

This project was developed for educational and academic purposes as part of an AI + Full Stack healthcare innovation project.

---

# Authors

- Bidya Rani (ua2503cdh542)
- Urvashi Rajput (ua2503cdh339)
- Vidya Rana (ua2503cdh346)

---

# License

Academic Use Only