# Child Health Monitoring API

## Overview
The Child Health Monitoring API is a simple Django REST Framework application designed to help caregivers track the health and vaccination records of children.  
It allows caregivers to:  
- Register and authenticate securely using token-based authentication.  
- Add and manage children under their care.  
- Track health records including height, weight, and notes.  
- Record vaccination status for each child.  
- View full child details including health and vaccination history in one request.

---

## Features
- User Authentication: Token-based authentication for secure access.  
- Child Management: Create, retrieve, update, and delete child records.  
- Health Records: Track child health metrics over time.  
- Vaccination Records: Monitor vaccination status (Pending/Completed).  

---

## Technology Stack
- Backend: Django, Django REST Framework  
- Database: SQLite (development)  
- Authentication: TokenAuthentication (DRF)

---

## API Endpoints

Authentication
POST /api-token-auth/ – Obtain auth token

Children
- GET /api/children/ – List children
- POST /api/children/ – Create child

Health Records
- GET /api/health-records/ – List health records
- POST /api/health-records/ – Create health record

Vaccinations
- GET /api/vaccinations/ – List vaccinations
- POST /api/vaccinations/ – Create vaccination record

----

## Notes

- Status for vaccinations must be one of: PENDING or COMPLETED.
- Only caregivers associated with the logged-in user can manage their children.