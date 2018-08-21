from tkinter import *
import oeick.csv_functions as csvf
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Application(Frame):
    TEXT_WIDTH = 120

    def __init__(self, master=None):
        list_of_dicts = None

        Frame.__init__(self, master)
        master.geometry('1000x500')
        self.header_textbox = Text(master, height=1, width=self.TEXT_WIDTH)
        self.header_textbox.grid(row=0, column=0, columnspan=3, rowspan=1)

        self.inhalt_textbox = Text(master, height=5, width=self.TEXT_WIDTH)
        self.inhalt_textbox.grid(row=1, column=0, columnspan=3, rowspan=3)

        vorgaben = {'Komma', 'Semikolon'}
        self.auswahl = StringVar()
        auswahl_dropdown = OptionMenu(master, self.auswahl, *vorgaben)
        self.auswahl.set(list(vorgaben)[0])
        auswahl_dropdown.grid(row=4, column=0)

        laden_btn = Button(text='Laden', command=self.text_laden)
        laden_btn.grid(row=4, column=1)

        save_btn = Button(text='Speichern', command=self.text_speichern)
        save_btn.grid(row=4, column=2)

    def max_field_sizes(self):
        max_fs = [len(f) for f in list(self.list_of_dicts[0].keys())]
        for row in self.list_of_dicts:
            for i in range(len(row)):
                field_size = len(row[list(row.keys())[i]])
                current_max = max_fs[i]
                max_fs[i] = max(field_size, current_max)
        return max_fs

    def put_list_of_dicts_into_textbox(self):
        self.inhalt_textbox.delete('1.0', END)
        self.header_textbox.delete('1.0', END)
        max_fs = self.max_field_sizes()
        fieldnames = list(self.list_of_dicts[0].keys())
        header_str = ''.join([("{:"+str(max_fs[i]+1)+"}").format(fieldnames[i]) for i in range(len(fieldnames))])
        self.header_textbox.insert(END, header_str + '\n')
        for row in self.list_of_dicts:
            row_string = ''
            for i in range(len(row)):
                field_content = row[list(row.keys())[i]]
                row_string = row_string + ("{:"+str(max_fs[i]+1)+"}").format(field_content)
            self.inhalt_textbox.insert(END, row_string + '\n')

    def get_delimiter(self):
        return ',' if self.auswahl.get() == 'Komma' else ';'

    def text_speichern(self):
        filename = asksaveasfilename()
        csvf.write_csv_file(filename, self.list_of_dicts, delimiter=self.get_delimiter())

    def text_laden(self):
        self.inhalt_textbox.delete('1.0', END)
        filename = askopenfilename()
        print(self.auswahl.get())
        self.list_of_dicts = csvf.read_csv_file(filename, delimiter=self.get_delimiter())
        self.put_list_of_dicts_into_textbox()


root = Tk()
app = Application(master=root)
app.mainloop()