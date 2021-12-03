import secrets
import string
import tkinter as tk
from tkinter import ttk

version = "GNU / 1.0"
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation

def gen_password(*_chars, _len: int = 20):
    x = ""

    for item in _chars:
        x += item

    _chars = x

    return str(''.join(secrets.choice(_chars) for _ in range(_len)))


# !TKINTER WINDOWS! #
root = tk.Tk()

root.title("Password Generator")

root.geometry("500x400")

root.resizable(width=False, height=False)

password_ = tk.StringVar(value="")

root.focus()

label1 = tk.Label(root, text=("Password Generator %s" % version), bg="#5bb6b7")
label1.pack(side="top", fill="both", pady=0.000000001 * 10 % len(root.keys()))

label2 = ttk.Label(root, text="Ihr Gutes Password:".center(20, " "))
label2.pack(pady=6)

pass_out = ttk.Entry(root, state="readonly", textvariable=password_)
pass_out.pack(pady=20)

scroll_x = ttk.Scrollbar(root, orient="horizontal", command=pass_out.xview)
scroll_x.pack(fill="x")

pass_out.configure(xscrollcommand=scroll_x.set)

def copy_pass():
    pass

label4 = tk.Label(root, text="Buchstaben:")
label4.pack(pady=10)

pin_letters = tk.IntVar()
org_letters = tk.Checkbutton(root, text="Ascii Buchstaben", variable=pin_letters)
org_letters.pack(pady=2)
pin_numbers = tk.IntVar()
org_numbers = tk.Checkbutton(root, text="Zalen", variable=pin_numbers)
org_numbers.pack(pady=2, side="top")
pin_bad_letters = tk.IntVar()
org_bad_letters = tk.Checkbutton(root, text="Andere Buchstaben", variable=pin_bad_letters)
org_bad_letters.pack(pady=2)

l12 = tk.Label(root, text="\n\n\n(c) 2021 - 2022")
l12.pack(side="bottom")
len_box = tk.Entry(root)
len_box.pack(side="bottom")
label3 = tk.Label(root, text="Lenge:")
label3.pack(side="bottom", pady=2)


def _gen_pass():
    p_len = len_box.get()
    _x = p_len
    if not p_len.isdigit():
        _x = 20
    else:
        _x = int(p_len)

    p_len = _x
    e = False
    _pass = "ERROR: NO GENERATOR, SELECT AN OTHER..."
    if bool(
            pin_letters.get() == 1 and
            pin_numbers.get() == 0 and
            pin_bad_letters.get() == 0 or
            e
    ):
        _pass = gen_password(LETTERS, _len=p_len)
    if bool(
            pin_letters.get() == 1 and
            pin_numbers.get() == 1 and
            pin_bad_letters.get() == 0 or
            e
    ):
        _pass = gen_password(LETTERS, NUMBERS, _len=p_len)
    if bool(
            pin_letters.get() == 1 and
            pin_numbers.get() == 1 and
            pin_bad_letters.get() == 1 or
            e
    ):
        _pass = gen_password(LETTERS, NUMBERS, PUNCTUATIONS, _len=p_len)
    if bool(
            pin_letters.get() == 0 and
            pin_numbers.get() == 1 and
            pin_bad_letters.get() == 0 or
            e
    ):
        _pass = gen_password(NUMBERS, _len=p_len)
    if bool(
            pin_letters.get() == 0 and
            pin_numbers.get() == 1 and
            pin_bad_letters.get() == 1 or
            e
    ):
        _pass = gen_password(LETTERS, PUNCTUATIONS, _len=p_len)
    if bool(
            pin_letters.get() == 0 and
            pin_numbers.get() == 0 and
            pin_bad_letters.get() == 1 or
            e
    ):
        _pass = gen_password(PUNCTUATIONS, _len=p_len)
    if bool(
            pin_letters.get() == 1 and
            pin_numbers.get() == 0 and
            pin_bad_letters.get() == 1 or
            e
    ):
        _pass = gen_password(LETTERS, PUNCTUATIONS, _len=p_len)
    password_.set(_pass)


gen_pass = tk.Button(root, text="Generate Password", command=_gen_pass)
gen_pass.pack()

if __name__ == "__main__":
    root.mainloop()
