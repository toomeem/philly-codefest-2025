# HR Harmony

## Elevator Pitch
HR Harmony is your go-to AI chatbot for instant HR-related answers, making workplace policies and DEI initiatives more accessible. Designed for efficiency and inclusivity, it provides a comfortable space for all employees—especially those who prefer digital interactions. Get the HR support you need, anytime, anywhere!

## Description
HR Harmony is an AI-powered chatbot designed to provide quick and accurate answers to HR-related questions. Whether you need clarification on company policies, DEI initiatives, employee benefits, or workplace guidelines, HR Harmony is here to help—instantly and confidentially.

Our platform enhances accessibility by catering to diverse employee needs, including those who prefer digital interactions over face-to-face conversations. By streamlining HR support, HR Harmony promotes an inclusive and informed workplace, empowering employees with the knowledge they need, anytime and anywhere.

## Tech Stack
HR Harmony is built using modern technologies to ensure efficiency, scalability, and security:

### Frontend:
- **Vite** - Fast development build tool
- **React** - Dynamic user interface
- **DaisyUI** - UI components built on Tailwind CSS
- **Tailwind CSS** - Utility-first CSS framework
- **JavaScript (ES6+)** - Core frontend logic
- **HTML/CSS** - Structuring and styling the application

### Backend:
- **Flask** - Lightweight Python web framework
- **Python** - Backend logic and AI integrations
- **OpenAI API** - AI-powered responses for HR inquiries
- **PostgreSQL** - Robust relational database
- **Amazon RDS** - Cloud-based database management
- **Amazon S3** - Secure file storage
- **Docker** - Containerized application for easy deployment
- **Docker Compose** - Managing multi-container applications

## Getting Started

### Prerequisites
Make sure you have the following installed:
- **Docker & Docker Compose**
- **Python 3.x**
- **Node.js & npm**

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/hr-harmony.git
   cd hr-harmony
   ```
2. Set up the backend:
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Set up the frontend:
   ```sh
   cd ../frontend
   npm install
   ```
4. Start the application using Docker:
   ```sh
   docker-compose up --build
   ```

## Usage
Once the application is running, access it via `http://localhost:5050` in your browser.

