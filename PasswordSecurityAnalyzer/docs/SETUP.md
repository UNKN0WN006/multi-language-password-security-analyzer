# Setup Instructions for Password Security Analyzer

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **.NET 6+ SDK**: Required for the C# frontend.
- **JDK 17+**: Required for the Java backend.
- **Python 3.9+**: Required for the analytics service.
- **Node.js 18+**: Required for development tools.
- **Git**: For version control and cloning the repository.

## Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone <your-repo>
cd PasswordSecurityAnalyzer
```

## Backend Setup

Navigate to the backend directory and build the project using Maven:

```bash
cd backend
mvn clean install
```

## Analytics Setup

Navigate to the analytics directory and install the required Python packages:

```bash
cd analytics
pip install -r requirements.txt
```

## Frontend Setup

Navigate to the frontend directory and restore the NuGet packages:

```bash
cd ../frontend
dotnet restore
```

## Running the Application

To run all services, execute the following script:

```bash
cd ../scripts
./run-dev.sh
```

## Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```
HIBP_API_KEY=your_hibp_api_key
JAVA_API_URL=http://localhost:8080
PYTHON_API_URL=http://localhost:5000
```

## Accessing the Application

Once all services are running, you can access the application through the frontend interface. The backend and analytics services will communicate seamlessly to provide real-time password analysis and recommendations.

## Troubleshooting

If you encounter any issues during setup or execution, please refer to the documentation in the `docs` directory or check the GitHub issues page for solutions.