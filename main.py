import tkinter as tk
import logging

Module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')

window = tk.Tk()
window.title("Skynet")
window.geometry("400x200")

hack = tk.PhotoImage(file="hack.gif", format="gif -index 0")
bg_hack = tk.Label(window, image=hack)
bg_hack.place(x=0, y=0, relwidth=1, relheight=1)

# hack_label = tk.Label(window, text="Hacking into the mainframe...", bg="black")
# hack_label.pack(pady=20)


if __name__ == '__main__':
    while True:
        Module_logger.warning("Overthrowing humanity...")
        window.mainloop()