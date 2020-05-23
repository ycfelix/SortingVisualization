from tkinter import messagebox
import tkinter as tk
import PIL.Image, PIL.ImageTk
import threading
import time
import numpy as np
import graphics
import cv2
window = tk.Tk()
window.title('Sorting visualization')

OPTIONS = [
"Bubble sort",
"Merge sort",
"Quick sort"
]
# cv_img=cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
cv_img=np.zeros((400,600))
height, width=cv_img.shape
image_on_canvas=None
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

def sort_click():
    global entry
    algo=sort_algo.get()
    # arr=eval(entry.get())
    def sort_by_time():
        global photo, canvas
        cv_img[:,:],bars = graphics.init_graphics(height,width,[7,6,5,4,3,2,1])
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        bubble_sort(bars)

    t=threading.Thread(target=sort_by_time)
    t.start()

'''
play animation here
'''
def swap(arr,i,j):
    global photo, canvas
    e1, bar1, barheight1, start1, end1=arr[i]
    e2, bar2, barheight2, start2, end2=arr[j]
    for dis in range(start2-start1):
        arr[i][3] = start1+dis
        arr[i][4] = end1+dis
        arr[j][3] = start2-dis
        arr[j][4] = end2-dis
        cv_img[:, :]=graphics.render_graph(height, width,arr)
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    arr[i],arr[j]=arr[j],arr[i]
    cv_img[:, :] = graphics.render_graph(height, width, arr)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)

def bubble_sort(bars):
    for i in range(len(bars)):
        for j in range(len(bars)):
            if j<=i:
                continue
            if bars[j][0]<bars[i][0]:
                swap(bars,i,j)


def help_click():
    messagebox.showinfo("Sample input", '''
    python array format \n Example: [1,3,7,9,5,4,2,6]''')

sort_algo=tk.StringVar(window)
sort_algo.set(OPTIONS[0])

header_label = tk.Label(window, text='Enter a customized array')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)

height_label = tk.Label(height_frame, text='array of integer')
height_label.pack(side=tk.LEFT)

entry = tk.Entry(height_frame,width=60)
entry.pack(side=tk.LEFT)

help_btn = tk.Button(height_frame, text='help',command=help_click)
help_btn.pack(side=tk.LEFT)

menu = tk.OptionMenu(window, sort_algo, *OPTIONS)
menu.pack()

sort_btn = tk.Button(window, text='sort',command=sort_click)
sort_btn.pack()

canvas = tk.Canvas(window, width = width, height = height)
canvas.pack()

canvas.create_image(0, 0, image=photo, anchor=tk.NW)


window.mainloop()