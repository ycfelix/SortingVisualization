import numpy as np

'''
tuples of arr_item, bar matrix,bar height, start_x,end_x
'''

def get_height(arr_item,min_val,max_val,step_height):
    return int(((arr_item-min_val)/(max_val-min_val)+1)*step_height)

def make_bar(barwidth,barheight):
    result=np.zeros(((barheight,barwidth)))
    result[5:barheight-5,5:barwidth-5]=255
    return result

def render_graph(h,w,bars):
    result = np.zeros((h, w))
    for item in bars:
        e, bar,barheight,start,end=item
        result[0:barheight, start:end] = bar
    return result


def init_graphics(h,w,arr):
    bars=[]
    arr=np.array(arr)
    result=np.zeros((h,w))
    min_item=np.min(arr)
    max_item=np.max(arr)
    step_height=h//(max_item-min_item)
    barwidth = w // arr.shape[0]
    for i,e in enumerate(arr):
        barheight=get_height(e,min_item,max_item,step_height)
        bar=make_bar(barwidth,barheight)
        result[0:barheight,i*barwidth:(i+1)*barwidth]=bar
        bars.append([e,bar,barheight,i*barwidth,(i+1)*barwidth])
    return result,bars
