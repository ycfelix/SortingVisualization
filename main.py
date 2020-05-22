from tkinter import messagebox
import tkinter as tk
import PIL.Image, PIL.ImageTk
import threading
import time
import cv2
window = tk.Tk()
window.title('Sorting visualization')

OPTIONS = [
"Bubble sort",
"Merge sort",
"Quick sort"
]

def sort_click():
    print("blur")
    # algo=sort_algo.get()
    # def blur_by_time():
    #     global photo,canvas
    #     for i in range(10):
    #         time.sleep(0.05)
    #         cv_img[:,:] = cv2.blur(cv_img, (3, 3))
    #         photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
    #         canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    # t=threading.Thread(target=blur_by_time)
    # t.start()
    pass

def help_click():
    messagebox.showinfo("Sample input", '''
    python array format \n Example: [1,3,7,9,5,4,2,6]''')



cv_img=cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)
# cv_img=np.zeros((400,600))
height, width=cv_img.shape
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

sort_algo=tk.StringVar(window)
sort_algo.set(OPTIONS[0])

header_label = tk.Label(window, text='Enter a customized array')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)

height_label = tk.Label(height_frame, text='array of integer')
height_label.pack(side=tk.LEFT)

height_entry = tk.Entry(height_frame,width=60)
height_entry.pack(side=tk.LEFT)

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