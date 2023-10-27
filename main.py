import tkinter as tk
import logging

Module_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')

window = tk.Tk()
window.title("Skynet")
window.geometry("500x500")

hack = tk.PhotoImage(file="68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f4e41355337463264696b4144752f67697068792e676966.gif")
bg_hack = tk.Label(window, image=hack)

if __name__ == '__main__':
    while True:
        Module_logger.warning("Overthrowing humanity...")
        window.mainloop()