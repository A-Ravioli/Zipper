import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
import time

# For folder monitoring
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    messagebox.showerror("Module Not Found",
                         "Please install the 'watchdog' module:\npip install watchdog")
    exit(1)

class FolderMonitorHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_any_event(self, event):
        if self.app.auto_zip_enabled:
            self.app.rezip_folder()

class ZipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zipper")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.configure(bg='black')

        self.selected_folder = ''
        self.zip_file_path = ''
        self.auto_zip_enabled = False
        self.observer = None

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(
            self.root, text="Zipper", bg='black', fg='white', font=("Helvetica", 16)
        )
        self.title_label.pack(pady=10)

        # Label to display selected folder
        self.folder_label = tk.Label(
            self.root, text="No folder selected.", bg='black', fg='white'
        )
        self.folder_label.pack(pady=5)

        # Button to select folder
        self.select_button = tk.Button(
            self.root, text="Select Folder", command=self.select_folder, bg='white', fg='black'
        )
        self.select_button.pack(pady=5)

        # Button to select destination folder
        self.destination_button = tk.Button(
            self.root, text="Set Destination Folder", command=self.set_destination_folder, bg='white', fg='black'
        )
        self.destination_button.pack(pady=5)

        # Label to display destination folder
        self.destination_label = tk.Label(
            self.root, text="Default destination: Same as selected folder", bg='black', fg='white'
        )
        self.destination_label.pack(pady=5)

        # Button to zip the folder
        self.zip_button = tk.Button(
            self.root, text="Zip", command=self.zip_folder, state=tk.DISABLED, bg='white', fg='black'
        )
        self.zip_button.pack(pady=5)

        # Button to rezip the folder
        self.rezip_button = tk.Button(
            self.root, text="Rezip", command=self.rezip_folder, state=tk.DISABLED, bg='white', fg='black'
        )
        self.rezip_button.pack(pady=5)

        # Autozip Toggle
        self.autozip_var = tk.BooleanVar()
        self.autozip_check = tk.Checkbutton(
            self.root, text="Enable Autozip", variable=self.autozip_var,
            command=self.toggle_autozip, bg='black', fg='white', selectcolor='black'
        )
        self.autozip_check.pack(pady=5)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=f"Selected Folder: {self.selected_folder}")
            if hasattr(self, 'destination_folder') and self.destination_folder:
                destination = self.destination_folder
            else:
                destination = os.path.dirname(self.selected_folder)
            self.zip_file_path = os.path.join(
                destination,
                os.path.basename(self.selected_folder) + '.zip'
            )
            self.zip_button.config(state=tk.NORMAL)
            if os.path.exists(self.zip_file_path):
                self.rezip_button.config(state=tk.NORMAL)
            else:
                self.rezip_button.config(state=tk.DISABLED)
            # Restart observer if autozip is enabled
            if self.auto_zip_enabled:
                self.start_observer()
        else:
            self.folder_label.config(text="No folder selected.")
            self.zip_button.config(state=tk.DISABLED)
            self.rezip_button.config(state=tk.DISABLED)

    def set_destination_folder(self):
        destination = filedialog.askdirectory()
        if destination:
            self.destination_folder = destination
            self.destination_label.config(text=f"Destination Folder: {self.destination_folder}")
            if self.selected_folder:
                self.zip_file_path = os.path.join(
                    self.destination_folder,
                    os.path.basename(self.selected_folder) + '.zip'
                )
        else:
            self.destination_folder = os.path.dirname(self.selected_folder)
            self.destination_label.config(text="Default destination: Same as selected folder")

    def zip_folder(self):
        if not self.selected_folder:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        if os.path.exists(self.zip_file_path):
            overwrite = messagebox.askyesno(
                "Overwrite Confirmation",
                f"The zip file {os.path.basename(self.zip_file_path)} already exists. Overwrite?"
            )
            if not overwrite:
                return

        try:
            self.create_zip()
            messagebox.showinfo("Success", f"Folder zipped successfully at {self.zip_file_path}")
            self.rezip_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while zipping: {e}")

    def rezip_folder(self):
        if not self.selected_folder:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        if not os.path.exists(self.zip_file_path):
            messagebox.showwarning("Warning", "No existing zip file to overwrite.")
            return

        try:
            os.remove(self.zip_file_path)
            self.create_zip()
            # Only show message if not autozipping
            if not self.auto_zip_enabled:
                messagebox.showinfo("Success", f"Folder rezipped successfully at {self.zip_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while rezipping: {e}")

    def create_zip(self):
        with zipfile.ZipFile(self.zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.selected_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=self.selected_folder)
                    zipf.write(file_path, arcname)

    def toggle_autozip(self):
        self.auto_zip_enabled = self.autozip_var.get()
        if self.auto_zip_enabled:
            if not self.selected_folder:
                messagebox.showwarning("Warning", "Please select a folder first.")
                self.autozip_var.set(False)
                self.auto_zip_enabled = False
                return
            self.start_observer()
        else:
            self.stop_observer()

    def start_observer(self):
        self.stop_observer()  # Stop any existing observer
        event_handler = FolderMonitorHandler(self)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.selected_folder, recursive=True)
        self.observer.start()

    def stop_observer(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None

    def on_closing(self):
        self.stop_observer()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipperApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

#test