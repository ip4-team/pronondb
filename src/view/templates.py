import tkinter as tk

from tkinter import ttk
from functools import partial
from tkcalendar import Calendar, DateEntry

from datetime import datetime


class Register(tk.Frame):
    def __init__(self, parent, controller, fields):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.fields = fields
        self.entries = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=self.exit)
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=self.callback)
        query_button.pack(side=tk.RIGHT, padx=5)

    def make_form(self):
        entries = []
        for key in self.fields:
            label_text = self.fields[key]['label']
            entry = self.fields[key]['entry']

            row = tk.Frame(self)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            lab = ttk.Label(row, width=35, text=label_text, anchor='w')
            lab.pack(side=tk.LEFT, padx=15)

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, text=v[0], value=v[1], variable=ent_var)
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='readonly',
                            values=self.fields[key]['value'], variable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy',
                            textvariable=ent_var)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, textvariable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        return entries

    def callback(self):
        query_values = []
        column_names = []
        for entry in self.entries:
            key = entry[0]
            text = entry[1].get()
            entry_type = entry[2]

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
            tk.messagebox.showinfo(message=self.parent.table_name + " cadastrado com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.parent.raise_parent()

    def refresh(self):
        for entry in self.entries:
            entry[1].set('')


class Update(tk.Frame):
    def __init__(self, parent, controller, fields):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.selected_id = ''
        self.fields = fields
        self.entries = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=self.exit)
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Salvar",
                                  command=self.callback)
        query_button.pack(side=tk.RIGHT, padx=5)

    def make_form(self):
        entries = []
        for key in self.fields:
            label_text = self.fields[key]['label']
            entry = self.fields[key]['entry']

            row = tk.Frame(self)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            lab = ttk.Label(row, width=35, text=label_text, anchor='w')
            lab.pack(side=tk.LEFT, padx=15)

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, text=v[0], value=v[1], variable=ent_var)
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='readonly',
                            values=self.fields[key]['value'], variable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, date_pattern='dd/mm/yyyy',
                            textvariable=ent_var)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, textvariable=ent_var)
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        return entries

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
            tk.messagebox.showinfo(message=self.parent.table_name + " atualizado com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.parent.raise_parent()

    def refresh(self):
        for entry in self.entries:
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


class Delete(tk.Frame):
    def __init__(self, parent, controller, fields):
        self.controller = controller
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.selected_id = ''
        self.fields = fields
        self.entries = self.make_form()
        # Send Query button
        back_button = ttk.Button(self, text="Voltar",
                                 command=self.exit)
        back_button.pack(side=tk.LEFT, padx=5)

        query_button = ttk.Button(self, text="Remover",
                                  command=self.callback)
        query_button.pack(side=tk.RIGHT, padx=5)

    def make_form(self):
        style = ttk.Style()
        style.map('TEntry',
                  foreground=[('disabled', 'black')])
        style.map('TRadiobutton',
                  foreground=[('disabled', 'black')])

        entries = []
        for key in self.fields:
            label_text = self.fields[key]['label']
            entry = self.fields[key]['entry']

            row = tk.Frame(self)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

            lab = ttk.Label(row, width=35, text=label_text, anchor='w')
            lab.pack(side=tk.LEFT, padx=15)

            ent_var = tk.StringVar()
            ent_var.set('')

            # In case that the entry is a radiobutton
            if entry == ttk.Radiobutton:
                for v in self.fields[key]['value']:
                    ent = entry(row, state='disabled',
                                text=v[0], value=v[1], variable=ent_var)
                    #  ent.configure(disabledforeground='black')
                    ent.pack(side=tk.LEFT, padx=15)
            # Combobox
            elif entry == ttk.Combobox:
                ent = entry(row, state='disabled',
                            values=self.fields[key]['value'], variable=ent_var)
                #  ent.configure(disabledforeground='black')
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Date picker
            elif entry == DateEntry:
                ent = entry(row, state='disabled', date_pattern='dd/mm/yyyy',
                            textvariable=ent_var)
                ent.delete(0, "end")
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)
            # Other entries
            else:
                ent = entry(row, state='disabled', textvariable=ent_var)
                #  ent.configure(disabledforeground='black')
                ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X, padx=15)

            entries.append((key, ent_var, entry))
        return entries

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

            entry[1].set(value)

    def callback(self):

        confirm_message = "Tem certeza que deseja deletar \n\n" + self.parent.table_name + " : "+ self.selected_id
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
            tk.messagebox.showinfo(message=self.parent.table_name+" : "+self.selected_id+" removido com sucesso!")
            self.exit()

    def exit(self):
        self.refresh()
        self.parent.raise_parent()

    def refresh(self):
        for entry in self.entries:
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
