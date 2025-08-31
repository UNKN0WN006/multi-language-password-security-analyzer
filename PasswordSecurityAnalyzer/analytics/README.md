# Password Security Analyzer – Analytics Microservice

This microservice is part of the multi-language-password-security-analyzer project. It provides REST API endpoints for analyzing password strength, detecting patterns, and checking for breaches (mocked for local development).

## Features
- Analyze password strength with feedback
- Detect common password patterns
- (Mocked) Check if a password has been breached
- RESTful API built with Flask

## Project Structure
```
PasswordSecurityAnalyzer/
  analytics/
    app.py                # Flask app entry point
    requirements.txt      # Python dependencies
    models/               # Data models
    services/             # Analysis and breach logic
    utils/                # Helper functions
```

## Setup & Usage
1. **Install dependencies**
   ```powershell
   cd PasswordSecurityAnalyzer/analytics
   E:\work_hack\kyh\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
2. **Run the Flask app**
   ```powershell
   E:\work_hack\kyh\.venv\Scripts\python.exe app.py
   ```
3. **API Endpoints**
   - `GET /` – Health check/status
   - `GET /test` – Sample password analysis
   - `POST /api/analyze` – Analyze a password
     - Body: `{ "password": "YourTestPassword123!" }`

## Example Request
```powershell
curl -Uri http://localhost:5000/api/analyze -Method POST -Body '{"password":"YourTestPassword123!"}' -ContentType "application/json"
```

## Notes
- The breach check is mocked for local development.
- Update `services/breach_checker.py` for real breach API integration.
- You can update this README as you add features or change the API.

---

_Last updated: August 31, 2025_
