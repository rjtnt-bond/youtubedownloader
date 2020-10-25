from pytube import YouTube
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter import *
from threading import *
file_size=0

def startdownload(url):
    global file_size
    path=askdirectory()
    if path is None:
        return
    try:
        yt=YouTube(url)
        st=yt.streams.first()
        file_size=st.filesize
        st.download(output_path=path)
        showinfo('d','dowenload complet')
    except Exception as e:
        print(e)
def clkbtn():
    try:
       dwnbutton['text']='please wait'
       url=urlentry.get()
       if url=='':
           return
       print(url)
       thred=Thread(target=startdownload,args=(url,))
       thred.start()
    except Exception as e:
        print(e)
font=('Calibri',18,'bold')
root=Tk()
root.geometry('600x500')
urlentry=Entry(root,font=font,justify=CENTER)
urlentry.pack(side=TOP,fill=X,pady=50,padx=10)
urlentry.focus()
dwnbutton=Button(root,text='Download Button',font=font,command=clkbtn)
dwnbutton.pack(side=TOP,pady=20,padx=20)
root.mainloop()
