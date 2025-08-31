# Password Security Analyzer

## Project Overview
The Password Security Analyzer is a comprehensive tool designed to analyze password strength, detect breaches, and provide security recommendations. This application leverages C#, Java, and Python to deliver real-time insights through a modern and responsive dashboard.

## Key Features
- Real-time password strength analysis
- Data breach checking using the HaveIBeenPwned API
- Multiple hashing algorithm comparisons
- Visual strength progression meters
- Smart improvement suggestions
- Cross-platform desktop application

## Architecture
The application is structured into three main components:
- **C# Frontend**: A WPF desktop application providing the user interface.
- **Java API Server**: A Spring Boot REST backend handling requests and responses.
- **Python Analytics**: A Flask service performing security analysis and breach detection.

## Setup Instructions
To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repo>
   cd PasswordSecurityAnalyzer
   ```

2. **Backend setup**:
   - Navigate to the analytics directory and install the required Python packages:
     ```bash
     cd analytics
     pip install -r requirements.txt
     ```
   - Navigate to the backend directory and build the Java application:
     ```bash
     cd ../backend
     mvn clean install
     ```

3. **Frontend setup**:
   - Restore the NuGet packages for the C# frontend:
     ```bash
     cd ../frontend
     dotnet restore
     ```

4. **Run all services**:
   ```bash
   ./scripts/run-dev.sh
   ```

## Usage Guidelines
- Launch the application and enter a password in the input field.
- Observe real-time feedback on password strength and breach status.
- Review the improvement suggestions provided based on the analysis.
- Explore hash comparisons for different algorithms.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.