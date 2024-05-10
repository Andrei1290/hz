import tkinter as tk
from tkinter import scrolledtext
from g4f.client import Client

def send_message():
    user_input = entry.get()
    history.append(user_input)  # Добавляем сообщение в историю
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"Вы: {user_input}\n")  # Отображаем сообщения пользователя
    output_text.insert(tk.END, f"ИИ: {response.choices[0].message.content}\n\n")  # Отображаем ответ ИИ
    output_text.config(state=tk.DISABLED)
    entry.delete(0, tk.END)  # Очищаем поле ввода

# Создание клиента
client = Client()

# Создание окна
root = tk.Tk()
root.title("Искусственный интеллект")

# Определение размеров окна
window_width = 600
window_height = 400

# Определение размеров экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Расчет координат для размещения окна по центру экрана
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Установка размеров и положения окна
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Создание метки и поле для ввода
entry_label = tk.Label(root, text="Введите текст:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Создание кнопки
button = tk.Button(root, text="Окей", command=send_message)
button.pack()

# Создание текстового поля для вывода истории и ответов
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack()

# История сообщений
history = []

# Запуск цикла обработки событий
root.mainloop()
