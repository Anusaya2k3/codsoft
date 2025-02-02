# Simple To-Do List App
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=75,bg="sky blue")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=70)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=50, command=add_task,bg="green")
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=50,bg="red",fg="black",command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=50, command=load_tasks,bg="pink")
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=50, command=save_tasks,bg="blue")
button_save_tasks.pack()

root.mainloop()
