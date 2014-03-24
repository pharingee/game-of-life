from Tkinter import *
from torus import Torus

def next():
    t.next_step()
    refresh()

def previous():
    t.previous()
    refresh()

def task():
    t.next_step()
    refresh()
    window.after(200, task)

def refresh():
    for y in xrange(torus_height):
        for x in xrange(torus_width):
            if t.cells[y][x]:
                labels[y][x].config(bg='white')
            else:
                labels[y][x].config(bg='black')

if __name__ == '__main__':

    try:
        percent = int(raw_input('Enter the percentage of live cells: '))

        torus_width = int(raw_input('Enter the torus width: '))
        torus_height = int(raw_input('Enter the torus height: '))
    except ValueError:
        pass

    t = Torus(torus_width, torus_height, percent)

    window = Tk()

    frame = Frame()
    frame.grid()
    labels = []



    y = 0

    while y < torus_height:
        x = 0
        xlabels = []
        while x < torus_width:
            if t.cells[y][x]:
                xlabels.append(
                    Label(frame, width=5, relief='sunken', bg='white'))
            
                xlabels[x].grid(
                    row=y%torus_height, column=x%torus_width)
            
            else:
                xlabels.append(
                    Label(frame, width=5, relief='sunken', bg='black'))
            
                xlabels[x].grid(
                    row=y%torus_height, column=x%torus_width)
            x += 1
        labels.append(xlabels)
        y += 1

    frame2 = Frame()
    frame2.grid()

    button = Button(frame2, text='Next', command=next)
    button.grid(row=1, column=1)

    button2 = Button(frame2, text='Previous', command=previous)
    button2.grid(row=1, column=2)

    # window.after(200, task)
    window.mainloop()