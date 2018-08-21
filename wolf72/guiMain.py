from tkinter import *
from tkinter import filedialog
import muster.commons


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.einlese_Button = Button(text="Datei einlesen...",command=self.read_file)
        self.einlese_Button.pack(side="top")
        self.quit = Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def read_file(self):
        self.einlesen = filedialog.askopenfilename(initialdir="../", title="Datei auswählen", filetypes=(("CSV Dateien", "*.csv"), ("Text Dateien", "*.txt")))
        print(self.einlesen)
        contentList = muster.commons.read_csv(self.einlesen)

        spaltennamen = (u"Vorname", u"Nachname", u"Ort")
        datenzeilen = (
                              (u"Max", u"Mustermann", u"Bremen"),
                              (u"Moriz", u"Mustermann", u"Hausen"),
                              (u"Maria", u"Wurstlbrumpft", u"München"),
                              (u"Marion", u"Hupfer", u"Telfs"),
                              (u"Dani", u"Ella", u"Oberhofen"),
                          ) * 20

        f = Application(spaltennamen=spaltennamen, datenzeilen=datenzeilen)
        f.Center()
        f.Show()


root = Tk()
app = Application(master=root)
app.mainloop()
