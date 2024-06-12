import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import webbrowser

# Function to perform the Google search
def perform_search():
    url = url_entry.get()
    selected_dork = dork_var.get()
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    # Create the Google search query based on the selected dork
    search_query = ""
    if selected_dork == "Site-specific search":
        search_query = f"site:{url}"
    elif selected_dork == "PDF files":
        search_query = f"site:{url} filetype:pdf"
    elif selected_dork == "Admin pages":
        search_query = f"site:{url} inurl:admin"
    elif selected_dork == "Login pages":
        search_query = f"site:{url} inurl:login"
    elif selected_dork == "Directory listings":
        search_query = f"site:{url} intitle:\"index of /\""
    elif selected_dork == "Configuration files":
        search_query = f"site:{url} filetype:cnf"
    elif selected_dork == "SQL error messages":
        search_query = f"site:{url} \"error\" \"sql\" \"syntax\""
    elif selected_dork == "Word documents":
        search_query = f"site:{url} filetype:doc"
    elif selected_dork == "Excel spreadsheets":
        search_query = f"site:{url} filetype:xls"
    elif selected_dork == "PowerPoint presentations":
        search_query = f"site:{url} filetype:ppt"
    elif selected_dork == "Text files":
        search_query = f"site:{url} filetype:txt"
    elif selected_dork == "Log files":
        search_query = f"site:{url} filetype:log"
    elif selected_dork == "Backup files":
        search_query = f"site:{url} filetype:bak"
    elif selected_dork == "Old versions of files":
        search_query = f"site:{url} filetype:old"
    elif selected_dork == "ZIP archives":
        search_query = f"site:{url} filetype:zip"
    elif selected_dork == "RAR archives":
        search_query = f"site:{url} filetype:rar"
    elif selected_dork == "Database files":
        search_query = f"site:{url} filetype:db"
    elif selected_dork == "Database dumps":
        search_query = f"site:{url} filetype:sql"
    elif selected_dork == "Database files (DBF)":
        search_query = f"site:{url} filetype:dbf"
    elif selected_dork == "MS Access databases":
        search_query = f"site:{url} filetype:mdb"
    elif selected_dork == "Private keys":
        search_query = f"site:{url} filetype:key"
    elif selected_dork == "Email lists (XLS)":
        search_query = f"site:{url} filetype:xls inurl:email"
    elif selected_dork == "Email lists (CSV)":
        search_query = f"site:{url} filetype:csv inurl:email"
    elif selected_dork == "phpMyAdmin interfaces":
        search_query = f"site:{url} intitle:\"phpMyAdmin\""
    elif selected_dork == "FTP directories":
        search_query = f"site:{url} intitle:\"index of\" \"ftp\""
    elif selected_dork == "Sensitive directories (private)":
        search_query = f"site:{url} intitle:\"index of /private\""
    elif selected_dork == "Sensitive directories (backup)":
        search_query = f"site:{url} intitle:\"index of /backup\""
    elif selected_dork == "Sensitive documents (confidential)":
        search_query = f"site:{url} filetype:pdf \"confidential\""
    elif selected_dork == "Sensitive documents (proprietary)":
        search_query = f"site:{url} filetype:doc \"proprietary\""

    # Open the default web browser with the search query
    if search_query:
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

# Create the main application window
root = tk.Tk()
root.title("Google Dork Search Tool")

# URL entry
url_label = ttk.Label(root, text="Enter URL:")
url_label.grid(column=0, row=0, padx=10, pady=10)
url_entry = ttk.Entry(root, width=50)
url_entry.grid(column=1, row=0, padx=10, pady=10)

# Dropdown menu for selecting a Google dork
dork_var = tk.StringVar()
dorks = [
    "Site-specific search",
    "PDF files",
    "Admin pages",
    "Login pages",
    "Directory listings",
    "Configuration files",
    "SQL error messages",
    "Word documents",
    "Excel spreadsheets",
    "PowerPoint presentations",
    "Text files",
    "Log files",
    "Backup files",
    "Old versions of files",
    "ZIP archives",
    "RAR archives",
    "Database files",
    "Database dumps",
    "Database files (DBF)",
    "MS Access databases",
    "Private keys",
    "Email lists (XLS)",
    "Email lists (CSV)",
    "phpMyAdmin interfaces",
    "FTP directories",
    "Sensitive directories (private)",
    "Sensitive directories (backup)",
    "Sensitive documents (confidential)",
    "Sensitive documents (proprietary)"
]
dork_label = ttk.Label(root, text="Choose Google Dork:")
dork_label.grid(column=0, row=1, padx=10, pady=10)
dork_menu = ttk.Combobox(root, textvariable=dork_var, values=dorks, state="readonly")
dork_menu.grid(column=1, row=1, padx=10, pady=10)
dork_menu.current(0)

# Search button
search_button = ttk.Button(root, text="Search", command=perform_search)
search_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
