import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        self.textarea = tk.Text(master, font=("Helvetica", 12))
        self.textarea.pack(fill=tk.BOTH, expand=True)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        master.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                text = f.read()
                self.textarea.delete("1.0", tk.END)
                self.textarea.insert(tk.END, text)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as f:
                text = self.textarea.get("1.0", tk.END)
                f.write(text)

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
