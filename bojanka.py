import tkinter as tk
from tkinter.colorchooser import askcolor

#Glavni prozor

root=tk.Tk()
root.geometry("1600x900")
root.state("zoomed")
root.title("Program za crtanje")
root.grid_columnconfigure(0,weight=1)

#Okvir za canvas

canvasFrame = tk.Frame(root, bg="gray85", height=740)

canvasFrame.grid_columnconfigure(0,weight=1)
canvasFrame.grid_columnconfigure(0,weight=1)

canvasFrame.grid_rowconfigure(0, weight=1, minsize=740)

#Prozor za spremanje

def openSave():
    root.update()
    saveWindow = tk.Toplevel()
    saveWindow.title("Save")
    saveWindow.geometry("500x300")

    closeButton = tk.Button(saveWindow, text="Close", command=saveWindow.destroy)
    closeButton.pack()

#Prozor za otvaranje pohranjenog projekta

def openOpen():
    root.update()
    openWindow = tk.Toplevel()
    openWindow.title("Open...")
    openWindow.geometry("500x300")

    closeButton = tk.Button(openWindow, text="Close", command=openWindow.destroy)
    closeButton.pack()

#Prozor za otvaranje novog projekta

canvas = tk.Canvas(canvasFrame, height=0, width=0)

def openNew():
    root.update()
    newWindow = tk.Toplevel()
    newWindow.title("New project")
    newWindow.geometry("180x80")

    widthLabel = tk.Label(newWindow, text="Width: ")
    widthEntry=tk.Entry(newWindow)
    heightLabel = tk.Label(newWindow, text="Height: ")
    heightEntry=tk.Entry(newWindow)

    def newCanavs(): #metoda koja stvara novi canvas za crtanje
        canvasHeight=heightEntry.get()
        canvasWidth=widthEntry.get()
        if(canvasWidth.isnumeric() and canvasHeight.isnumeric()):
            if(int(canvasWidth)>0 and int(canvasHeight)>0):
                for widget in canvasFrame.winfo_children(): #brisanje već postojećeg canvasa
                    widget.destroy()
                root.update()
                canvas = tk.Canvas(canvasFrame, height=int(canvasHeight), width=int(canvasWidth))
                canvas.grid(row=0, column=0)
                newWindow.destroy()
    
    newCanvasButton=tk.Button(newWindow, text="Create", command=newCanavs)

    widthLabel.grid(row=0, column=0)
    widthEntry.grid(row=0, column=1)
    heightLabel.grid(row=1, column=0)
    heightEntry.grid(row=1, column=1)
    newCanvasButton.grid(row=2, column=1, columnspan=2)

#Meni

menubar = tk.Menu(root)
fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label="New", command=openNew)
fileMenu.add_command(label="Open", command=openOpen)
fileMenu.add_command(label="Save", command=openSave)
menubar.add_cascade(label="File", menu=fileMenu)

root.config(menu=menubar)


#Okvir za zaglavlje s alatima

header = tk.Frame(root, bg="white", pady=5)

header.columnconfigure(0, weight=1)
header.columnconfigure(1, weight=1)
header.columnconfigure(2, weight=1)
header.columnconfigure(3, weight=7)
header.columnconfigure(4, weight=1)
header.columnconfigure(5, weight=1)
header.columnconfigure(6, weight=1)
header.columnconfigure(7, weight=1)
header.columnconfigure(8, weight=1)
header.columnconfigure(9, weight=1)
header.columnconfigure(10, weight=1)
header.columnconfigure(11, weight=1)
header.columnconfigure(12, weight=1)

header.rowconfigure(0, weight=1, minsize=50)

#Gumb za olovku

pencilimg=tk.PhotoImage(file="images\olovka_ikona.png")
pencil = tk.Button(header, image=pencilimg, width=25, height=25)
pencil.grid(row=0, column=0)

pencilLabel = tk.Label(header, text="Olovka", bg="white")
pencilLabel.grid(row=1, column=0)

#Gumb za gumicu

eraserimg=tk.PhotoImage(file="images\gumica_ikona.png")
eraser = tk.Button(header, image=eraserimg, width=25, height=25)
eraser.grid(row=0, column=1)

eraserLabel = tk.Label(header, text="Gumica", bg="white")
eraserLabel.grid(row=1, column=1)

#Slider za veličinu olovke

pencilSize = tk.Scale(header, from_=0, to=100, orient="horizontal", bg="white", bd=0, highlightthickness=0)
pencilSize.grid(row=0, column=2)

sizeLabel = tk.Label(header, text="Veličina", bg="white")
sizeLabel.grid(row=1, column=2)

deafultButton=tk.PhotoImage(file='images\deafult_gumb.png') #slika koja definira oblik gumbi za boje

#Gumbi za predefinirane boje

redBtn = tk.Button(header, bg="red", image=deafultButton)
redBtn.grid(row=0, column=4)

orangeBtn = tk.Button(header, bg="orange", image=deafultButton)
orangeBtn.grid(row=0, column=5)

yellowBtn = tk.Button(header, bg="yellow", image=deafultButton)
yellowBtn.grid(row=0, column=6)

greenBtn = tk.Button(header, bg="green", image=deafultButton)
greenBtn.grid(row=0, column=7)

blueBtn = tk.Button(header, bg="blue", image=deafultButton)
blueBtn.grid(row=0, column=8)

purpleBtn = tk.Button(header, bg="purple", image=deafultButton)
purpleBtn.grid(row=0, column=9)

blackBtn = tk.Button(header, bg="black", image=deafultButton)
blackBtn.grid(row=0, column=10)

whiteBtn = tk.Button(header, bg="white", image=deafultButton)
whiteBtn.grid(row=0, column=11)

#Odabir custom boje

chosenColor="white"
def colorPicking():
    colorCode = askcolor(title ="Choose color")[1]
    if colorCode:
        chosenColor = colorCode
        colorPickerBtn.config(bg=chosenColor)

eyedropimg=tk.PhotoImage(file='images\odabir_boje_ikona.png')
colorPickerBtn = tk.Button(header, text="custom", command=colorPicking, image=eyedropimg, width=25, height=25)
colorPickerBtn.grid(row=0, column=12)

bojeLabel = tk.Label(header, text="Odabir boje", bg="white")
bojeLabel.grid(row=1, column=12)

header.grid(row=0, column=0, sticky="ew")

canvasFrame.grid(row=1, column=0, sticky="nsew")

root.mainloop()