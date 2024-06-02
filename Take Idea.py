import tkinter as tk
from random import randint, choice
from tkinter import messagebox

def addIdea():
    value = enterText.get()
    if value != "":
        with open("Idea.txt", "a+", encoding = "utf-8") as file:
            file.write(value + "\n")
        enterText.delete(0, "end")
    else:
        tk.messagebox.showinfo("Ошибка", ("Поле для ввода пустое")) 

def randomIdea():
    with open("Idea.txt", "r", encoding = "utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo("Идея", (choice(lines)))

def enterClick(this):
    addIdea()


window = tk.Tk()

#window = resizable(width = False, height = False)

window.title("Генератор идей")

window.geometry('720x360')
window["bg"] = "black"

idea = tk.Label(window, text = "Добавить идею", font = ("Roboto Bold", 15), fg = "white", bg = "black")
idea.place(x = 290, y = 25)

enterText = tk.Entry(fg = "blue", width = 47)
enterText.place(x = 220, y = 65)

button = tk.Button(window, text = "Добавить", command = addIdea, width = "40", height = "2", fg = "blue", bg = "white")
button.place(x = 220, y = 95)

window.bind("<Return>", enterClick)

giveIdea = tk.Label(window, text = "Сгенерировать идею", font = ("Roboto Bold", 15), fg = "white", bg = "black")
giveIdea.place(x = 266, y = 185)

button = tk.Button(window, text = "Получить идею", command = randomIdea, width = "40", height = "2", fg = "blue", bg = "white")
button.place(x = 220, y = 220)

window.mainloop()