import wikipedia
import tkinter as tk
from tkinter import scrolledtext

lang = 'en'  # Определяем переменную lang до создания графического интерфейса

def switch_language():
    global lang
    if lang == 'ru':
        lang = 'en'
        switch_button.config(text="Ru", bg="#3498db", fg="white")
    else:
        lang = 'ru'
        switch_button.config(text="Eng", bg="#3498db", fg="white")

def search_wikipedia():
    query = entry.get()
    try:
        wikipedia.set_lang(lang)
        result = wikipedia.page(query)
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, result.content)
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options)
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"Пожалуйста, уточните запрос. Возможные варианты: {options}")
    except wikipedia.exceptions.PageError:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, "Ничего не найдено по вашему запросу.")

# Создаем графический интерфейс
root = tk.Tk()
root.title("Поиск по Википедии (сделано Vafls'ом)")
root.configure(bg="#ecf0f1")

# Создаем элементы интерфейса
label = tk.Label(root, text="Введите запрос:", bg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, width=50, bg="#d5dbdb", fg="#2c3e50", bd=0)
entry.pack(pady=5)

switch_button = tk.Button(root, text="Ru", command=switch_language, bg="#3498db", fg="white", bd=0)
switch_button.pack(pady=5)

search_button = tk.Button(root, text="Поиск", command=search_wikipedia, bg="#2ecc71", fg="white", bd=0)
search_button.pack(pady=5)

text_area = scrolledtext.ScrolledText(root, width=70, height=20, bg="#bdc3c7", fg="#2c3e50", bd=0)
text_area.pack(padx=10, pady=10)

# Запускаем главный цикл событий
root.mainloop()
