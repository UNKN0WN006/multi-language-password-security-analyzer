#!/bin/bash

# Build the backend Java application
cd backend
mvn clean package

# Build the analytics Python application
cd ../analytics
pip install -r requirements.txt

# Build the frontend C# application
cd ../frontend
dotnet build PasswordAnalyzer.sln

# Notify user of successful build
echo "Build completed successfully for all components."