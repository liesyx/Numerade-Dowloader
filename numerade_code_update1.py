
from tkinter import *
from tkinter import filedialog, messagebox
import requests
import os
import sys, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import N
from tkinter import *
import urllib.request


path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

# def select_path(event):
#     global output_path

#     # window.withdraw()
#     output_path = filedialog.askdirectory()
#     path_entry.delete(0, END)
#     path_entry.insert(0, output_path)
#     # window.deiconify()


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)

    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)

    return label


 ############################################
def getlink():

        connect='https://cdn.numerade.com/'
        problsub='encoded/'
        ect='.mp4'
        crssub="coursevideos/"
        ####
        url = URL_entry.get() #get url 
        key = key_entry.get() # get key
        ####
        
        
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('video',)


        for img in images:
            if img.has_attr('poster'):
                site2=img['poster']
        site2.rfind("_")
        site2.rfind("f")
    ###############################################
        
        #Python GUI save a file
        file = filedialog.asksaveasfile(initialdir="C:\\",
                                        defaultextension='.mp4',
                                        filetypes=[
                                            ("MP4 file",".mp4"),
                                        ])
        if file is None:
            return
        
        #get the name file
        file=str(file)
        file_x=file[file.rfind("/")+1:file.rfind(".mp4")+3]#name of file
        
        #dowload video files
        file_duongdandaluu=file[file.rfind("'C:")+1:file.rfind("p4'")+2] #link duong dan da save
        fullfilename = os.path.join(file_duongdandaluu) # path save dowload
    ##################################################
        #filter
        if url.rfind('question')>0:
            core=site2[34:-10] 
            linkv=connect+problsub+core+ect
            print("done")
            
            try:
                messagebox.showinfo(title="Numera Dowloader by _Liesy",
                                message="Downloading starts...")
                
                urllib.request.urlretrieve(linkv, fullfilename)
            
                messagebox.showinfo(title="Numera Dowloader by _Liesy",
                                message="Download completed...!!")
            
            except Exception as e:
                print(e)
        else :
            core=site2[47:-10] 
            linkv2=connect+crssub+core+ect
            print("not done")
            try:
                messagebox.showinfo(title="Numera Dowloader by _Liesy",
                                message="Downloading starts...")
                urllib.request.urlretrieve(linkv2, fullfilename)
                messagebox.showinfo(title="Numera Dowloader by _Liesy",
                                message="Download completed...!!")
            except Exception as e:
                print(e)

################################################
#GUI
window = Tk()
window.title("Numera Dowloader by _Liesy")
window.iconbitmap("image\icon1.ico")
window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
##khai bao bien thong bao
thongbao=Text(window,height=1,width=15)
thongbao.grid(row=2, column=1)
###########
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"image\maxresdefault.png") #chi duoc png
background = canvas.create_image(
    610, 286.0,
    image=background_img)

canvas.create_text(
    700.0, 130,
    text = "NHAP LINK VAO DAY",
    fill = "#ffffff",
    font = ("Roboto-Light", int(14.0)))

canvas.create_text(
    700, 310,
    text = "ENTER KEY",
    fill = "#ffffff",
    font = ("Roboto-Light", int(14.0)))

canvas.create_text(
    98, 563,
    text = "Made By Liesy ^^",
    fill = "#ffffff",
    font = ("Roboto-Thin", int(12.0)))

#box url
URL_entry_img = PhotoImage(file = f"image\img_textBox0.png")
URL_entry_bg = canvas.create_image(
    703.5, 187.5,
    image = URL_entry_img)

URL_entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

URL_entry.place(
    x = 569.5, y = 162,
    width = 268.0,
    height = 49)


key_entry_img = PhotoImage(file = f"image\img_textBox2.png")
key_entry_bg = canvas.create_image(
    703.5, 358.5,
    image = key_entry_img)
# url=path_entry.get()
key_entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

key_entry.place(
    x = 569.5, y = 333,
    width = 268.0,
    height = 49)



img0 = PhotoImage(file = f"image\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = getlink,# use dev functions
    relief = "flat")

b0.place(
    x = 642, y = 471,
    width = 123,
    height = 49)



window.resizable(False, False)
window.mainloop()
