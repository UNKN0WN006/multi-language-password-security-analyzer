# API Documentation for Password Security Analyzer

## Overview
The Password Security Analyzer provides a set of API endpoints for analyzing password strength, checking for breaches, and comparing hashing algorithms. This document outlines the available endpoints, their request and response formats.

## Base URL
```
http://localhost:8080/api
```

## Endpoints

### 1. Analyze Password Strength
- **Endpoint:** `/analyze`
- **Method:** `POST`
- **Request Body:**
```json
{
  "password": "string"
}
```
- **Response:**
```json
{
  "strength": "string",
  "length": "integer",
  "has_uppercase": "boolean",
  "has_numbers": "boolean",
  "has_special_characters": "boolean",
  "suggestions": ["string"]
}
```

### 2. Check Password Breach
- **Endpoint:** `/breach`
- **Method:** `POST`
- **Request Body:**
```json
{
  "password": "string"
}
```
- **Response:**
```json
{
  "breached": "boolean",
  "breach_info": {
    "count": "integer",
    "last_breach": "string"
  }
}
```

### 3. Hash Comparison
- **Endpoint:** `/hash/compare`
- **Method:** `POST`
- **Request Body:**
```json
{
  "password": "string",
  "hashes": {
    "md5": "string",
    "sha256": "string",
    "bcrypt": "string"
  }
}
```
- **Response:**
```json
{
  "results": {
    "md5": "boolean",
    "sha256": "boolean",
    "bcrypt": "boolean"
  }
}
```

## Error Handling
Responses will include an error object in the following format in case of failure:
```json
{
  "error": {
    "code": "integer",
    "message": "string"
  }
}
```

## Notes
- Ensure that the password is sent securely over HTTPS.
- The API is designed to handle multiple requests concurrently.