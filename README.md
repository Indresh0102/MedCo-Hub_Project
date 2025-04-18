# MedCo-Hub_Project
A real-world healthcare e-commerce platform called MedCo-Hub, built with Django and React to simulate industry-grade development practices.

# MedCo-Hub 🏥💊

MedCo-Hub is a real-world healthcare e-commerce platform built using Django (Backend) and React (Frontend). It simulates how real clinics, pharmacies, and patients interact through a medical marketplace.

## 👨‍⚕️ What It Does
- Patients can search and order medicines
- Clinics can prescribe medicines and refer
- Pharmacies manage inventory and deliver orders

## 🛠️ Tech Stack
- **Frontend**: React + Tailwind CSS
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Design**: Figma (Wireframes)
- **DevOps**: Docker (optional, coming soon)
- **Version Control**: Git + GitHub

## 📂 Project Structure (planned)
- `/frontend` → React App
- `/backend` → Django App
- `/docs` → Design files, wireframes

## 🎯 Goal
Simulate building a scalable, production-ready healthcare platform as done by real companies in industry.

## 📅 Sprint Progress
- ✅ Sprint 1: GitHub repo, .gitignore, setup
- 🔜 Sprint 2: Wireframes, Auth flows

## 🧩 UI Flow (Figma)

Below is the wireframe showing the main screens and navigation flow of the MedCo-Hub application.

![MedCo-Hub UI Flow](assets/Figma_UIUX_Flow.png) 

---
# MedCo-Hub API
## Authentication
Uses JWT (SimpleJWT)
- `POST /api/token/` - Get token (login)
- `POST /api/token/refresh/` - Refresh token

## Medicines Endpoint
- `GET /api/v1/medicines/` - List medicines
- `POST /api/v1/medicines/` - Add medicine (admin only)
- `GET /api/v1/medicines/<id>/` - Get medicine detail
- `PUT/PATCH/DELETE` - Update/Delete medicine

## Sample POST data
```json
{
  "name": "Paracetamol",
  "brand": "Generic",
  "price": 15.0,
  "stock": 100,
  "mg": 500,
  "expiry_date": "2025-12-31T00:00:00Z"
}
```
## 💼 For Interviewers:
This project is structured like a real-world product — complete with version control, modular code, API integration, and user-centered design.
