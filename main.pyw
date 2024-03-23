import tkinter as tk

def d2h(c):
    val = str(hex(c)[2:])
    if len(val) == 1:
        val = str(0)+str(val)
    return val

def showPalette(hexShades,length=75):
    squareSideLen = length
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
### Start/End Color
start_color = (158, 104, 104)
end_color = (46, 1, 1)
### Number of color shades (including start and end shades) 
number_of_shades = 7

new_shades = number_of_shades - 1
R = (start_color[0] - end_color[0])/new_shades
G = (start_color[1] - end_color[1])/new_shades
B = (start_color[2] - end_color[2])/new_shades
shades = []
hexShades = []

shades.append(start_color)
hexShades.append("#"+d2h(start_color[0])+d2h(start_color[1])+d2h(start_color[2]))

for x in range(1,new_shades+1):
    newR = start_color[0]-(R*x)
    newG = start_color[1]-(G*x)
    newB = start_color[2]-(B*x)
    c = (int(newR),int(newG),int(newB))
    hexShades.append("#"+d2h(c[0])+d2h(c[1])+d2h(c[2]))
    shades.append(c)

#shades.append(end_color)
#hexShades.append("#"+d2h(end_color[0])+d2h(end_color[1])+d2h(end_color[2]))

showPalette(hexShades,50)
print(hexShades)


