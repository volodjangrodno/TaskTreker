import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_listBox.curselection()
    if selected_task_index:
        selected_task_text = task_listBox.get(selected_task_index)  # Получаем текст выбранной задачи
        task_listBox.delete(selected_task_index)
        deleted_task_listBox.insert(tk.END, selected_task_text)  # Вставляем текст задачи в другой список

def mark_task():
    selected_task_index = task_listBox.curselection()
    if selected_task_index:
        selected_task_text = task_listBox.get(selected_task_index)  # Получаем текст задачи
        task_listBox.delete(selected_task_index)
        closed_task_listBox.insert(tk.END, selected_task_text)  # Вставляем текст задачи в другой список

root = tk.Tk()
root.title(f"Task list")
root.configure(background="bisque3")

text1 = tk.Label(root, text="Введите вашу задачу", bg="bisque3")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="alice blue")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, width=30, text="Добавить задачу", bg="gold", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = tk.Button(root, width=30, text="Удалить задачу", fg="alice blue", bg="DarkRed", command=delete_task)
delete_task_button.pack(pady=5)

mark_task_button = tk.Button(root, width=30, text="Отметить задачу как выполненую", fg="alice blue", bg="dark green", command=mark_task)
mark_task_button.pack(pady=5)

text2 = tk.Label(root, text="Список предстоящих задач:", bg="bisque3")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="gold")
task_listBox.pack()

text3 = tk.Label(root, text="Список выполненных задач:", bg="bisque3")
text3.pack(pady=5)

closed_task_listBox = tk.Listbox(root, height=10, width=50, bg="dark green", fg="alice blue")
closed_task_listBox.pack()

text4 = tk.Label(root, text="Список удалённых задач:", bg="bisque3")
text4.pack(pady=5)

deleted_task_listBox = tk.Listbox(root, height=10, width=50, fg="alice blue", bg="DarkRed")
deleted_task_listBox.pack()

root.mainloop()
