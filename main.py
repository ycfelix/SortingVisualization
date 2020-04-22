import tkinter as tk

window = tk.Tk()
window.title('BMI App')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()

# 以下為 height_frame 群組
height_frame = tk.Frame(window)
# 向上對齊父元件
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（m）')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

# 以下為 weight_frame 群組
weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算')
calculate_btn.pack()

window.mainloop()