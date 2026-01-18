# Password Generator (Python, Tkinter)

A simple and secure desktop password generator written in **Python** using **Tkinter**.

## Features

- Adjustable password length (slider)
- Options to include:
  - Letters (a–z, A–Z)
  - Digits (0–9)
  - Symbols (!@#$ etc.)
- Cryptographically secure password generation (`secrets`)
- Copy password to clipboard
- Clean dark-themed GUI
- No console window (when built as `.exe`)

## Requirements

- Python **3.8+**
- Tkinter (included with standard Python installation)

## How to Run

1. Clone or download this repository
2. Make sure Python is installed:
   ```bash
   python --version
   ```
3. Run the program:
   ```bash
   python password_generator.py
   ```

## How to Build `.exe` (Windows)

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to the project folder:
   ```bash
   cd path_to_project
   ```

3. Build executable:
   ```bash
   pyinstaller --onefile --windowed password_generator.py
   ```

4. The executable will appear in:
   ```
   dist/password_generator.exe
   ```

## Project Structure

```
password-generator/
│
├── password_generator.py
├── README.md
└── dist/
    └── password_generator.exe
```

## Security Notes

- Passwords are generated using the `secrets` module
- No passwords are stored or logged
- Clipboard is used only when pressing the **COPY** button

## License

This project is free to use for learning and personal projects.
