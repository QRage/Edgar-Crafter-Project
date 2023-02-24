import tkinter as tk


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x50")

        self.running = False

        self.btn = tk.Button(self.root, text="Start", command=self.toggle)
        self.btn.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.mainloop()

    def toggle(self):
        if self.running:
            self.running = False
            self.btn.config(text="Start")
        else:
            self.running = True
            self.btn.config(text="Stop")

        while self.running:
            self.root.update()

            print('running...')

    def close(self):
        self.running = False
        self.root.destroy()


if __name__ == '__main__':
    app = Interface()
