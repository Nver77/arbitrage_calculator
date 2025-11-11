# 🎯 Arbitrage Calculator (Django + Bootstrap)

A clean and responsive Django web app that helps users calculate potential **arbitrage opportunities** based on bookmaker odds.  
The app supports between **2 and 8 coefficients**, automatically detects if an arbitrage exists, and stores the last 10 calculations in a simple database table.

---

## 🚀 Features

- ✅ Supports from **2 up to 8 odds**
- ⚙️ Dynamic form — updates the number of input fields instantly
- 📊 Calculates arbitrage margin using:
1 - ((xy)/(x+y))100 → for 2 odds
1 - ((xyz)/(xz+xy+y*z))*100 → for 3 odds

markdown
Copy code
and so on automatically
- 🧮 Displays:
- **Arbitrage Found (🔥)** — highlighted in red
- **No Arbitrage (✅)** — highlighted in green
- **Zero Arbitrage** if the margin equals 0
- 💾 Saves the last 10 calculations in the database
- 🎨 Modern, Bootstrap-based design (inspired by [surebet.com](https://en.surebet.com/calculator))

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Django 5.2**
- **Bootstrap 5**
- **SQLite3**

---

## ⚙️ Installation

1. **Clone the repository**
 ```bash
 git clone https://github.com/YOUR_USERNAME/arbitrage-calculator.git
 cd arbitrage-calculator
Create and activate a virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run migrations

bash
Copy code
python manage.py migrate
Start the development server

bash
Copy code
python manage.py runserver
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:8000/
📸 Preview
(Optional — add a screenshot here)
You can take a screenshot of your running app and place it here, for example:

scss
Copy code
![Arbitrage Calculator Screenshot](static/images/preview.png)
🧩 Project Structure
Copy code
arbitrage_project/
│
├── calculator/
│   ├── templates/
│   │   └── calculator/
│   │       └── index.html
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── arbitrage_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── db.sqlite3
├── manage.py
└── requirements.txt
💡 Future Improvements
Add user authentication to save personal arbitrage history

Export results as PDF or Excel

Add real bookmaker API integration

Create a REST API endpoint

👨‍💻 Author
Nver Pogosyan
📍 Based in Armenia
💼 Passionate about Django, Data Science, and Web Development
📧 [Add your email here if you want to show it publicly]

📜 License
This project is open-source and available under the
