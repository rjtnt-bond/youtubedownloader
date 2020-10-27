'''
Name: Rezwanul islam Bondhon
Gamil: bondhonbondhon342@gamil.com
Facebook: Rezwanul islam Bondhon
Instagram: bondhon_342
'''


'''
code is not work properly
Key Error Name:assets
Date:27/10/2020
'''


from pytube import YouTube
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter import *
from threading import *
from tkinter import ttk


font=('Calibri',14,'bold')

root=Tk()

root.geometry('530x400')
root.minsize(530,400)
root.maxsize(530,400)
root.title('Best YoutubeDownloader')

file_size = 0

def completedownload(stream=None, file_path=None):
    print('Downloaded completed')
    showinfo('Happy ', 'Download completed')
    dwnbutton['text'] = 'DOWNLOAD BUTTON'
    dwnbutton['state'] = 'active'
    urlentry.delete(0,END)

def progressdown(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    dwnbutton['text'] = '{:00.0f}%download '.format(percent)

def startdownload():
    choice = choicebtn.get()
    url = urlentry.get()
    print(url)
    global file_size
    path = askdirectory()
    if path is None:
        showinfo('Error','Your device path not selected')
        return

    try:
        if len(url) > 1:
            yt = YouTube(url)
            try:

                if choice == choics[0]:
                    st= yt.streams.filter(progressive=True).first()

                elif choice == choics[1]:
                    st = yt.streams.filter(progressive=True,file_extension='mp4').last()

                elif choice == choics[2]:
                    st = yt.streams.filter(only_audio=True).first()

            except Exception as e:
                print(e)
                showinfo('Error', 'your select quality not found')

            yt.register_on_complete_callback(completedownload)
            yt.register_on_progress_callback(progressdown)
            file_size=st.filesize
            st.download(output_path=path)

    except Exception as e:
        print(e)
        showinfo('Error','Try again')
        dwnbutton['text'] = 'DOWNLOAD BUTTON'
        dwnbutton['state'] = 'active'
        urlentry.delete(0, END)

def clkbtn():
    try:
        dwnbutton['text'] = 'please wait'
        dwnbutton['state'] = 'disabled'
        thred = Thread(target=startdownload)
        thred.start()

    except Exception as e:
        print(e)

pic=PhotoImage(file='img/img1.png')
headinglabel=Label(root,image=pic)
headinglabel.pack(side=TOP,fill=X)

text=Label(root,text='Enter Url Here:',font=font,bg='dark green',fg='white')
text.pack(side=TOP,fill=X,pady=10,padx=15)

url=StringVar()
urlentry=Entry(root,font=font,justify=CENTER,textvariable=url, relief=SOLID)
urlentry.pack(side=TOP,fill=X,pady=5,padx=15)

text1=Label(root,text='Select Quality',font=font,bg='dark green',fg='white')
text1.pack(side=TOP,pady=10,padx=15)

choics=["720p","480p","Only Audio"]
choicebtn=ttk.Combobox(root,values=choics)
choicebtn.pack(side=TOP,pady=8,padx=10)

dwnbutton=Button(root,text='DOWNLOAD BUTTON',bg='dark red',fg='white',font=('Calibri',12,'bold'),relief=SUNKEN,width=15,padx=20,command=clkbtn)
dwnbutton.pack(side=TOP,pady=30,padx=20)

root.mainloop()

'''Note:
cipher' issue is resloved.
Go to  pytube folder under that open  extract.py.
In line no 301 replace the code with this code:parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats).
Now you can download any video
'''
