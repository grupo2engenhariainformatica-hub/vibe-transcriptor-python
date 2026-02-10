import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern GUI Interface")
        self.geometry("400x300")
        self.configure(bg='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=(10, 10, 10, 10), style='TFrame')
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title_label = ttk.Label(frame, text="Welcome to Vibe Transcriptor", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, pady=10, sticky=tk.W)

        self.entry = ttk.Entry(frame, width=30)
        self.entry.grid(row=1, column=0, pady=10)

        submit_button = ttk.Button(frame, text="Submit", command=self.on_submit)
        submit_button.grid(row=2, column=0, pady=10)

    def on_submit(self):
        user_input = self.entry.get()
        print(f"User input: {user_input}")

if __name__ == '__main__':
    app = Application()
    app.mainloop()