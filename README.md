# Zipper - A Python GUI Tool for Zipping Folders

## Overview

**Zipper** is a user-friendly Python application with a graphical interface that simplifies the process of zipping folders. It allows you to select a folder, set a destination for the zip file, and provides options to manually zip or rezip the folder. Additionally, it features an **Autozip** functionality that monitors the selected folder for changes and automatically updates the zip file when modifications are detected.

## Features

- **Select Folder to Zip**: Easily browse and select the folder you want to compress.
- **Set Destination Folder**: Choose where the zip file will be saved.
- **Zip and Rezip**: Create a new zip file or update an existing one with the latest folder contents.
- **Autozip**: Enable automatic rezipping when changes are detected in the selected folder.
- **User-Friendly Interface**: A clean and intuitive GUI with customizable aesthetics.
- **Executable Version**: Create a standalone executable for easy distribution.
- **GitHub Release**: Share your application with others via GitHub releases.

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Selecting a Folder](#selecting-a-folder)
  - [Setting the Destination Folder](#setting-the-destination-folder)
  - [Zipping the Folder](#zipping-the-folder)
  - [Enabling Autozip](#enabling-autozip)
  - [Exiting the Application](#exiting-the-application)
- [Creating an Executable](#creating-an-executable)
  - [Install PyInstaller](#install-pyinstaller)
  - [Build the Executable](#build-the-executable)
  - [Testing the Executable](#testing-the-executable)
- [Making a GitHub Release](#making-a-github-release)
  - [Create a GitHub Repository](#create-a-github-repository)
  - [Add Your Project Files](#add-your-project-files)
  - [Create a Release](#create-a-release)
- [Customization](#customization)
  - [GUI Appearance](#gui-appearance)
  - [Autozip Configuration](#autozip-configuration)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure that Python is installed on your system.
- **pip**: Python package installer should be available.
- **PyInstaller**: For creating an executable version of the application.
- **Git**: For version control and pushing to GitHub.

### Setup

1. **Clone or Download the Repository**:

   ```bash
   git clone https://github.com/yourusername/zipper.git
   cd zipper
   ```

2. **Install Required Python Modules**:

   The application uses the `watchdog` module to monitor file system events for the Autozip feature. Install it using pip:

   ```bash
   pip install watchdog
   ```

## Usage

### Running the Application

Navigate to the directory containing the `zipper.py` script and run:

```bash
python zipper.py
```

### Selecting a Folder

1. Click the **"Select Folder"** button.
2. Browse and select the folder you wish to zip.
3. The selected folder path will be displayed on the application window.

### Setting the Destination Folder

1. Click the **"Set Destination Folder"** button.
2. Choose the directory where you want the zip file to be saved.
3. The destination path will be displayed. If not set, the zip file defaults to the same directory as the selected folder.

### Zipping the Folder

- Click the **"Zip"** button to create a zip file of the selected folder.
- If a zip file with the same name already exists at the destination, you'll be prompted to overwrite it.
- A success message will confirm the creation of the zip file.

### Enabling Autozip

- Check the **"Enable Autozip"** checkbox to start monitoring the folder.
- Any changes (additions, modifications, deletions) in the folder will automatically trigger the rezipping process.
- Ensure the application remains open for Autozip to function.

### Exiting the Application

- Click the close button (**"X"** on the window title bar).
- The application will stop monitoring and close gracefully.

## Creating an Executable

To distribute your application without requiring users to install Python and dependencies, you can create a standalone executable using PyInstaller.

### Install PyInstaller

Ensure PyInstaller is installed in your Python environment:

```bash
pip install pyinstaller
```

### Build the Executable

1. **Navigate to the Project Directory**:

   ```bash
   cd path_to_your_project_directory
   ```

2. **Run PyInstaller**:

   ```bash
   pyinstaller --onefile --windowed zipper.py
   ```

   **Explanation of the options**:

   - `--onefile`: Packages everything into a single executable file.
   - `--windowed`: Suppresses the console window (useful for GUI applications).

3. **Include an Icon (Optional)**:

   If you have an icon file (e.g., `icon.ico`), include it using:

   ```bash
   pyinstaller --onefile --windowed --icon=icon.ico zipper.py
   ```

4. **Handle Hidden Imports (If Necessary)**:

   If PyInstaller misses some modules (like `watchdog` submodules), include them using `--hidden-import`:

   ```bash
   pyinstaller --onefile --windowed --icon=icon.ico \
   --hidden-import=watchdog.observers.winapi_async \
   --hidden-import=watchdog.observers.winapi \
   zipper.py
   ```

### Testing the Executable

1. **Locate the Executable**:

   The executable will be located in the `dist` directory as `zipper.exe`.

2. **Run the Executable**:

   - Double-click `zipper.exe` to run the application.
   - Test all functionalities to ensure it works correctly.

## Making a GitHub Release

Share your application with others by creating a release on GitHub.

### Create a GitHub Repository

1. **Sign in to GitHub** and navigate to [GitHub](https://github.com/).
2. **Create a New Repository**:
   - Click the **"+"** icon and select **"New repository"**.
   - **Repository Name**: `zipper`.
   - **Description**: Provide a brief description.
   - **Public**: Make the repository public.
   - **Initialize Repository**: Optionally add a README and .gitignore (choose Python template).
   - Click **"Create repository"**.

### Add Your Project Files

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/zipper.git
   cd zipper
   ```

2. **Copy Your Files**:

   Copy your `zipper.py`, `README.md`, and any other necessary files into the repository directory.

3. **Add and Commit Files**:

   ```bash
   git add .
   git commit -m "Initial commit"
   ```

4. **Push to GitHub**:

   ```bash
   git push -u origin master
   ```

### Create a Release

1. **Go to the Releases Section**:

   - Navigate to your repository on GitHub.
   - Click on **"Releases"**.

2. **Draft a New Release**:

   - Click **"Draft a new release"**.

3. **Fill in Release Details**:

   - **Tag version**: e.g., `v1.0.0`.
   - **Release title**: e.g., `Zipper v1.0.0`.
   - **Description**: Add release notes and features.

4. **Upload Executable File**:

   - Under **"Attach binaries..."**, drag and drop your `zipper.exe` file.

5. **Publish Release**:

   - Click **"Publish release"**.

## Customization

### GUI Appearance

- **Background and Text Colors**: Modify the `bg` and `fg` parameters in the code to change colors.
- **Fonts and Styles**: Adjust font styles and sizes in the GUI elements.

### Autozip Configuration

- **Monitoring Specific Events**: Edit the `on_any_event` method in the `FolderMonitorHandler` class to filter specific events.
- **Debouncing**: Implement delays to prevent multiple rapid rezips during continuous file changes.

## Troubleshooting

- **Module Not Found Error**: Ensure the `watchdog` module is installed and you're using the correct Python environment.
- **Permission Issues**: Verify that you have read/write permissions for the selected and destination folders.
- **Executable Issues**:
  - If the executable doesn't run on other machines, include missing modules using `--hidden-import` in PyInstaller.
  - Test the executable on a machine without Python installed.

## Dependencies

- **Python Standard Libraries**:
  - `os`
  - `zipfile`
  - `tkinter`
  - `threading`
  - `time`
- **Third-Party Modules**:
  - `watchdog` (Install via `pip install watchdog`)
  - **PyInstaller** (For creating the executable)
    - Install via `pip install pyinstaller`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This application is intended for educational purposes. Customize and expand it according to your needs. If you encounter any issues or have suggestions for improvements, feel free to contribute or contact the maintainer.

---

**Download the Executable**: Users can download the latest executable version from the [Releases](https://github.com/yourusername/zipper/releases) page on GitHub.

**Contributions**: Contributions are welcome! Feel free to open issues or submit pull requests.
