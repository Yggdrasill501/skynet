import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        root.title("GIF Background Example")
        root.geometry("500x500")

        # Load the GIF image
        self.bg_image = tk.PhotoImage(file="68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f4e41355337463264696b4144752f67697068792e676966.gif")

        # Create a Canvas to display the image
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Add other widgets on top of the background
        self.label = tk.Label(root, text="This is on top of the background!", bg="white")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="A Button")
        self.button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()