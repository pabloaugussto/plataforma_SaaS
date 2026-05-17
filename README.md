# 🚀 Intelligent SaaS Helpdesk Platform

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A modern, responsive, and robust IT Helpdesk ticketing system designed for B2B environments. Built with a powerful Django backend and a clean, dynamic Vanilla JavaScript frontend, this platform streamlines support requests, tracks ticket lifecycles, and provides real-time dashboard analytics.

## ✨ Key Features

* **Role-Based Access Control:** Distinct interfaces and permissions for Support Technicians and Clients.
* **Ticket Management (CRUD):** Users can easily open, track, and categorize support tickets with priorities (Low, Medium, High).
* **Interactive Analytics Dashboard:** Real-time KPI cards and dynamic charts (powered by Chart.js) providing an overview of system health and ticket status.
* **Automated Audit Logs:** Background tracking of every state change within a ticket to ensure accountability and history tracking.
* **Modern UI/UX:** Custom CSS architecture utilizing CSS Variables for a cohesive Dark Blue & Orange brand identity, featuring smooth transitions and user-friendly form designs.

## 🛠️ Tech Stack

* **Backend:** Python 3, Django
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js
* **Database:** SQLite (Development)
* **Architecture:** MVT (Model-View-Template)

## 📸 Screenshots

*(You can add screenshots of your project here later!)*
## ⚙️ Local Setup & Installation

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.x installed
* Git installed

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/plataforma_SaaS.git](https://github.com/YOUR_GITHUB_USERNAME/plataforma_SaaS.git)
   cd plataforma_SaaS

2.Create and activate a virtual environment:
Windows: python -m venv venv
venv\Scripts\activate

Linux: python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4.Run database migrations:
python manage.py migrate

5.Create a superuser (Admin) to access the system:
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver

7.Access the platform:  

Open your browser and navigate to http://127.0.0.1:8000/

Admin Panel available at http://127.0.0.1:8000/admin/

🛣️ Roadmap / Future Enhancements
[ ] Connect Chart.js to live backend data.

[ ] Technician detailed view to reply and update ticket status.

[ ] Keyword-based intelligent ticket routing.

[ ] Email notifications for ticket updates.

Developed with 💡 and ☕ by Pablo Augusto + Gemini AI

