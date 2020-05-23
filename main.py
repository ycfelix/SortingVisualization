from tkinter import messagebox
import tkinter as tk
import threading
import time
import graphics
import timeit
import re
import random
import sys

window = tk.Tk()
window.title('Sorting visualization')

ALGO_OPTIONS = [
    "Bubble sort",
    "Heap sort",
    "Quick sort"
]
SPEED_OPTIONS = ["1","2","3","4"]

detail = tk.StringVar()
running = tk.StringVar()
speed_var = tk.StringVar(window)
sort_algo = tk.StringVar(window)
default_arr = [random.randint(-50, 50) for i in range(19)]
default = tk.StringVar(window, value="{}".format(default_arr))

speed_var.set(SPEED_OPTIONS[0])
pause = tk.IntVar()
sort_algo.set(ALGO_OPTIONS[0])

height, width = 400, 600
expand = 30

def sort_click():
    global entry, sort_btn
    sort_btn["state"] = tk.DISABLED
    running.set(str(0))
    algo = sort_algo.get()
    arr = re.findall("^\[[\d|,|\s|\-|\.]*\]$", entry.get())
    if not arr:
        messagebox.showinfo("Wrong input!", '''
           your input is wrong!''')
        return
    else:
        arr = eval(arr[0])
    detail.set("Sorting algorithm:{} \n Expected output:{}".format(algo, sorted(arr)))
    def sort_by_time():
        global photo,canvas
        canvas.delete("all")
        bars = graphics.init_graphics(height, width, arr, canvas)
        if algo == ALGO_OPTIONS[0]:
            bubble_sort(bars, canvas)
        elif algo == ALGO_OPTIONS[1]:
            heap_sort(bars, canvas)
        elif algo == ALGO_OPTIONS[2]:
            start = timeit.default_timer()
            quick_sort(bars, 0, len(bars) - 1, start, canvas)
        sort_btn["state"] = tk.NORMAL
    running_thread = threading.Thread(target=sort_by_time)
    running_thread.start()


'''
play animation here
'''


def swap(arr, i, j, canvas, start):
    fast = int(speed_var.get())
    ei, bari, texti, xi1, yi1, xi2, yi2 = arr[i]
    ej, barj, textj, xj1, yj1, xj2, yj2 = arr[j]
    if ei == ej:
        return
    canvas.itemconfig(bari, fill='red')
    canvas.itemconfig(barj, fill='red')
    canvas.itemconfig(texti, fill='red')
    canvas.itemconfig(textj, fill='red')
    for dis in range(abs(xj1 - xi1)):
        while pause.get():
            time.sleep(1)
        if xj1 > xi1:
            canvas.move(bari, 1, 0)
            canvas.move(barj, -1, 0)
            canvas.move(texti, 1, 0)
            canvas.move(textj, -1, 0)
        else:
            canvas.move(bari, -1, 0)
            canvas.move(barj, 1, 0)
            canvas.move(texti, -1, 0)
            canvas.move(textj, 1, 0)
        time.sleep((1 / fast) / abs(xj1 - xi1))
        running.set("Running time: " + "{0:.2f} s".format(timeit.default_timer() - start))
    arr[i][3], arr[j][3] = arr[j][3], arr[i][3]
    arr[i][5], arr[j][5] = arr[j][5], arr[i][5]
    arr[i], arr[j] = arr[j], arr[i]
    canvas.itemconfig(texti, fill='green')
    canvas.itemconfig(textj, fill='green')
    canvas.itemconfig(bari, fill='black')
    canvas.itemconfig(barj, fill='black')


def partition(arr, low, high, canvas, start):
    i = (low - 1)
    pivot = arr[high][0]
    for j in range(low, high):
        if arr[j][0] < pivot:
            i = i + 1
            swap(arr, i, j, canvas, start)
    swap(arr, i + 1, high, canvas, start)
    return (i + 1)


def quick_sort(arr, low, high, start, canvas):
    if low < high:
        pi = partition(arr, low, high, canvas, start)
        quick_sort(arr, low, pi - 1, start, canvas)
        quick_sort(arr, pi + 1, high, start, canvas)



def bubble_sort(bars, canvas):
    start = timeit.default_timer()
    for i in range(len(bars)):
        for j in range(len(bars)):
            if j <= i:
                continue
            if bars[j][0] < bars[i][0]:
                swap(bars, i, j, canvas, start)


def help_click():
    messagebox.showinfo("Sample input", '''
    python array format \n Example: [1,3,7,9,5,4,2,6]''')


def heapify(arr, n, i, canvas, start):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i][0] < arr[l][0]:
        largest = l
    if r < n and arr[largest][0] < arr[r][0]:
        largest = r
    if largest != i:
        swap(arr, i, largest, canvas, start)
        heapify(arr, n, largest, canvas, start)


def heap_sort(arr, canvas):
    start = timeit.default_timer()
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i, canvas, start)
    for i in range(n - 1, 0, -1):
        swap(arr, i, 0, canvas, start)
        heapify(arr, i, 0, canvas, start)


header_label = tk.Label(window, text='Enter a customized array')
header_label.pack()


def close_program():
    window.destroy()
    sys.exit()


tk.Button(window, text='close program', command=close_program).pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)

height_label = tk.Label(height_frame, text='array of integer')
height_label.pack(side=tk.LEFT)

entry = tk.Entry(height_frame, width=60, textvariable=default)
entry.pack(side=tk.LEFT)

help_btn = tk.Button(height_frame, text='help', command=help_click)
help_btn.pack(side=tk.LEFT)

menu = tk.OptionMenu(window, sort_algo, *ALGO_OPTIONS)
menu.pack()

button_area = tk.Frame(window)
button_area.pack(side=tk.TOP)

speed_label = tk.Label(button_area, text='Animation speed')
speed_label.pack(side=tk.LEFT)

speed = tk.OptionMenu(button_area, speed_var, *SPEED_OPTIONS)
speed.pack(side=tk.LEFT)

sort_btn = tk.Button(button_area, text='sort', command=sort_click)
sort_btn.pack(side=tk.LEFT)

tk.Checkbutton(button_area, text="Pause", variable=pause).pack(side=tk.LEFT)

detail_label = tk.Label(window, textvariable=detail)
detail_label.pack()

running_label = tk.Label(window, textvariable=running)
running_label.pack()

canvas = tk.Canvas(window, width=width + expand, height=height + expand)
canvas.pack()

window.mainloop()
