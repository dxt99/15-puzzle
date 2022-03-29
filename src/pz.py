from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

class MsgPanel(ttk.Frame):
    def __init__(self, master, msgtxt):
        ttk.Frame.__init__(self, master)
        self.pack(side=TOP, fill=X)
        
        msg = Label(self, wraplength='4i', justify=LEFT)
        msg['text'] = ''.join(msgtxt)
        msg.pack(fill=X, padx=5, pady=5)

class PuzzleDemo(Frame):
    def __init__(self, isapp=True, name='puzzledemo'):
        Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('15 Puzzle Demo')
        self.isapp = isapp
        MsgPanel(self,[])
        self._create_demo_panel()

    def _create_demo_panel(self):
        bgColor = 'gray80'  # colour for panel background and empty space
        
        # if width and height are not specifically set buttons are positioned
        # in a 0 size window and do not show up
        demoPanel = Frame(self, borderwidth=2, relief=SUNKEN, background=bgColor,
                          width=120, height=120)
        demoPanel.pack(side=TOP, pady=1, padx=1)
        
        # buttons are placed relative to the top, left corner of demoPanel
        # with relations expressed as a value between 0.0 and 1.0
        # top, left corner = (x,y) = (0,0)
        # bottom, right corner = (x,y) = (1,1)
        self.xypos = {}
        self.xypos['space'] = (.75, .75)
        order = [3, 1, 6, 2, 5, 7, 15, 13, 4, 11, 8, 9, 14, 10, 12]
        
        for i in range(15):
            num = order[i]
            self.xypos[num] = ( i%4 * .25, i//4 * .25)
            b = ttk.Button(text=num, style='Puzzle.TButton')
            b['command'] =lambda b=b: self._puzzle_switch(b)
            b.place(in_=demoPanel, relx=self.xypos[num][0], rely=self.xypos[num][1],
                    relwidth=.25, relheight=.25)
        
        # set button background to demoPanel background
        ttk.Style().configure('Puzzle.TButton', background=bgColor)
        
    def _puzzle_switch(self, button):
        num = button['text']
        sx = self.xypos['space'][0]     # position of 'space'
        sy = self.xypos['space'][1]
        x = self.xypos[num][0]          # position of selected button
        y = self.xypos[num][1]
        
        # is the selected button next to the space?
        if(    sy-.01 <= y <= sy+.01 and sx-.26 <= x <= sx+.26
            or sx-.01 <= x <= sx+.01 and sy-.26 <= y <= sy+.26):
            
            # swap button with space
            self.xypos['space'], self.xypos[num] = self.xypos[num], self.xypos['space']
            
            # re-position button
            button.place(relx=self.xypos[num][0], rely=self.xypos[num][1])
        
if __name__ == '__main__':
    PuzzleDemo().mainloop()