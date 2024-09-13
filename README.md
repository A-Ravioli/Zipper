# Zipper - A Python GUI Tool for Zipping Folders

## Overview

**Zipper** is a user-friendly Python application with a graphical interface that simplifies the process of zipping folders. It allows you to select a folder, set a destination for the zip file, and provides options to manually zip or rezip the folder. Additionally, it features an **Autozip** functionality that monitors the selected folder for changes and automatically updates the zip file when modifications are detected.

## Features

- **Select Folder to Zip**: Easily browse and select the folder you want to compress.
- **Set Destination Folder**: Choose where the zip file will be saved.
- **Zip and Rezip**: Create a new zip file or update an existing one with the latest folder contents.
- **Autozip**: Enable automatic rezipping when changes are detected in the selected folder.
- **User-Friendly Interface**: A clean and intuitive GUI with customizable aesthetics.

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

## Customization

### GUI Appearance

- **Background and Text Colors**: The application uses a black background with white text and buttons for better contrast.
- **Fonts and Styles**: Modify the `font`, `bg`, and `fg` parameters in the code to change the appearance.

### Autozip Configuration

- **Monitoring Specific Events**: Adjust the `on_any_event` method in the `FolderMonitorHandler` class to filter specific file system events.
- **Debouncing**: Implement delays to prevent multiple rapid rezips during continuous file changes.

## Troubleshooting

- **Module Not Found Error**: Ensure the `watchdog` module is installed and you're using the correct Python environment.
- **Permission Issues**: Verify that you have read permissions for the selected folder and write permissions for the destination folder.
- **Application Not Responding**: Avoid monitoring very large folders with frequent changes, or optimize the code for better performance.

## Dependencies

- **Python Standard Libraries**:
  - `os`
  - `zipfile`
  - `tkinter`
  - `threading`
  - `time`
- **Third-Party Modules**:
  - `watchdog` (Install via `pip install watchdog`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: This application is intended for educational purposes. Customize and expand it according to your needs. If you encounter any issues or have suggestions for improvements, feel free to contribute or contact the maintainer.
