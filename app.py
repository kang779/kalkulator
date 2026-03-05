import tkinter as tk

class POSApp:
    def __init__(self, master):
        self.master = master
        master.title("POS System")

        self.label = tk.Label(master, text="Welcome to the POS System")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        print(f"Entry: {self.entry.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    pos_app = POSApp(root)
    root.mainloop()