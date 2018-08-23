import tkinter
from tkinter import filedialog
import muster.commons
import wx
import wx.grid





class ContentTableFrame(wx.Frame):
    def create_widgets(self):
        self.einlese_Button = wx.Button()
        buttonPanel = wx.Panel(self)

        self.einlese_Button.Bind(wx.EVT_BUTTON, self.read_file)
        # einlese_Button.pack(side="top")
        # self.quit = tkinter.Button(self, text="QUIT", fg="red",command=self.Destroy())
        # self.quit.pack(side="bottom")

    def read_file(self):
        self.einlesen = filedialog.askopenfilename(initialdir="../", title="Datei auswählen",
                                                   filetypes=(("CSV Dateien", "*.csv"), ("Text Dateien", "*.txt")))
        print(self.einlesen)
        contentList = muster.commons.read_csv(self.einlesen)


    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.create_widgets()
        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)
        gridPanel = wx.Panel(self, 43, wx.DefaultPosition, wx.Size(300, 200))
        vbox = wx.BoxSizer()
        vbox.Add(grid, 0, wx.ALIGN_CENTER)
        vbox.Add(self.einlese_Button, 0, wx.BOTTOM)
        gridPanel.SetSizer(vbox)
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(20, 10)

        # We can set the sizes of individual rows and columns
        # in pixels
        grid.SetRowSize(0, 60)
        grid.SetColSize(0, 120)

        # And set grid cell contents as strings
        grid.SetCellValue(0, 0, 'wxGrid is good')

        # We can specify that some cells are read.only
        grid.SetCellValue(0, 3, 'This is read.only')
        grid.SetReadOnly(0, 3)

        # Colours can be specified for grid cell contents
        grid.SetCellValue(3, 3, 'green on grey')
        grid.SetCellTextColour(3, 3, wx.GREEN)
        grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        grid.SetColFormatFloat(5, 6, 2)
        grid.SetCellValue(0, 6, '3.1415')
        self.Show()



if __name__ == '__main__':

    app = wx.App(0)
    frame = ContentTableFrame(None)
    app.MainLoop()
