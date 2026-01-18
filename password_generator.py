import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password():
    length = length_scale.get()

    chars = ""
    if letters_var.get():
        chars += string.ascii_letters
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one character type")
        return

    password = ''.join(secrets.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    password = result_entry.get()
    if not password:
        messagebox.showwarning("Warning", "Password has not been generated yet")
        return
    window.clipboard_clear()
    window.clipboard_append(password)
    messagebox.showinfo("Done", "Password copied to clipboard")

window = tk.Tk()
window.title("Password Generator")
window.geometry("380x380")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

FONT = ("Segoe UI", 10)
FG = "#ffffff"
BG = "#1e1e1e"
BTN = "#3a7ff6"

tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Segoe UI", 14, "bold"),
    fg=FG,
    bg=BG
).pack(pady=10)

tk.Label(window, text="Password length:", fg=FG, bg=BG, font=FONT).pack()
length_scale = tk.Scale(
    window,
    from_=4,
    to=32,
    orient="horizontal",
    bg=BG,
    fg=FG,
    troughcolor="#444",
    highlightthickness=0
)
length_scale.set(12)
length_scale.pack()

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

def checkbox(text, var):
    return tk.Checkbutton(
        window,
        text=text,
        variable=var,
        fg=FG,
        bg=BG,
        selectcolor=BG,
        activebackground=BG,
        font=FONT
    )

checkbox("Letters (a-z, A-Z)", letters_var).pack(anchor="w", padx=60)
checkbox("Digits (0-9)", digits_var).pack(anchor="w", padx=60)
checkbox("Symbols (!@#$)", symbols_var).pack(anchor="w", padx=60)

tk.Button(
    window,
    text="GENERATE",
    command=generate_password,
    bg=BTN,
    fg="white",
    font=FONT,
    width=20
).pack(pady=15)

result_entry = tk.Entry(window, width=36, font=FONT, justify="center")
result_entry.pack(pady=5)

tk.Button(
    window,
    text="COPY",
    command=copy_password,
    bg="#2ecc71",
    fg="white",
    font=FONT,
    width=20
).pack(pady=10)

window.mainloop()
