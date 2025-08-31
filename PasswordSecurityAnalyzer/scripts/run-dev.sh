#!/bin/bash

# Navigate to the backend directory and start the Java API server
cd ../backend
mvn spring-boot:run &

# Navigate to the analytics directory and start the Python analytics service
cd ../analytics
python3 app.py &

# Navigate to the frontend directory and start the WPF application
cd ../frontend
dotnet run