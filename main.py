import tkinter as tk
from tkinter import *

def main():
    root = Tk()
    root.geometry("500x400")
    root.resizable(0,0)
    root.title("To Do List")
    root.configure(bg='#A7CAF3')
    Application(root)
    root.mainloop()

class Application:
    def __init__(self, master=None):
        self.selected_index = None

        self.project_font = ("Segoe UI", "10")
        self.title_container = Frame(master, background='#A7CAF3')
        self.title_container["pady"] = 10
        self.title_container.pack()

        self.text_container = Frame(master, background='#A7CAF3')
        self.text_container["padx"] = 20
        self.text_container["pady"] = 20
        self.text_container.pack()

        self.list_container = Frame(master, background='#A7CAF3')
        self.list_container["padx"] = 20
        self.list_container["pady"] = 20
        self.list_container.pack()

        self.error_container = Frame(master, background='#DBEBFF')
        self.error_container["padx"] = 20
        self.error_container.pack()

        self.titulo = Label(self.title_container,
                            text="To Do List",
                            background='#A7CAF3'
                            )
        self.titulo["font"] = ("Segoe UI", "14", "normal", "bold")
        self.titulo.pack()

        self.item_title = Entry(self.text_container)
        self.item_title["width"] = 40
        self.item_title["font"] = self.project_font
        self.item_title["bg"] = '#DBEBFF'
        self.item_title.pack(side=LEFT)

        self.add_item = Button(self.text_container)
        self.add_item["text"] = "Add"
        self.add_item["font"] = ("Calibri", "8")
        self.add_item["width"] = 5
        self.add_item["command"] = self.add_item_clicked
        self.add_item.pack(side=LEFT, padx=(20, 10))

        self.delete_item = Button(self.text_container)
        self.delete_item["text"] = "Del"
        self.delete_item["font"] = ("Calibri", "8")
        self.delete_item["width"] = 5
        self.delete_item["command"] = self.delete_item_clicked
        self.delete_item.pack(side=LEFT, padx=(0, 10))

        self.update_item = Button(self.text_container)
        self.update_item["text"] = "Upd"
        self.update_item["font"] = ("Calibri", "8")
        self.update_item["width"] = 5
        self.update_item["command"] = self.update_item_clicked
        self.update_item.pack(side=LEFT, padx=(0, 10))

        self.scrollbar = Scrollbar(self.list_container)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox_tasks = Listbox(self.list_container,
                                     height=6,
                                     selectmode=tk.SINGLE
                                     )
        self.listbox_tasks["width"] = 70
        self.listbox_tasks["height"] = 10
        self.listbox_tasks["bg"] = '#DBEBFF'
        self.listbox_tasks.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_tasks.yview)
        self.listbox_tasks.pack(expand=True, fill=tk.BOTH)
        self.task_list = ['Your tasks will appear here']

        for task in self.task_list:
            self.listbox_tasks.insert(END, task)

        self.error_handling = Label(self.error_container,
                                    text="Errors will show up here",
                                    fg="black",
                                    background='#DBEBFF',
                                    font=self.project_font
                                    )
        self.error_handling["width"] = 40
        self.error_handling["pady"] = 22
        self.error_handling.pack()

        def items_selected(event):
            try:
                self.selected_index = self.listbox_tasks.curselection()[0]
            except IndexError:
                pass
            self.item_title.delete(0, tk.END)
            self.item_title.insert(0, f'{self.task_list[self.selected_index]}')

        self.listbox_tasks.bind('<<ListboxSelect>>', items_selected)

    def add_item_clicked(self):
        if self.item_title.get() == "" or str.isspace(self.item_title.get()):
            self.error_handling["text"] = "Error: Item name cannot be empty"
            return
        self.clear_error_message()
        self.task_list.append(self.item_title.get())
        self.listbox_tasks.insert(END, self.item_title.get())
        self.item_title.delete(0, tk.END)

    def delete_item_clicked(self):
        self.clear_error_message()
        try:
            self.task_list.remove(self.task_list[self.selected_index])
            self.listbox_tasks.delete(self.selected_index)
            self.selected_index = None
            self.item_title.delete(0, tk.END)
        except TypeError:
            self.error_handling["text"] = "Error: No item was selected"

    def update_item_clicked(self):
        self.clear_error_message()
        try:
            new_item = self.item_title.get()
            self.task_list[self.selected_index] = new_item
            self.listbox_tasks.delete(self.selected_index)
            self.listbox_tasks.insert(self.selected_index, new_item)
            self.selected_index = None
        except TypeError:
            self.error_handling["text"] = "Error: No item was selected"

    def clear_error_message(self):
        self.error_handling["text"] = ""
if __name__ == "__main__":
    main()