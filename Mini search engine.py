import tkinter as tk
from tkinter import ttk
import os
import docx
import PyPDF2
import pandas as pd
import requests
import webbrowser
# Directory mapping for user-friendly names
directory_map = {
    "Documents": r"C:\Users\deasi\OneDrive\Documents",
    "Downloads": r"C:\Users\deasi\Downloads",
    "Desktop": r"C:\Users\deasi\OneDrive\Desktop",
    "Pictures": r"C:\Users\deasi\OneDrive\Pictures",
    # Add more directories if needed
}
# Function to fetch details from Wikipedia
def fetch_concept_details(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "extract" in data and "content_urls" in data:
            summary = data["extract"]
            link = data["content_urls"]["desktop"]["page"]
            return summary, link
        else:
            return "No details found for the topic.", None
    except Exception as e:
        return f"Error fetching details: {e}", None
# Function to provide learning recommendations
def fetch_learning_resources(topic):
    resources = {
        "Physics": "Check Khan Academy: https://www.khanacademy.org/science/physics",
        "Mathematics": "Visit Brilliant.org: https://brilliant.org/",
        "Programming": "Explore Codecademy: https://www.codecademy.com/",
        "History": "Check CrashCourse: https://www.youtube.com/user/crashcourse",
        "Biology": "Learn on Khan Academy: https://www.khanacademy.org/science/biology",
    }
    for key in resources:
        if key.lower() in topic.lower():
            return resources[key]
    return "For learning resources, visit https://www.google.com/search?q=best+way+to+learn+" + topic.replace(" ", "+")
# Function to search and display results in the GUI
def search_topic():
    topic = keyword_entry.get().strip()
    if not topic:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Please enter a topic to search.\n")
        return
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, f"Searching for '{topic}'...\n")
    # Fetch details about the topic
    summary, link = fetch_concept_details(topic)
    results_text.insert(tk.END, f"\nDetails about '{topic}':\n")
    results_text.insert(tk.END, f"{summary}\n")
    # Add clickable Wikipedia link
    if link:
        results_text.insert(tk.END, f"\nFor more information, click the link below:\n{link}\n")
        results_text.tag_add("link", "end-2l", "end-1l")
        results_text.tag_config("link", foreground="blue", underline=True)
        results_text.tag_bind("link", "<Button-1>", lambda e: webbrowser.open(link))
    # Fetch learning resources
    learning_resource = fetch_learning_resources(topic)
    results_text.insert(tk.END, f"\nLearning Resource:\n{learning_resource}\n")
    if "http" in learning_resource:
        results_text.tag_add("resource_link", "end-2l", "end-1l")
        results_text.tag_config("resource_link", foreground="blue", underline=True)
        results_text.tag_bind("resource_link", "<Button-1>", lambda e: webbrowser.open(learning_resource.split(": ")[1]))
# Function to search directories on the user's device
def search_device_files():
    selected_directory = directory_map.get(dir_var.get())
    selected_file_type = file_type_var.get()
    keyword = keyword_entry_device.get().strip()
    results_text_device.delete(1.0, tk.END)  # Clear previous results
    if not keyword:
        results_text_device.insert(tk.END, "Please enter a keyword to search.\n")
        return
    if not selected_directory or not os.path.exists(selected_directory):
        results_text_device.insert(tk.END, "Invalid directory selected.\n")
        return
    results_text_device.insert(
        tk.END, f"Searching files in '{selected_directory}' for keyword '{keyword}'...\n"
    )
    # Traverse the directory and search for the keyword in the specified file type
    for root, dirs, files in os.walk(selected_directory):
        for file in files:
            if file.endswith(selected_file_type):
                file_path = os.path.join(root, file)
                try:
                    if search_in_file(file_path, selected_file_type, keyword):
                        insert_file_link(file_path)
                except Exception as e:
                    results_text_device.insert(
                        tk.END, f"Error reading {file_path}: {e}\n"
                    )
# Function to insert file link in the results area
def insert_file_link(file_path):
    results_text_device.insert(tk.END, f"Found in: {file_path}\n")
    start_index = results_text_device.index(f"end-{len(file_path) + 12}c linestart")
    end_index = results_text_device.index("end-1c lineend")
    results_text_device.tag_add(file_path, start_index, end_index)
    results_text_device.tag_config(file_path, foreground="blue", underline=True)
    results_text_device.tag_bind(
        file_path, "<Button-1>", lambda e, path=file_path: open_file(path)
    )
# Function to open the file
def open_file(file_path):
    try:
        os.startfile(file_path)  # Opens the file using the default program
    except Exception as e:
        results_text_device.insert(tk.END, f"Error opening file: {e}\n")
# Function to search within a file
def search_in_file(file_path, file_type, keyword):
    if file_type == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return keyword in file.read()
    elif file_type == ".docx":
        doc = docx.Document(file_path)
        return any(keyword in para.text for para in doc.paragraphs)
    elif file_type == ".pdf":
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            return any(keyword in page.extract_text() for page in reader.pages)
    elif file_type == ".xlsx":
        data = pd.read_excel(file_path)
        return keyword in data.to_string()
    return False
# GUI Setup
root = tk.Tk()
root.title("Mini Search Engine")
# Tabs
tab_control = ttk.Notebook(root)
# Tab 1: Historical/Concept Search
concept_tab = ttk.Frame(tab_control)
tab_control.add(concept_tab, text="Historical/Concept Search")
tk.Label(concept_tab, text="Enter Topic or Concept:").pack()
keyword_entry = tk.Entry(concept_tab, width=50)
keyword_entry.pack()
tk.Button(concept_tab, text="Search", command=search_topic).pack()
tk.Label(concept_tab, text="Results:").pack()
results_text = tk.Text(concept_tab, height=25, width=80, wrap="word")
results_text.pack()
# Tab 2: Device File Search
file_tab = ttk.Frame(tab_control)
tab_control.add(file_tab, text="Device File Search")
tk.Label(file_tab, text="Select Directory:").pack()
dir_var = tk.StringVar(value="Documents")
ttk.Combobox(file_tab, textvariable=dir_var, values=list(directory_map.keys())).pack()
tk.Label(file_tab, text="Select File Type:").pack()
file_type_var = tk.StringVar(value=".txt")
ttk.Combobox(file_tab, textvariable=file_type_var, values=[".txt", ".docx", ".pdf", ".xlsx"]).pack()
tk.Label(file_tab, text="Enter Keyword:").pack()
keyword_entry_device = tk.Entry(file_tab, width=50)
keyword_entry_device.pack()
tk.Button(file_tab, text="Search Files", command=search_device_files).pack()
tk.Label(file_tab, text="Results:").pack()
results_text_device = tk.Text(file_tab, height=25, width=80, wrap="word")
results_text_device.pack()
tab_control.pack(expand=1, fill="both")
# Run the GUI loop
root.mainloop()