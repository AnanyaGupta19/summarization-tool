import tkinter as tk
from tkinter import filedialog, messagebox
from app.summarizer import extractive_summary

def summarize_text():
    text = text_input.get("1.0", tk.END)
    summary = extractive_summary(text)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, summary)

def load_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, text)

app = tk.Tk()
app.title("Text Summarizer")

tk.Button(app, text="Upload Text File", command=load_file).pack()
text_input = tk.Text(app, height=10)
text_input.pack()

tk.Button(app, text="Summarize", command=summarize_text).pack()
text_output = tk.Text(app, height=10)
text_output.pack()

app.mainloop()
