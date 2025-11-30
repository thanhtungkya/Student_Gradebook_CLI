🎓 Student Gradebook Manager (GUI Edition)

A comprehensive Python desktop application designed to help students manage their academic performance. This project upgrades a traditional Command Line Interface (CLI) into a fully functional Graphical User Interface (GUI) using Tkinter, structured with the Model-View-Controller (MVC) design pattern.

🚀 Key Features

User-Friendly GUI: Built with tkinter and ttk for a modern, native look on macOS and Windows.

MVC Architecture: Clean separation of concerns (Logic, UI, and Control) for better maintainability and scalability.

CRUD Operations: Easily Add, Edit, and Delete courses via intuitive popup forms.

Advanced Data Management:

Search: Real-time filtering of courses by Name or Code.

Sort: Clickable column headers to sort data (e.g., by Score or Credits).

Data Persistence: Grades are automatically saved to gradebook.csv (Excel-compatible) and user settings to config.json.

Smart GPA Calculation: Automatically computes the weighted GPA and provides a semester-based breakdown.

Cross-Platform: Runs smoothly on macOS (Retina display supported), Windows, and Linux.

📂 Project Structure

The project follows industry-standard software engineering practices:

StudentGradebook/
│
├── main.py        # [Controller] Entry point. Coordinates Model and View.
├── model.py       # [Model] Handles business logic, CSV I/O, and calculations.
├── view.py        # [View] Handles UI components, tables, and event listeners.
├── config.py      # [Config] Constants, file paths, and settings.
└── README.md      # Project documentation.


🛠️ Technology Stack

Language: Python 3.x

GUI Framework: Tkinter (Standard Library)

Data Storage: CSV (Structured Data), JSON (Configuration)

Design Pattern: MVC (Model-View-Controller)

⚙️ Installation & Usage

1. Clone the Repository

git clone [https://github.com/thanhtungkya/projectofart.git](https://github.com/thanhtungkya/projectofart.git)
cd projectofart


2. Run the Application

Execute the main.py file to start the program:

# For macOS / Linux
python3 main.py

# For Windows
python main.py


3. First-Time Setup

Upon the first launch, the application will ask for your Student Name.

It will automatically create a data folder at ~/Desktop/Intro_to_IT/ to store your records safely.

📊 Data Storage Location

Your data is stored locally and persists between sessions:

Directory: Desktop/Intro_to_IT/

Files:

gradebook.csv: Contains your course list and grades. You can open this file with Microsoft Excel.

config.json: Stores user preferences.

📸 Screenshots

(Add your application screenshots here to make the README look better)

👨‍💻 Author

Thanh Tung (thanhtungkya)

GitHub: thanhtungkya

Project: Intro to IT - Advanced Track Assignment

Built with ❤️ and Python.