
<!-- Project Title -->

# 🌟 Password Generator 🌟

<!-- Project Description -->

This is a simple command-line application for generating random, secure passwords.

<!-- Installation Instructions -->

## Installation

1. Clone this repository:

   ```bash

   git clone https://github.com/yourusername/password-generator.git

   ```
2. Navigate to the project directory:

   ```bash

   cd password-generator

   ```

<!-- Usage Instructions -->

## Usage

**Generating a random password:**

```bash

pythonpassword_generator/main.py

```

This will generate a password with a default length of 10 characters and a mix of uppercase letters, lowercase letters, digits, and special characters.

**Specifying password length:**

```bash

pythonpassword_generator/main.py<length>

```

Replace `<length>` with the desired password length (minimum 1 character).

**Specifying character types:**

```bash

pythonpassword_generator/main.py [OPTIONS]

```

Use the following options to specify which character types to include in the password:

- `-u` or `--uppercase`: Include uppercase letters
- `-l` or `--lowercase`: Include lowercase letters
- `-d` or `--digits`: Include digits
- `-s` or `--special`: Include special characters

You can combine these options to create passwords with specific requirements.

<!-- Features -->

## Features

- Generate random passwords with specified length.
- Customize password composition with options for including uppercase letters, lowercase letters, digits, and special characters.
- Simple and intuitive command-line interface.

<!-- Requirements -->

## Requirements

- Python 3.x
- argparse

To install the required dependency, run:

```bash

pip install -r requirements.txt

```

<!-- Project Structure -->

## 🎨 Project Structure

```

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

├── README.md

└── requirements.txt

```

<!-- License -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<!-- Author -->

## Author

[Abahazem](https://github.com/dom557)
