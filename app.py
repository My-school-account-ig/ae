import tkinter as tk

root = tk.Tk()

root.title("storm chasing  gaem thinf :3")
root.configure(background="black")
root.minwidth(500, 500)
root.maxwidth(1920, 1080)

canvas = Canvas(root)
canvas.create_polygon(10, 10, 200, 50, 90, 150, 50, 80, 120, 55, outline="blue", width=2)

root.mainloop()
