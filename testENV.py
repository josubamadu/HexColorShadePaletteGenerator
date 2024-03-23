import tkinter as tk

hexShades = ['#bea5cc', '#a58ab5', '#8d6f9e', '#755587', '#5c3a70', '#441f59', '#2c0542']
squareSideLen = 100
windowWidth = len(hexShades)*squareSideLen
window = tk.Tk()
window.geometry(str(windowWidth)+"x"+str(squareSideLen))
window.title("Palette")
canvas_1 = tk.Canvas(window,width=windowWidth,height=squareSideLen)
canvas_1.pack()
for x in range(len(hexShades)):
    x0 = x*squareSideLen
    y0 = 0
    x1 = x0 + squareSideLen
    y1 = y0 + squareSideLen
    canvas_1.create_rectangle(x0,y0,x1,y1,fill=hexShades[x])

window.mainloop()