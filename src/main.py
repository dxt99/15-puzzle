import os
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from puzzlesolver import *
from tkinter.messagebox import showinfo

### NON-UI VARIABLES
# input
config = ""

# puzzle animation config
puzzle_start = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
zero_pos = (3,3)
moves = []

# puzzle solving details
kurang = []
kurangSum = 0
X = []
mincost = 0
duration = 0
total = 0

### BUTTONS
# file select button
def select_file():
    global config
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./test',
        filetypes=filetypes)

    filename_label.config(text = "Config: " + os.path.basename(filename))
    config = filename

#call puzzle solver
def solve():
    global puzzle_start, zero_pos, moves, puzzle_labels
    global kurang, kurangSum, X, mincost, duration, total

    animate_button.place_forget()
    reset_button.place_forget()

    if (len(config)==0):
        status_label.config(text = "File config tidak valid!")
        return
    psolver = puzzlesolver(config)
    if (len(psolver.puzzle)==0):
        status_label.config(text = "File config tidak valid!")
        return
    status_label.config(text = "Solving...")
    root.update()
    # CALL FUCNTION
    start = time.time()
    kurangSum = psolver.solve()
    end = time.time()
    print('done')
    duration = end - start
    if kurangSum%2!=0:
        status_label.config(text = "Tidak ada solusi!")
        puzzle_start = copy.deepcopy(psolver.puzzle)
        moves = []
    else:
        status_label.config(text = "Solusi ditemukan!")
        puzzle_start = copy.deepcopy(psolver.puzzle)
        moves = copy.deepcopy(psolver.answer)
        animate_button.place(x=110, y=225)
        reset_button.place(x=110, y=260)
    kurang = copy.deepcopy(psolver.kurang)
    X = psolver.X
    mincost = psolver.mincost
    total = psolver.total
    details_button.place(x=20, y=110)
    resetPuzzle()

def details():
    info = "Execution time: "+str(duration*1000)+" ms\n"
    info += "Jumlah simpul yang dibangkitkan: " + str(total) + "\n"
    info += "Jumlah fungsi kurang adalah " + str(kurangSum) + "\n" 
    for i in range(1,16):
        info += "Nilai fungsi kurang " + str(i) + ": " + str(kurang[i]) + "\n"
    info += "Nilai fungsi kurang 16: " + str(kurang[0]) + "\n"
    showinfo(
        title='Solution Details',
        message=info
    )

# reset puzzle ui
def resetPuzzle():
    global zero_pos
    for i in range(4):
        for j in range(4):
            if puzzle_start[i][j]==0:
                zero_pos = (i,j)
                puzzle_labels[i][j].config(text = "")
            else:
                puzzle_labels[i][j].config(text = str(puzzle_start[i][j])) 
    root.update()     

# animate solution
def animate():
    resetPuzzle()
    global puzzle_labels
    puzzle = copy.deepcopy(puzzle_start)
    zero = copy.deepcopy(zero_pos)

    for dxy in moves:
        time.sleep(1)
        zx, zy = zero
        dx, dy = dxy
        puzzle[zx][zy], puzzle[zx+dx][zy+dy] = puzzle[zx+dx][zy+dy], puzzle[zx][zy]
        puzzle_labels[zx+dx][zy+dy].config(text = "")
        puzzle_labels[zx][zy].config(text = str(puzzle[zx][zy]))
        zero = (zx + dx, zy + dy)
        root.update()

### TKINTER SETTINGS
# setting the windows size
root=Tk()
root.title("15 Puzzle Solver")
root.geometry("300x300")

# label
prompt_label = Label(root, text = 'Pilih masukan puzzle:', font=('calibre',8))
prompt_label.place(x=20, y=8)

# open button
open_button = ttk.Button(
    root,
    text='Select file',
    command=select_file
)
open_button.place(x=20, y=30)

#filename
filename_label = Label(root, text = 'File config belum dipilih', font=('calibre',8))
filename_label.place(x=20, y=56)

# solve button
solve_button = ttk.Button(
    root,
    text='Solve',
    command=solve
)
solve_button.place(x=20, y=78)

# status_label
status_label = Label(root, text = '', font=('calibre',8))
status_label.place(x=100, y=80)

# kurang_label
kurang_label = Label(root, text = '', font=('calibre',8))
kurang_label.place(x=20, y=104)

# puzzle labels
puzzle_labels=[[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        puzzle_labels[i][j] = Label(root, text = str(i*4+j+1), font=('calibre',8),
            height= 1, width=2, anchor=CENTER,
            borderwidth=1, relief="solid")
        puzzle_labels[i][j].place(x=110+20*j, y=135+20*i)
puzzle_labels[3][3].config(text= " ")

# animate button
animate_button = ttk.Button(
    root,
    text='Animate',
    command=animate
)


# reset button
reset_button = ttk.Button(
    root,
    text='Reset',
    command=resetPuzzle
)


# reset button
details_button = ttk.Button(
    root,
    text='Details',
    command=details
)

root.mainloop()