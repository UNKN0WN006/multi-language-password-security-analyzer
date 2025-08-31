#!/bin/bash

# This script sets up the development environment for the Password Security Analyzer project.

# Clone the repository
git clone <your-repo-url>
cd PasswordSecurityAnalyzer

# Backend setup
cd analytics
pip install -r requirements.txt
cd ../backend
mvn clean install

# Frontend setup
cd ../frontend
dotnet restore

# Notify user of successful setup
echo "Setup completed successfully. You can now run the application."