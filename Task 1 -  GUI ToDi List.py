import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def update_task():
    selected = listbox.curselection()
    if selected:
        task = entry.get()
        if task:
            listbox.delete(selected)
            listbox.insert(selected, task)
            entry.delete(0, tk.END)

def delete_all_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Todo List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Courier New", 12))
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT)

update_button = tk.Button(frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT)

delete_all_button = tk.Button(frame, text="Delete All Tasks", command=delete_all_tasks)
delete_all_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, font=("Courier New", 12), width=50, height=10)
listbox.pack(pady=20)

root.mainloop()