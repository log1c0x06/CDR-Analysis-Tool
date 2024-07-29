# -*- coding: utf-8 -*-
"""
CDR Analysis Tool

Copyright (c) 2024 log1c. All rights reserved.

This script is part of the CDR Analysis Tool. Unauthorized use,
distribution, or modification of this script is prohibited.

"""

import pandas as pd
import json
import xml.etree.ElementTree as ET
from tkinter import Tk, filedialog, Button, Label, Frame, RIGHT, Y, END
from tkinter import messagebox
from tkinter import font as tkfont
from tkinter.ttk import Treeview, Scrollbar

# Load CDR data from CSV, JSON, TXT, or XML file
def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as f:
                data = pd.DataFrame(json.load(f))
        elif file_path.endswith('.xml'):
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = pd.DataFrame([elem.attrib for elem in root])
        elif file_path.endswith('.txt'):
            data = pd.read_csv(file_path, delimiter='\t')
        else:
            raise ValueError("Unsupported file format. Please use CSV, TXT, XML, or JSON.")
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        messagebox.showerror("Error", "No data in file")
        return None
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error decoding JSON file")
        return None
    except ET.ParseError:
        messagebox.showerror("Error", "Error parsing XML file")
        return None

# Analyze data and return results as list of lists for display
def analyze_data(data):
    results = []
    if data is not None:
        # Create a list for headers
        headers = ["Call Start Time", "Call End Time", "Duration", "Caller Number", "Receiver Number", "Call Type", "Country", "Tower ID", "ISP Name", "Cost", "Call Status"]
        results.append(headers)

        for index, row in data.iterrows():
            results.append([
                row.get('Call Start Time', 'N/A'),
                row.get('Call End Time', 'N/A'),
                row.get('Duration', 'N/A'),
                row.get('Caller Number', 'N/A'),
                row.get('Receiver Number', 'N/A'),
                row.get('Call Type', 'N/A'),
                row.get('Country', 'N/A'),
                row.get('Tower ID', 'N/A'),
                row.get('ISP Name', 'N/A'),
                row.get('Cost', 'N/A'),
                row.get('Call Status', 'N/A')
            ])
    else:
        results.append(["No data to analyze"])
    return results

# Open file dialog to select CDR file
def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select CDR File",
        filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"), ("XML files", "*.xml"), ("JSON files", "*.json")]
    )
    return file_path

# Save results to a text file
def save_results():
    results = "\n".join(["\t".join(map(str, row)) for row in tree_data])
    if results:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Results"
        )
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write(results)
                messagebox.showinfo("Success", f"Results saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")
    else:
        messagebox.showwarning("No Results", "There are no results to save")

# Display analysis results in the treeview
def display_results(results):
    for item in tree.get_children():
        tree.delete(item)

    for row in results:
        tree.insert("", "end", values=row)

# Open file and perform analysis
def open_file():
    file_path = open_file_dialog()
    if file_path:
        data = load_data(file_path)
        global tree_data
        tree_data = analyze_data(data)
        display_results(tree_data)

# Main function
def main():
    global tree, tree_data

    root = Tk()
    root.title("CDR Common Analysis")
    root.geometry("1000x600")  # Adjusted size for better layout

    # Create a frame for the layout
    frame = Frame(root, bg="#d4edda")  # Light green background for the frame
    frame.pack(padx=15, pady=15, fill='both', expand=True)

    # Title Label
    title_font = tkfont.Font(family="Arial", size=20, weight="bold")
    title_label = Label(frame, text="CDR Analysis Tool", font=title_font, bg="#d4edda", fg="#155724")
    title_label.pack(pady=10)

    # Treeview with Scrollbars
    tree_frame = Frame(frame)
    tree_frame.pack(fill='both', expand=True)

    scroll_y = Scrollbar(tree_frame, orient='vertical')
    scroll_y.pack(side=RIGHT, fill=Y)

    tree = Treeview(tree_frame, yscrollcommand=scroll_y.set, columns=("Call Start Time", "Call End Time", "Duration", "Caller Number", "Receiver Number", "Call Type", "Country", "Tower ID", "ISP Name", "Cost", "Call Status"), show='headings')
    tree.pack(fill='both', expand=True)

    scroll_y.config(command=tree.yview)

    # Define columns and headings
    columns = ["Call Start Time", "Call End Time", "Duration", "Caller Number", "Receiver Number", "Call Type", "Country", "Tower ID", "ISP Name", "Cost", "Call Status"]
    tree['columns'] = columns
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor='center')

    # Set background and text color
    tree.tag_configure('header', background='#d4edda', font=("Arial", 14, "bold"))
    tree.tag_configure('data', background='#ffffff', foreground='#000000')  # Black text on white background

    # Buttons Frame
    button_frame = Frame(frame, bg="#d4edda")
    button_frame.pack(side='bottom', fill='x', pady=10)

    # Open File Button
    open_button = Button(button_frame, text="Open CDR File", command=open_file, font=("Arial", 10), bg="#28a745", fg="#ffffff", relief="raised")
    open_button.pack(side='left', padx=5)

    # Save Results Button
    save_button = Button(button_frame, text="Save Results", command=save_results, font=("Arial", 10), bg="#007bff", fg="#ffffff", relief="raised")
    save_button.pack(side='left', padx=5)

    # Clear Results Button
    clear_button = Button(button_frame, text="Clear Results", command=lambda: tree.delete(*tree.get_children()), font=("Arial", 10), bg="#dc3545", fg="#ffffff", relief="raised")
    clear_button.pack(side='left', padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
