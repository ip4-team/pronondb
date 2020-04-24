import tkinter as tk

from tkinter import ttk
from functools import partial
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import ScrolledText

from datetime import datetime


class Menu():
    def __init__(self, parent, controller, table_name, fields):
        self.controller = controller
        self.parent = parent

        self.table_name = table_name
        self.modal_isopen = False

        container = tk.Frame(parent)
        container.pack(side="top", fill="both", expand=True)

        self.form_frame = tk.Frame(parent)
        self.form_frame.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.buttonframe = tk.Frame(parent)
        self.buttonframe.place(in_=container, x=0, y=0,
                               relwidth=1, relheight=1)

        self.form = Form(self.form_frame, fields)
        self.entries = self.form.make_form()

        self.register = Register(self, parent, controller, self.entries)
        self.update = Update(self, parent, controller, self.entries)
        self.delete = Delete(self, parent, controller, self.entries)

        self.initUI()

    def initUI(self):
        self.buttonframe.lift()
        register_button = ttk.Button(self.buttonframe, text="Cadastrar " + self.table_name,
                                     command=partial(self.raise_slave, self.register), width=30)
        register_button.pack(pady=5)

        update_button = ttk.Button(self.buttonframe, text="Atualizar " + self.table_name,
                                   command=partial(self.select_id, self.update), width=30)
        update_button.pack(pady=5)

        remove_button = ttk.Button(self.buttonframe, text="Remover " + self.table_name,
                                   command=partial(self.select_id, self.delete), width=30)
        remove_button.pack(pady=5)

    def select_id(self, slave):
        self.ids = self.get_rows(self.table_name)

        x = self.parent.winfo_x()
        y = self.parent.winfo_y()

        self.modal = tk.Toplevel(self.parent)
        self.modal.minsize(300, 100)
        self.modal.geometry('+%d+%d' % (x + 200, y + 200))
        self.modal.grab_set()

        modal_label = ttk.Label(
            self.modal, text="Selecione o " + self.table_name)
        modal_label.pack(side=tk.TOP, pady=10)

        self.modal_entry = ttk.Combobox(
            self.modal, state='readonly', values=self.ids)
        self.modal_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.X, padx=15,
                              pady=10)

        exit_button = ttk.Button(
            self.modal, text="Fechar", command=self.destroy_modal)
        exit_button.pack(side=tk.LEFT, padx=5, pady=15)

        send_button = ttk.Button(
            self.modal, text="Enviar", command=partial(self.raise_slave, slave))
        send_button.pack(side=tk.RIGHT, padx=5, pady=15)

        self.modal_isopen = True

    def raise_slave(self, slave):
        if self.modal_isopen:
            slave.set_id(self.modal_entry.get())
            self.modal.destroy()
            self.modal_isopen = False

        self.form.back_button.config(command=slave.exit)
        self.form.query_button.config(command=slave.callback)
        self.form_frame.lift()

    def destroy_modal(self):
        self.modal.destroy()
        self.modal_isopen = False

    def raise_parent(self):
        self.buttonframe.lift()

    def get_rows(self, table):
        table_values = self.controller.send_query('SELECT',
                                                  table,
                                                  '*')
        ids = [x['id'+table] for x in table_values[2]]

        return ids


class Form():
    def __init__(self, parent, fields, disable=False):
        self.parent = parent
        self.fields = fields
        self.disable = disable
        canvas = tk.Canvas(parent, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)

        self.frame = ttk.Frame(canvas)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.bind("<Configure>",
                        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.fram_n_canvas_iid = canvas.create_window((0, 0), window=self.frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill='both', expand=True)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        canvas.bind("<Configure>", self.canvas_configure)

        self.back_button = ttk.Button(self.frame, text="Voltar")
        self.query_button = ttk.Button(self.frame, text="Salvar")

    def canvas_configure(self, event):
        canvas = event.widget
        canvas.itemconfigure(canvas.fram_n_canvas_iid, width=canvas.winfo_width())

    def make_form(self):
        style = ttk.Style()
        if self.disable:
            style.map('TEntry',
                      foreground=[('disabled', 'black')])
            style.map('TRadiobutton',
                      foreground=[('disabled', 'black')])

            entry_state = 'disabled'
            combobox_state = 'disabled'
        else:
            entry_state = 'normal'
            combobox_state = 'readonly'

        entries = []
        for key in self.fields:
            label_text = self.fields[key]['label']
            entry = self.fields[key]['entry']

            row = tk.Frame(self.frame)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            lab = ttk.Label(row, width=35, text=label_text, anchor='w')
            lab.pack(side=tk.LEFT, padx=15)

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, text=v[0], value=v[1], variable=ent_var,
                                state=entry_state)
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state=combobox_state, 
                            values=self.fields[key]['value'], textvariable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy',
                            textvariable=ent_var, state=entry_state)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Text box
            elif entry == ScrolledText:
                ent_var = entry(row, wrap=tk.WORD, width=20, height=10)
                ent_var.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, textvariable=ent_var, state=entry_state)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        # Send Query button
        self.back_button.pack(side=tk.LEFT, padx=5, pady=50)
        self.query_button.pack(side=tk.RIGHT, padx=5, pady=50)
        return entries


class Register():
    def __init__(self, menu, parent, controller, entries):
        self.controller = controller
        self.parent = parent
        self.menu = menu

        self.entries = entries

    def callback(self):
        query_values = []
        column_names = []
        for entry in self.entries:
            key = entry[0]
            entry_type = entry[2]
            if entry_type == ScrolledText:
                text = entry[1].get('1.0', tk.END)
            else:
                text = entry[1].get()

            if text == '':
                text = None

            if entry_type == DateEntry and text != None:
                date = text.split('/')
                text = date[2] + '/' + date[1] + '/' + date[0]

            column_names.append(key)
            query_values.append(text)

        result = self.controller.send_query('INSERT',
                                            self.parent.table_name,
                                            tuple(column_names),
                                            query_values=tuple(query_values)
                                            )
        if result[0]:
            self.controller.handler(*result)

        if not result[0]:
            tk.messagebox.showinfo(
                message=self.parent.table_name + " cadastrado com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.menu.raise_parent()

    def refresh(self):
        for entry in self.entries:
            if entry[2] == ScrolledText:
                entry[1].delete('1.0', tk.END)
            else:
                entry[1].set('')

    def set_id(self):
        pass

class Update():
    def __init__(self, menu, parent, controller, entries):
        self.controller = controller
        self.parent = parent
        self.menu = menu
        self.selected_id = ''

        self.entries = entries

    def update_form(self):
        row_values = list(self.row.values())[1:]
        entry_objs = [x[1] for x in self.entries]
        zipped_entries = zip(self.entries, row_values)

        for entry, value in zipped_entries:
            if entry[2] == DateEntry:
                raw_date = value.strftime('%Y/%m/%d')
                date = raw_date.split('/')
                date_fix = date[2] + '/' + date[1] + '/' + date[0]
                entry[1].set(date_fix)
                continue

            if entry[2] == ScrolledText:
                entry[1].insert('1.0', value[:-1])
            else:
                entry[1].set(value)

    def callback(self):
        old_values = []
        query_values = []
        column_names = []
        row_values = list(self.row.values())[1:]
        zipped_entries = zip(self.entries, row_values)

        for entry, value in zipped_entries:
            key = entry[0]
            entry_type = entry[2]
            entry_type = entry[2]
            if entry_type == ScrolledText:
                text = entry[1].get('1.0', tk.END)
            else:
                text = entry[1].get()

            if entry_type == DateEntry:
                value = value.strftime('%Y/%m/%d')
                date = text.split('/')
                text = date[2] + '/' + date[1] + '/' + date[0]

            if text == '':
                text = None

            if text != str(value):
                old_values.append(str(value))
                query_values.append(str(text))
                column_names.append(key)

        if len(old_values) == 0:
            tk.messagebox.showwarning(
                message="Nenhuma mudança encontrada em " + self.parent.table_name + "!")
            return

        confirm_message = "Os seguintes valores serão atualizados: "
        for key, old, new in zip(column_names, old_values, query_values):
            if len(old.split('/')) == 3 and len(new.split('/')) == 3:
                old_splitted = old.split('/')
                old = old_splitted[2] + '/' + \
                    old_splitted[1] + '/' + old_splitted[2]
                new_splitted = new.split('/')
                new = new_splitted[2] + '/' + \
                    new_splitted[1] + '/' + new_splitted[2]

            confirm_message = confirm_message + "\n\n" + \
                key + " de: " + old + " para: " + new
        confirm_message = confirm_message + "\n\n Deseja continuar?"
        confirm_response = tk.messagebox.askyesno(message=confirm_message)

        if not confirm_response:
            return

        result = self.controller.send_query('UPDATE',
                                            self.parent.table_name,
                                            column_names,
                                            query_values=query_values,
                                            where='id'+self.parent.table_name,
                                            where_values=self.selected_id
                                            )
        if result[0]:
            self.controller.handler(*result)

        if not result[0]:
            tk.messagebox.showinfo(
                message=self.parent.table_name + " atualizado com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.menu.raise_parent()

    def refresh(self):
        for entry in self.entries:
            if entry[2] == ScrolledText:
                text = entry[1].delete('1.0', tk.END)
            else:
                text = entry[1].set('')

    def set_id(self, input_id):
        self.selected_id = input_id
        code, message, selected_row = self.controller.send_query('SELECT',
                                                                 self.parent.table_name,
                                                                 '*',
                                                                 where='id'+self.parent.table_name,
                                                                 where_values=self.selected_id)

        self.row = selected_row[0]
        self.update_form()


class Delete():
    def __init__(self, menu, parent, controller, entries):
        self.controller = controller
        self.parent = parent
        self.menu = menu
        self.selected_id = ''
        self.entries = entries

    def update_form(self):
        row_values = list(self.row.values())[1:]
        entry_objs = [x[1] for x in self.entries]
        zipped_entries = zip(self.entries, row_values)

        for entry, value in zipped_entries:
            if entry[2] == DateEntry:
                raw_date = value.strftime('%Y/%m/%d')
                date = raw_date.split('/')
                date_fix = date[2] + '/' + date[1] + '/' + date[0]
                entry[1].set(date_fix)
                continue

            if entry[2] == ScrolledText:
                text = entry[1].insert('1.0', value)
                entry[1].config(state='disabled')
            else:
                entry[1].set(value)

    def callback(self):
        confirm_message = "Tem certeza que deseja deletar \n\n" + \
            self.parent.table_name + " : " + self.selected_id
        confirm_response = tk.messagebox.askyesno(message=confirm_message)

        if not confirm_response:
            return

        result = self.controller.send_query('DELETE',
                                            self.parent.table_name,
                                            '',
                                            where='id'+self.parent.table_name,
                                            where_values=self.selected_id
                                            )
        if result[0]:
            self.controller.handler(*result)

        if not result[0]:
            tk.messagebox.showinfo(
                message=self.parent.table_name+" : "+self.selected_id+" removido com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.menu.raise_parent()

    def refresh(self):
        for entry in self.entries:
            if entry[2] == ScrolledText:
                entry[1].delete('1.0', tk.END)
            else:
                entry[1].set('')

    def set_id(self, input_id):
        self.selected_id = input_id

        code, message, selected_row = self.controller.send_query('SELECT',
                                                                 self.parent.table_name,
                                                                 '*',
                                                                 where='id'+self.parent.table_name,
                                                                 where_values=self.selected_id)

        self.row = selected_row[0]
        self.update_form()
