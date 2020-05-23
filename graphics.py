import numpy as np
import time
'''
tuples of arr_item, x1,y1,x2,y2
'''

def get_height(arr_item,min_val,max_val,h):
    return int((min(max_val-min_val,arr_item+5-min_val)/(max_val-min_val))*h)

def init_graphics(h,w,arr,canvas):
    bars=[]
    arr=np.array(arr)
    min_item=np.min(arr)
    max_item=np.max(arr)
    barwidth = w // arr.shape[0]
    for i,e in enumerate(arr):
        barheight=get_height(e,min_item,max_item,h)
        bar=canvas.create_rectangle(i*barwidth+5,h-barheight+5,(i+1)*barwidth-5,h-5,fill='black')
        text_x=(i*barwidth+5+(i+1)*barwidth-5)//2
        text_y=h+5
        text=canvas.create_text(text_x, text_y, fill="green", font="Times 12 italic bold",
                           text=str(e))
        bars.append([e,bar,text,i*barwidth+5,h-barheight+5,(i+1)*barwidth-5,h-5])
    return bars