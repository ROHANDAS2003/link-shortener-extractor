# Link shortener Extractor

1. **Clone the Repository:**
    - Open your terminal or command prompt.
    - Navigate to the directory where you want to clone the project.
    - Use the following command to clone the project from GitHub:

git clone <https://github.com/your-username/link-shortener-extractor.git>

(Replace your-username with your actual GitHub username and link-shortener-extractor with the repository name if different.)

1. **Navigate to the Project Directory:** After cloning the repository, change to the project directory:

cd link-shortener-extractor

1. **Set Up a Python Virtual Environment (Optional but Recommended):** It's a good practice to create a virtual environment for your Python projects to manage dependencies.
    - **Create a virtual environment:**

On Windows:

python -m venv venv

On macOS/Linux:

python3 -m venv venv

- - **Activate the virtual environment:**

On Windows:

.\\venv\\Scripts\\activate

On macOS/Linux:

source venv/bin/activate

1. **Install Dependencies:** The project has a dependency on pyshorteners for URL shortening. Use pip to install this dependency:

pip install pyshorteners

1. **Run the Program:** After installing the required dependencies, run the program by executing the Python file.

python link_shortener_extractor.py

If the script is named differently, use the appropriate file name (e.g., python main.py).

### Folder Structure

When the project is cloned, the typical folder structure will look like this:

link-shortener-extractor/

│

├── venv/ (if virtual environment is set up)

│

├── link_shortener_extractor.py (Main Python script)

│

├── README.md (Project documentation)

│

├── requirements.txt (optional, can be added for dependency management)

│

└── .gitignore (optional, for ignoring unnecessary files)

### Setting up requirements.txt (Optional)

To make dependency installation

easier for future users, you can create a requirements.txt file in the project directory. This file contains a list of all the dependencies required for the project. To set it up:

1. **Create requirements.txt:**

If you're in a virtual environment and have already installed the dependencies (e.g., pyshorteners), you can automatically generate this file:

pip freeze > requirements.txt

This will list all the installed packages and their versions in the requirements.txt file.

1. **Installing Dependencies from requirements.txt:**

If the file exists in the project, users can simply run the following command to install all necessary dependencies:

pip install -r requirements.txt

### Running the Program

- After following all the steps above, the user can run the program using the command:

python link_shortener_extractor.py

This will start the script, prompting the user to choose between shortening a link or extracting a real URL from a shortened one.

### Recap of Commands

1. Clone the repository:

git clone <https://github.com/your-username/link-shortener-extractor.git>

1. Navigate to the project directory:

cd link-shortener-extractor

1. Set up and activate a virtual environment (optional):
    - **Windows:**

python -m venv venv

.\\venv\\Scripts\\activate

- - **macOS/Linux:**

python3 -m venv venv

source venv/bin/activate

1. Install dependencies:

pip install pyshorteners

Or, if requirements.txt exists:

pip install -r requirements.txt

1. Run the program:

python link_shortener_extractor.py