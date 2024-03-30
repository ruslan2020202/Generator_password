from tkinter import Tk, PhotoImage, Label, Entry, N, END, RAISED

import random
from tkinter import ttk
from string import ascii_letters

root = Tk()
root.title("Password Generator")
root.geometry("400x185+550+250")
root.resizable(width=False, height=False)
icon = PhotoImage(file="iconn.png")
root.iconphoto(False, icon)
root.config(bg="#211342")

label_generate = Label(root, text="генератор паролей".upper(), bg="#331e69", fg="#7836bf",
                       font=("Times New Roman", 15, 'bold'),
                       height=2,
                       width=25,
                       relief=RAISED,
                       bd=5
                       )
label_generate.pack(pady=10, anchor=N)

# Добавим поле ввода и кнопку
entry = Entry(root, width=30, fg='#7836bf')
entry.pack(pady=10)


def generate_password():
    gen = [random.choice(ascii_letters) for _ in range(13)]
    passwd = ''.join(gen)
    entry.delete(0, END)  # Очищаем поле ввода
    entry.insert(0, passwd)  # Вставляем сгенерированный пароль


button_generate = ttk.Button(root, text="Сгенерировать", command=generate_password)
button_generate.pack(pady=15)

if __name__ == "__main__":
    root.mainloop()
