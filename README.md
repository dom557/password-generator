Password Generator
This is a versatile password generator offering both a simple command-line interface and a user-friendly graphical user interface (GUI) for creating random, secure passwords.

Installation
Prerequisites:

Python 3.x
Steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/password-generator.git
Navigate to the project directory:

bash
Copy code
cd password-generator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Using the Command-Line
Generating a Random Password (Default Settings):

bash
Copy code
python src/main.py
This command generates a password with a default length of 10 characters, comprising a mix of uppercase letters, lowercase letters, digits, and special characters.

Specifying Password Length:

bash
Copy code
python src/main.py <length>
Replace <length> with the desired password length (minimum 1 character).

Specifying Character Types:

bash
Copy code
python src/main.py [OPTIONS]
Use the following options to customize the password composition:

-u or --uppercase: Include uppercase letters
-l or --lowercase: Include lowercase letters
-d or --digits: Include digits
-s or --special: Include special characters
You can combine these options to create passwords with specific requirements. For example:

bash
Copy code
python src/main.py -l 16 -u -d
This command generates a password of length 16 containing lowercase letters, uppercase letters, and digits.

Using the GUI
Run the GUI application by executing python gui.py in your terminal.
Enter the desired password length in the designated entry field.
Select the character types you want to include using the checkboxes (uppercase, lowercase, digits, special characters).
Click the "Generate" button to create a random password based on your selections.
The generated password will be displayed in the password entry field.
Features
Generate random passwords of specified length (minimum 1 character).
Customize password complexity by including or excluding uppercase letters, lowercase letters, digits, and special characters (both in GUI and command-line).
Simple and intuitive command-line interface.
User-friendly graphical user interface for easy interaction.
Requirements
Python 3.x
argparse library (included in the requirements.txt file)
tkinter library (included in the requirements.txt file)
Installation:

bash
Copy code
pip install -r requirements.txt
Project Structure
css
Copy code
password_generator/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── generator.py
│
├── tests/
│   ├── __init__.py
│   └── test_generator.py
│
├── gui.py  # GUI application file
├── README.md
└── requirements.txt
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Abahazem
