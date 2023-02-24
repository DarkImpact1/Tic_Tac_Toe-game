import tkinter as tk
import colorsys

root = tk.Tk()

# create a label widget with initial text and foreground color
my_label = tk.Label(root, text="Glowing Label", fg="blue")
my_label.pack()

# function to change the label foreground color smoothly
def smooth_glow():
    hue = (tk.Misc.winfo_id(root) % 360) / 360  # use window ID to get a unique hue
    saturation = 1
    value = 1
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, saturation, value)]
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    my_label.config(fg=hex_color)
    my_label.after(50, smooth_glow)  # call this function again after 50 ms

# start the smooth glowing effect
smooth_glow()

root.mainloop()
