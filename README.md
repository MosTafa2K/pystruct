# pystruct
# Project Structure Generator Documentation

This Python project is a **Project Structure Generator** that allows developers to create a project structure based on a predefined YAML file. The program reads a `structure.yaml` file that defines the desired folder and file hierarchy, and it generates the entire structure in a specified directory.

---

## Features

1. **YAML-based Configuration**: Define project structures in a simple and readable YAML file.
2. **Automatic File and Folder Creation**: Automatically creates files and directories as specified in the YAML configuration.
3. **Customizable Base Path**: Choose where to generate the project structure.
4. **Error Handling**: Handles invalid or missing YAML files gracefully.

---

## How It Works

1. **Define the Structure**: Create a `structure.yaml` file to specify the desired project structure.
2. **Run the Script**: Execute the Python script to generate the project structure in a directory of your choice.
3. **Check Output**: The program creates all folders and files with optional default content.

---

## Prerequisites

- Python 3.9 or higher
- `PyYAML` library

Install `PyYAML` using pip:

```bash
pip install pyyaml
```

---

## File: `structure.yaml`

The `structure.yaml` file defines the project structure. Here's an example:

```yaml
app:
  api:
    v1:
      endpoints:
        auth.py: "# Authentication endpoints"
        users.py: "# User endpoints"
      __init__.py: "# API v1 init"
  core:
    config.py: "# Configuration file"
    security.py: "# Security functions"
  db:
    base.py: "# Base DB setup"
    session.py: "# Session setup"
    models:
      user.py: "# User model"
  schemas:
    user.py: "# User schema"
  main.py: "# Main application entry point"
tests:
  __init__.py: "# Tests init"
  test_users.py: "# Tests for user endpoints"
  test_auth.py: "# Tests for auth endpoints"
requirements.txt: "# List your dependencies here"
README.md: "# Project documentation"
```

---

## How to Use

1. **Prepare the YAML File**: Ensure a `structure.yaml` file exists in the project directory.
2. **Run the Script**:
   - Open a terminal and navigate to the directory containing the script.
   - Run the script:
     ```bash
     python create_project.py
     ```
3. **Enter the Base Path**:
   - The program will prompt you to enter a base path where the project structure will be created. Press `Enter` to use the current directory or specify a custom path.

Example:
```plaintext
Enter the base path for the project structure: /path/to/project
```

4. **Check Output**:
   - Once the script finishes, navigate to the specified base path to see the generated structure.

---

## Error Handling

### Missing `structure.yaml`
If the file `structure.yaml` is missing, the script will display the following message:
```plaintext
File 'structure.yaml' not found. Please create the file and try again.
```

### Invalid YAML File
If the YAML file contains errors, the program will print:
```plaintext
Error in YAML file: <specific error message>
```

### Empty YAML File
If the YAML file is empty, the program will print:
```plaintext
Error in YAML file: YAML structure is empty.
```

---

## Example Run

1. **Input**: Create the `structure.yaml` file as shown above.
2. **Run the Script**:
   ```bash
   python create_project.py
   ```
3. **Input Base Path**:
   ```plaintext
   Enter the base path for the project structure: .
   ```
4. **Output**: The project structure will be created in the current directory.

---

## Example Output

For the YAML structure provided above, the generated project structure will look like this:

```plaintext
app/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   └── users.py
│   │   └── __init__.py
├── core/
│   ├── config.py
│   └── security.py
├── db/
│   ├── base.py
│   ├── session.py
│   └── models/
│       └── user.py
├── schemas/
│   └── user.py
├── main.py
tests/
├── __init__.py
├── test_users.py
└── test_auth.py
requirements.txt
README.md
```

---

## Customization

You can modify `structure.yaml` to define a different structure. For example:

```yaml
src:
  components:
    Header.js: "// React header component"
    Footer.js: "// React footer component"
  App.js: "// Main React App"
  index.js: "// Entry point"
public:
  index.html: "<!-- HTML entry point -->"
README.md: "# React Project"
```

Running the script with this YAML will create the appropriate structure.

---

## FAQ

### Q: Can I use this script for any programming language?
A: Yes, the script is not language-specific. You can define any structure in the YAML file.

### Q: Can I include empty folders?
A: Yes, just define a folder in YAML with an empty dictionary `{}`.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as needed.

---

If you have any questions or encounter issues, feel free to reach out! 😊
