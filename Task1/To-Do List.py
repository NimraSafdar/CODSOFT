import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = []
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_name, status = line.strip().split('|')
                    tasks.append({"name": task_name, "done": status == "Done"})
        except FileNotFoundError:
            pass
        return tasks

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                status = "Done" if task['done'] else "Pending"
                file.write(f"{task['name']}|{status}\n")

    # GUI Methods
    def run_gui(self):
        def display_tasks():
            listbox.delete(0, tk.END)
            for task in self.tasks:
                status = "[Done]" if task['done'] else "[Pending]"
                listbox.insert(tk.END, f"{task['name']} {status}")

        def add_task():
            task_name = simpledialog.askstring("Input", "Enter task name:")
            if task_name:
                self.tasks.append({"name": task_name, "done": False})
                self.save_tasks()
                display_tasks()

        def mark_as_done():
            try:
                index = listbox.curselection()[0]
                self.tasks[index]['done'] = True
                self.save_tasks()
                display_tasks()
            except IndexError:
                messagebox.showerror("Error", "Please select a task.")

        def remove_task():
            try:
                index = listbox.curselection()[0]
                del self.tasks[index]
                self.save_tasks()
                display_tasks()
            except IndexError:
                messagebox.showerror("Error", "Please select a task.")

        root = tk.Tk()
        root.title("To-Do List App (GUI)")

        listbox = tk.Listbox(root, width=50, height=20)
        listbox.pack(pady=20)

        frame = tk.Frame(root)
        frame.pack(pady=20)

        btn_add = tk.Button(frame, text="Add Task", command=add_task)
        btn_add.grid(row=0, column=0, padx=20)

        btn_done = tk.Button(frame, text="Mark as Done", command=mark_as_done)
        btn_done.grid(row=0, column=1, padx=20)

        btn_remove = tk.Button(frame, text="Remove Task", command=remove_task)
        btn_remove.grid(row=0, column=2, padx=20)

        display_tasks()

        root.mainloop()

    # CLI Methods
    def display_menu(self):
        print("\nTo-Do List App")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("Enter your choice: ")
        return choice

    def display_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        print("\nTasks:")
        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task['done'] else "Pending"
            print(f"{idx}. {task['name']} - {status}")

    def add_task(self):
        task_name = input("\nEnter task name: ")
        self.tasks.append({"name": task_name, "done": False})
        self.save_tasks()

    def remove_task(self):
        self.display_tasks()
        task_num = int(input("\nEnter the task number to remove: "))
        if task_num <= len(self.tasks):
            del self.tasks[task_num - 1]
            self.save_tasks()
            print("Task removed!")
        else:
            print("Invalid task number.")

    def mark_task_as_done(self):
        self.display_tasks()
        task_num = int(input("\nEnter the task number to mark as done: "))
        if task_num <= len(self.tasks):
            self.tasks[task_num - 1]['done'] = True
            self.save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    def run_cli(self):
        while True:
            choice = self.display_menu()

            if choice == "1":
                self.display_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.mark_task_as_done()
            elif choice == "5":
                print("Exiting the app!")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

    def run(self):
        choice = input("Choose the version (GUI/CLI): ").strip().lower()
        if choice == "gui":
            self.run_gui()
        elif choice == "cli":
            self.run_cli()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    app = ToDoList()
    app.run()
