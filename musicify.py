from tkinter import *
import customtkinter as ctk
from  customtkinter import CTkImage
from PIL import Image,ImageTk
import random
import time
import pygame
import os
import shutil
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  
root=ctk.CTk()
root.geometry("800x600")
root.iconbitmap("im//jwrld.ico")
root.title("Music app by SG")
canvas=Canvas(root,width=469,height=480)
canvas.pack()
im1=PhotoImage(file="im//jwrld.png")
im2=PhotoImage(file="im//em.png")
im3=PhotoImage(file="im//jwrld2.png")
im4=PhotoImage(file="im//black.png")
im5=PhotoImage(file="im//emicon.png")
im6=PhotoImage(file="im//jwrld3.png")
sett=PhotoImage(file="im//settings.png")
pl=PhotoImage(file="im//play.png")
pa=PhotoImage(file="im//pause.png")
sk=PhotoImage(file="im//skip.png")
se=PhotoImage(file="im//search.png")
#jimage=PhotoImage(file="im//jwrld_1.png")
eimage=PhotoImage(file="im//em_1.png")
ai_im=canvas.create_image(0,0,image=im1,anchor=NW)
im7=PhotoImage(file="im//other.png")
im8=PhotoImage(file="im//fav.png")
im9=PhotoImage(file="im//rap.png")
im10=PhotoImage(file="im//pop.png")
im11=PhotoImage(file="im//rock.png")
im12=PhotoImage(file="im//rap2.png")
pygame.init()
pygame.mixer.init()
x=False
xy=0
nu=""
ju=""
nz=0
z=0
ru=""
fu=""
bu=""
pu=''
rou=''
rap=[]
rap2=[]
jw=[]
jw2=[]
playlist=[]
playlist2=[]
favs=[]
favs2=[]
be=[]
be2=[]
pop=[]
pop2=[]
rock=[]
rock2=[]
al=[]

def al__l():
     global al
     path="allsongs"
     d=os.listdir(path)
     for i in d:
            al.append(i)
     return al
def j_j():
     global jw,jw2
     path="allsongs"
     d=os.listdir(path)
     for i in d:
            i="allsongs//"+i
            jw.append(i)
            jw2.append(i)
     return jw,jw2
def q():
        global rap,rap2
        path="allsongs"
        d=os.listdir(path)
        for i in d:
            i="allsongs//"+i
            rap.append(i)
            rap2.append(i)
        return rap,rap2
def e():
       global playlist,playlist2
       path="allsongs"
       d=os.listdir(path)
       for i in d:
            i="allsongs//"+i
            playlist.append(i)
            playlist2.append(i) 
       return playlist,playlist2
def f():
       global favs,favs2
       try:
            path="favourites"
            d=os.listdir(path)
            for i in d:
                 i="favourites//"+i
                 favs.append(i)
                 favs2.append(i) 
            return favs,favs2
       except FileNotFoundError:
            pass
def bil():
       global be,be2
       path="allsongs"
       d=os.listdir(path)
       for i in d:
            i="allsongs//"+i
            be.append(i)
            be2.append(i) 
       return be,be2
def p():
       global pop,pop2
       path="allsongs"
       d=os.listdir(path)
       for i in d:
            i="allsongs//"+i
            pop.append(i)
            pop2.append(i) 
       return pop,pop2
def ro():
       global rock,rock2
       path="allsongs"
       d=os.listdir(path)
       for i in d:
            i="allsongs//"+i
            rock.append(i)
            rock2.append(i) 
       return rock,rock2
def setting():
        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("green")  
        root4=ctk.CTk()
        root4.geometry("400x200")
        root4.iconbitmap("im//jwrld.ico")
        root4.title("Settings")
        def sound(a):
            a=a*0.1
            pygame.mixer.music.set_volume(a)
        def dev():
                ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
                ctk.set_default_color_theme("green")  
                root45=ctk.CTk()
                root45.geometry("400x400")
                root45.iconbitmap("im//jwrld.ico")
                root45.title("About developer")
                lab__1 = ctk.CTkLabel(root45, text="This app is copyrighted by Shaunak Ghose."+"\n"+"Any illegal actions may cause your death."+"\n"+ "Contact me @gshaunak18march@gmail.com",compound="right", width=2)
                lab__1.place(relx=0, rely=0.1, anchor=NW)
                root45.mainloop()
        b=ctk.CTkButton(master=root4,text="About developer",width=0.1,height=0.1,command=dev)
        b.place(relx=0.5, rely=0.2, anchor= CENTER)        
        slider=ctk.CTkSlider(master=root4, from_=0, to=10, command=sound)
        slider.place(relx=0.5, rely=0.5, anchor=CENTER)
        root4.mainloop()
def queue():
        global playlist,nu,playlist2
        #p=["allsongs//Eminem - Lose Yourself.mp3","allsongs//Eminem - Cleanin Out My Closet.mp3","allsongs//Eminem - Godzilla ft. Juice WRLD.mp3","allsongs//Eminem - Like Toy Soldiers.mp3","allsongs//Eminem - Love The Way You Lie ft. Rihanna.mp3","allsongs//Eminem - Mockingbird.mp3","allsongs//Eminem - No Love (Explicit Version) ft. Lil Wayne.mp3","allsongs//Eminem - Not Afraid.mp3","allsongs//Eminem - Rap God.mp3","allsongs//Eminem - Sing For The Moment.mp3","allsongs//Eminem - Stan  ft. Dido.mp3","allsongs//Eminem - The Monster ft. Rihanna.mp3","allsongs//Eminem - The Real Slim Shady.mp3","allsongs//Eminem - The Way I am.mp3","allsongs//Eminem - Till I Collapse.mp3"]
        nu=playlist.pop(0)
        playlist.append(nu) 
        pygame.mixer.music.load(nu)  # Get the first track from the playlist
         # Queue the 2nd song
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        nu=nu.replace("allsongs//","")
        nu=nu.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                                                      "+nu+"                                                                    ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        pygame.mixer.music.play()           # Play the music

        
        while len(playlist)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                 nu=playlist.pop(0)
                 playlist.append(nu)  
                 pygame.mixer.music.load(nu)  # Get the first track from the playlist
                 nu=nu.replace("allsongs//","")
                 nu=nu.replace(".mp3","")
                 pygame.mixer.music.play()
                 lab__1 = ctk.CTkLabel(root, text="                                               "+nu+"                                                                           ",compound="right", width=2)
                 lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                 root.update()
                 pygame.mixer.music.set_endevent ( pygame.USEREVENT )

        
        return playlist,nu

def queue2():
        global jw,ju,jw2
        #j=["allsongs//Juice WRLD - All Girls Are The Same.mp3","allsongs//Juice WRLD - Already Dead.mp3","allsongs//Juice WRLD - Bad Energy.mp3","allsongs//Juice WRLD - Bandit ft. NBA Youngboy.mp3","allsongs//Juice WRLD - Black & White.mp3","allsongs//Juice WRLD - Burn.mp3","allsongs//Juice WRLD - Candles.mp3","allsongs//Juice WRLD - Can't Die.mp3","allsongs//Juice WRLD - Conversations.mp3","allsongs//Juice WRLD - Desire.mp3","allsongs//Juice WRLD - Doom.mp3","allsongs//Juice WRLD - Empty.mp3","allsongs//Juice WRLD - End Of The Road.mp3","allsongs//Juice WRLD - Fast.mp3","allsongs//Juice WRLD - Feel Alone.mp3","allsongs//Juice WRLD - Hear Me Calling.mp3","allsongs//Juice WRLD - Feeling.mp3","allsongs//Juice WRLD - Feline (with Polo G & Trippie Redd).mp3","allsongs//Juice WRLD - Flaws and Sins.mp3","allsongs//Juice WRLD - From My Window.mp3","allsongs//Juice WRLD - I Want It.mp3","allsongs//Juice WRLD - Lean Wit Me.mp3","allsongs//Juice WRLD - Legends.mp3","allsongs//Juice WRLD - Lucid Dreams.mp3","allsongs//Juice WRLD - Make Believe.mp3","allsongs//Juice WRLD - Relocate.mp3","allsongs//Juice WRLD - Rich And Blind.mp3","allsongs//Juice WRLD - Righteous.mp3","allsongs//Juice WRLD - Robbery.mp3","allsongs//Juice WRLD - Rockstar In His Prime.mp3","allsongs//Juice WRLD - Screw Juice.mp3","allsongs//Juice WRLD - Stay High.mp3","allsongs//Juice WRLD - Until The Plug Comes Back Around.mp3","allsongs//Juice WRLD - Wishing Well.mp3","allsongs//Juice WRLD - You Wouldn't Understand.mp3","allsongs//Juice WRLD ft. Halsey - Life's A Mess.mp3","allsongs//Juice WRLD ft. Marshmello - Come & Go.mp3","allsongs//Juice WRLD ft. Marshmello, Polo G & Kid Laroi - Hate The Other Side.mp3","allsongs//Juice WRLD – Wasted (feat. Lil Uzi Vert).mp3","allsongs//Juice WRLD - Titanic.mp3"]
        ju=jw.pop(0)
        jw.append(ju)
        
        pygame.mixer.music.load(ju)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        ju=ju.replace("allsongs//"," ")
        ju=ju.replace(".mp3"," ")
        lab__1 = ctk.CTkLabel(root, text="                                                                     "+ju+"                                                     ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        
        pygame.mixer.music.play()           # Play the music

        running = True
        
        while len(jw)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                      ju=playlist.pop(0)
                      jw.append(ju)  
                      pygame.mixer.music.load(ju)  # Get the first track from the playlist
                      ju=ju.replace("allsongs//","")
                      ju=ju.replace(".mp3","")
                      pygame.mixer.music.play()
                      lab__1 = ctk.CTkLabel(root, text="                                                            "+ju+"                                                              ",compound="right", width=2)
                      lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                      root.update()
                      
                      pygame.mixer.music.set_endevent ( pygame.USEREVENT )

        return jw,ju
        
def queuerap():
        global rap,ru,rap2
        random.shuffle(rap)
        #r=['allsongs//Kendrick Lamar - All The Stars.mp3', 'allsongs//Kendrick Lamar - Count Me Out.mp3', 'allsongs//Kendrick Lamar - Die Hard.mp3', 'allsongs//Kendrick Lamar - Humble.mp3', 'allsongs//Kendrick Lamar - N95.mp3', 'allsongs//Kendrick Lamar - Purple Hearts.mp3', 'allsongs//Kendrick Lamar - Rich Spirit.mp3', 'allsongs//Kendrick Lamar - Silent Hill.mp3', 'allsongs//Kendrick Lamar - United In Grief.mp3', 'allsongs//Lil Mosey - Blueberry Faygo.mp3', 'allsongs//Lil Tecca - Ransom.mp3', 'allsongs//Metro Boomin - Calling.mp3', 'allsongs//Metro Boomin - Space Cadet.mp3', 'allsongs//Mustard - Ballin.mp3', 'allsongs//Post Malone - One Right Now.mp3', 'allsongs//Roddy Ricch - The Box.mp3', 'allsongs//The Weeknd - Starboy.mp3', 'allsongs//Travis Scott - Goosebumps.mp3', 'allsongs//Travis Scott - Highest in the room.mp3', 'allsongs//Travis Scott - Sicko Mode.mp3', 'allsongs//XXXTENTACION - Attention.mp3', 'allsongs//XXXTENTACION - Bad vibes forever.mp3', 'allsongs//XXXTENTACION - Changes.mp3', 'allsongs//XXXTENTACION - Everybody Dies In Their Nightmares.mp3', 'allsongs//XXXTENTACION - Look At Me.mp3', 'allsongs//XXXTENTACION - Moonlight.mp3', 'allsongs//XXXTENTACION - Revenge.mp3', 'allsongs//XXXTENTACION -Sad.mp3', 'allsongs//XXXTENTACION- Hope.mp3']
        ru=rap.pop(0)
        
        rap.append(ru)
        pygame.mixer.music.load(ru)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        ru=ru.replace("allsongs//","")
        ru=ru.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                              "+ru+"                                                                                           ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        pygame.mixer.music.play()           # Play the music

        running = True
        while len(rap)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                       ru=rap.pop(0)
                       rap.append(ru)
                       pygame.mixer.music.load(ru)  # Get the first track from the playlist
                       ru=ru.replace("allsongs//","")
                       ru=ru.replace(".mp3","")
                       pygame.mixer.music.play()
                       lab__1 = ctk.CTkLabel(root, text="                                                                              "+ru+"                                            ",compound="right", width=2)
                       lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                       root.update()
                       
                       pygame.mixer.music.set_endevent ( pygame.USEREVENT )
                    

        
        return rap,ru
def queuefav():
        global favs,fu,favs2
        #r=['allsongs//Kendrick Lamar - All The Stars.mp3', 'allsongs//Kendrick Lamar - Count Me Out.mp3', 'allsongs//Kendrick Lamar - Die Hard.mp3', 'allsongs//Kendrick Lamar - Humble.mp3', 'allsongs//Kendrick Lamar - N95.mp3', 'allsongs//Kendrick Lamar - Purple Hearts.mp3', 'allsongs//Kendrick Lamar - Rich Spirit.mp3', 'allsongs//Kendrick Lamar - Silent Hill.mp3', 'allsongs//Kendrick Lamar - United In Grief.mp3', 'allsongs//Lil Mosey - Blueberry Faygo.mp3', 'allsongs//Lil Tecca - Ransom.mp3', 'allsongs//Metro Boomin - Calling.mp3', 'allsongs//Metro Boomin - Space Cadet.mp3', 'allsongs//Mustard - Ballin.mp3', 'allsongs//Post Malone - One Right Now.mp3', 'allsongs//Roddy Ricch - The Box.mp3', 'allsongs//The Weeknd - Starboy.mp3', 'allsongs//Travis Scott - Goosebumps.mp3', 'allsongs//Travis Scott - Highest in the room.mp3', 'allsongs//Travis Scott - Sicko Mode.mp3', 'allsongs//XXXTENTACION - Attention.mp3', 'allsongs//XXXTENTACION - Bad vibes forever.mp3', 'allsongs//XXXTENTACION - Changes.mp3', 'allsongs//XXXTENTACION - Everybody Dies In Their Nightmares.mp3', 'allsongs//XXXTENTACION - Look At Me.mp3', 'allsongs//XXXTENTACION - Moonlight.mp3', 'allsongs//XXXTENTACION - Revenge.mp3', 'allsongs//XXXTENTACION -Sad.mp3', 'allsongs//XXXTENTACION- Hope.mp3']
        fu=favs.pop(0)
        
        favs.append(fu)
        print(fu)
        pygame.mixer.music.load(fu)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        fu=fu.replace("favourites//","")
        fu=fu.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                              "+fu+"                                                                                           ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        
        pygame.mixer.music.play()           # Play the music

        running = True
        while len(rap)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                       fu=favs.pop(0)
                       favs.append(fu)
                       print(fu)
                       pygame.mixer.music.load(fu)  # Get the first track from the playlist
                       fu=fu.replace("favourites//","")
                       fu=fu.replace(".mp3","")
                       pygame.mixer.music.play()
                       lab__1 = ctk.CTkLabel(root, text="                                                                              "+fu+"                                            ",compound="right", width=2)
                       lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                       
                       root.update()
                       
                       pygame.mixer.music.set_endevent ( pygame.USEREVENT )
                    

        
        return favs,fu
def queueb():
        global be,bu,be2
        random.shuffle(be)
        bu=be.pop(0)
        be.append(bu)
        pygame.mixer.music.load(bu)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        bu=bu.replace("billie//","")
        bu=bu.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                                          "+bu+"                                                                                           ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        pygame.mixer.music.play()           # Play the music

        running = True
        while len(rap)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                       bu=be.pop(0)
                       be.append(bu)
                       pygame.mixer.music.load(bu)  
                       bu=bu.replace("billie//","")
                       bu=bu.replace(".mp3","")
                       lab__1 = ctk.CTkLabel(root, text="                                               "+bu+"                                                                                           ",compound="right", width=2)
                       lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                       pygame.mixer.music.play()
                       root.update()
                       
                       pygame.mixer.music.set_endevent ( pygame.USEREVENT )
                    

        
        return be,bu
def queuepop():
        global pop,pu,pop2
        random.shuffle(pop)
        pu=pop.pop(0)
        pop.append(pu)
        pygame.mixer.music.load(pu)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        pu=pu.replace("pop//","")
        pu=pu.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                                          "+pu+"                                                                                           ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        pygame.mixer.music.play()           # Play the music

        running = True
        while len(rap)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                       pu=pop.pop(0)
                       pop.append(pu)
                       pygame.mixer.music.load(pu)  
                       pu=pu.replace("pop//","")
                       pu=pu.replace(".mp3","")
                       lab__1 = ctk.CTkLabel(root, text="                                               "+pu+"                                                                                           ",compound="right", width=2)
                       lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                       pygame.mixer.music.play()
                       root.update()
                       
                       pygame.mixer.music.set_endevent ( pygame.USEREVENT )
                    

        
        return pop,pu

def queuerock():
        global rock,rou,rock2
        random.shuffle(rock)
        rou=rock.pop(0)
        rock.append(rou)
        pygame.mixer.music.load(rou)  # Get the first track from the playlist
        pygame.mixer.music.set_endevent ( pygame.USEREVENT )# Setup the end track event
        rou=rou.replace("rock//","")
        rou=rou.replace(".mp3","")
        lab__1 = ctk.CTkLabel(root, text="                                          "+rou+"                                                                                           ",compound="right", width=2)
        lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
        pygame.mixer.music.play()           # Play the music

        running = True
        while len(rap)>0:
            root.update()
            for event in pygame.event.get():  
              if event.type == pygame.USEREVENT:# A track has ended
                       rou=rock.pop(0)
                       rock.append(rou)
                       pygame.mixer.music.load(rou)  
                       rou=rou.replace("rock//","")
                       rou=rou.replace(".mp3","")
                       lab__1 = ctk.CTkLabel(root, text="                                               "+rou+"                                                                                           ",compound="right", width=2)
                       lab__1.place(relx=0.35, rely=0.82, anchor= CENTER)
                       pygame.mixer.music.play()
                       root.update()
                       
                       pygame.mixer.music.set_endevent ( pygame.USEREVENT )
                    

        
        return rock,rou
def talk(y):
    engine.say(y)
    engine.runAndWait()
def play1(x):
    
    pygame.mixer.music.load(x)
    pygame.mixer.music.play(loops=0)
def pause1():
    global x
    if x:
        pygame.mixer.music.unpause()
        x=False
        return x
    else:
        pygame.mixer.music.pause()
        x=True
        return x

def start():
    canvas.destroy()
    al__l()
    ro()
    p()
    bil()
    q()
    j_j()
    e()
    f()  
    lab__1 = ctk.CTkLabel(root, text="                                                                                  ",compound="right", width=2)
    lab__1.place(relx=0.5, rely=0.9, anchor= CENTER)
    canvas1=Canvas(root,width=600,height=150)
    canvas1.pack(padx=1,pady=150)
    ent6=ctk.CTkEntry(master=root,placeholder_text="search for a song to add to favourites",width=250,border_width=2,corner_radius=10)
    ent6.place(relx=0.35, rely=0.2, anchor= CENTER)
    def addsong():
          curr=os.getcwd()
          inp=ent6.get()
          for i in curr:
               if i.isalpha():
                    pass
               elif i.isnumeric():
                    pass
               elif i==":":
                    pass
               else:
                    curr=curr.replace(i,"/")
          curr=curr+"/"+"favourites"
          path="allsongs"
          d=os.listdir(path)
          alls=""
          os.system("ytmdl "+inp+" -o "+curr)
          
    b=Button(master=root, image=se, command=addsong)
    b.place(relx=0.5, rely=0.2, anchor= CENTER)
    ai_im=canvas1.create_image(0,0,image=im4,anchor=NW)
    lab__1 = ctk.CTkLabel(root, text="Listen from these options above",compound="right", width=2)
    lab__1.place(relx=0.5, rely=0.7, anchor= CENTER)
    
    def em():
        canvas1.destroy()
        lab__1.destroy()
        bs.destroy()
        canvas2=Canvas(root,width=500,height=380)
        canvas2.pack(padx=1,pady=80)
        lab_1 = ctk.CTkLabel(root, text="                                              ",compound="right", width=2)
        lab_1.place(relx=0.85, rely=0.9, anchor= CENTER)
        lab_1 = ctk.CTkLabel(root, text="                                              ",compound="right", width=2)
        lab_1.place(relx=0.1, rely=0.9, anchor= CENTER)
        ai_im=canvas2.create_image(0,0,image=im4,anchor=NW)
        ai_im=canvas2.create_image(20,10,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,30,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,50,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,70,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,90,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,110,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,130,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,150,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,170,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,190,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,210,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,230,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,250,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,270,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,290,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,310,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,330,image=im5,anchor=NW)
        ai_im=canvas2.create_image(20,350,image=im5,anchor=NW)
        def ly():
            play1("allsongs//Eminem - Lose Yourself.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Eminem - Lose Yourself                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
            
        def c():
            play1("allsongs//Eminem - Cleanin Out My Closet.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Cleanin Out My Closet - Eminem                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
            
        def g():
            play1("allsongs//Eminem - Godzilla ft. Juice WRLD.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                         Eminem - Godzilla ft. Juice WRLD                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
            
        def lts():
            play1("allsongs//Eminem - Like Toy Soldiers.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Like Toy Soldiers                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
            
        def ltw():
            play1("allsongs//Eminem - Love The Way You Lie ft. Rihanna.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                         Eminem - Love The Way You Lie ft. Rihanna                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def m():
            play1("allsongs//Eminem - Mockingbird.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Mockingbird                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def nl():
            play1("allsongs//Eminem - No Love (Explicit Version) ft. Lil Wayne.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - No Love (Explicit Version) ft. Lil Wayne                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def nf():
            play1("allsongs//Eminem - Not Afraid.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Not Afraid                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def rg():
            play1("allsongs//Eminem - Rap God.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Rap God                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def sm():
            play1("allsongs//Eminem - Sing For The Moment.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Sing For The Moment                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def st():
            play1("allsongs//Eminem - Stan  ft. Dido.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Eminem - Stan  ft. Dido                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def mon():
            play1("allsongs//Eminem - The Monster ft. Rihanna.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          The Monster ft. Rihanna                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def ss():
            play1("allsongs//Eminem - The Real Slim Shady.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                           The Real Slim Shady                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def w():
            play1("allsongs//Eminem - The Way I am.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          The Way I am                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def t():
            play1("allsongs//Eminem - Till I Collapse.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                          Till I Collapse by Eminem                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def playem():
            
            pl=["allsongs//Eminem - Lose Yourself.mp3","allsongs//Cleanin Out My Closet - Eminem.mp3","allsongs//Eminem - Godzilla ft. Juice WRLD.mp3","allsongs//Eminem - Like Toy Soldiers.mp3","allsongs//Eminem - Love The Way You Lie ft. Rihanna.mp3","allsongs//Eminem - No Love (Explicit Version) ft. Lil Wayne.mp3","allsongs//Eminem - Not Afraid.mp3","allsongs//Eminem - Rap God.mp3","allsongs//Eminem - Sing For The Moment.mp3","allsongs//Eminem - Stan  ft. Dido.mp3","allsongs//Eminem - The Monster ft. Rihanna.mp3","allsongs//Eminem - The Real Slim Shady.mp3","allsongs//Eminem - The Way I am.mp3","allsongs//Till I Collapse by Eminem.mp3"]
            queue()
            
        def next1():
           
           queue()
           
            
        b=ctk.CTkButton(master=canvas2, text="Eminem - Lose Yourself                                   ", command=ly,width=2,height=1,)
        b.place(relx=0.33, rely=0.065, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Cleanin Out My Closet - Eminem                   ", command=c,width=2,height=1,)
        b.place(relx=0.33, rely=0.13, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Godzilla ft. Juice WRLD                  ", command=g,width=2,height=1,)
        b.place(relx=0.34, rely=0.195, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Like Toy Soldiers                        ", command=lts,width=2,height=1,)
        b.place(relx=0.32, rely=0.26, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Love The Way You Lie ft. Rihanna", command=ltw,width=2,height=1,)
        b.place(relx=0.34, rely=0.325, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Mockingbird                                  ", command=m,width=2,height=1,)
        b.place(relx=0.33, rely=0.385, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - No Love (Explicit Version) ft. Lil Wayne", command=nl,width=2,height=1,)
        b.place(relx=0.36, rely=0.45, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Not Afraid                                            ", command=nf,width=2,height=1,)
        b.place(relx=0.34, rely=0.515, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Rap God                                                   ", command=rg,width=2,height=1,)
        b.place(relx=0.35, rely=0.57, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Sing For The Moment                           ", command=sm,width=5,height=2,)
        b.place(relx=0.35, rely=0.635, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - Stan  ft. Dido                                      ", command=st,width=5,height=2,)
        b.place(relx=0.35, rely=0.69, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - The Monster ft. Rihanna                      ", command=mon,width=5,height=2,)
        b.place(relx=0.35, rely=0.755, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - The Real Slim Shady                          ", command=ss,width=5,height=2,)
        b.place(relx=0.35, rely=0.82, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Eminem - The Way I am                                           ", command=w,width=5,height=2,)
        b.place(relx=0.35, rely=0.88, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Till I Collapse by Eminem                                   ", command=t,width=5,height=2,)
        b.place(relx=0.35, rely=0.94, anchor= CENTER)
        b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=playem)
        b5.place(relx=0.45, rely=0.965, anchor= CENTER)
        b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
        b6.place(relx=0.5, rely=0.965, anchor= CENTER)
        b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=next1)
        b7.place(relx=0.55, rely=0.965, anchor= CENTER)
        def home():
                canvas2.destroy()
                b5.destroy()
                lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                start()
        b=ctk.CTkButton(master=root,text="HOME",command=home)
        b.place(relx=0.8, rely=0.1, anchor= CENTER)
    bem=Button(master=canvas1,image=im2,width=0.1,height=0.1, command=em)
    bem.place(relx=0.125, rely=0.5, anchor= CENTER)
    def juice():
        canvas1.destroy()
        lab__1.destroy()
        canvas2=Canvas(root,width=500,height=420)
        canvas2.pack(padx=0,pady=0)
        ai_im=canvas2.create_image(0,0,image=im4,anchor=NW)
        ai_im=canvas2.create_image(0,10,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,30,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,50,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,70,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,90,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,110,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,130,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,150,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,170,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,190,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,210,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,230,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,250,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,270,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,290,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,310,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,330,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,350,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,370,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,390,image=im6,anchor=NW)
        ai_im=canvas2.create_image(0,410,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,0,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,10,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,30,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,50,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,70,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,90,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,110,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,130,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,150,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,170,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,190,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,210,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,230,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,250,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,270,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,290,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,310,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,330,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,350,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,370,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,390,image=im6,anchor=NW)
        ai_im=canvas2.create_image(250,410,image=im6,anchor=NW)
        def s1():
            play1("allsongs//Juice WRLD - All Girls Are The Same.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - All Girls Are The Same                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s2():
            play1("allsongs//Juice WRLD - Already Dead.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Already Dead                                                                   ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s3():
            play1("allsongs//Juice WRLD - Bad Energy.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Bad Energy                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s4():
            play1("allsongs//Juice WRLD - Bandit ft. NBA Youngboy.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Bandit ft. NBA Youngboy                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s5():
            play1("allsongs//Juice WRLD - Black & White.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Black & White                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s6():
            play1("allsongs//Juice WRLD - Burn.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Burn                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s7():
            play1("allsongs//Juice WRLD - Candles.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Candles                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s8():
            play1("allsongs//Juice WRLD - Can't Die.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Can't Die                                                                ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s9():
            play1("allsongs//Juice WRLD - Conversations.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Conversations                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s10():
            play1("allsongs//Juice WRLD - Desire.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Desire                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s11():
            play1("allsongs//Juice WRLD - Empty.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Empty                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s12():
            play1("allsongs//Juice WRLD - End Of The Road.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - End Of The Road                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s13():
            play1("allsongs//Juice WRLD - Fast.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Fast                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s14():
            play1("allsongs//Juice WRLD - Feel Alone.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Feel Alone                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s15():
            play1("allsongs//Juice WRLD - Hear Me Calling.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Hear Me Calling                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s16():
            play1("allsongs//Juice WRLD - Feeling.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Feeling                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s17():
            play1("allsongs//Juice WRLD - Feline (with Polo G & Trippie Redd).mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Feline (with Polo G & Trippie Redd)                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s18():
            play1("allsongs//Juice WRLD - Flaws and Sins.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Flaws and Sins                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s19():
            play1("allsongs//Juice WRLD - From My Window.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - From My Window                                                                  ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s20():
            play1("allsongs//Juice WRLD - I Want It.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - I Want It                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s21():
            play1("allsongs//Juice WRLD - Lean Wit Me.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Lean Wit Me                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s22():
            play1("allsongs//Juice WRLD - Legends.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Legends                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s23():
            play1("allsongs//Juice WRLD - Lucid Dreams.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Lucid Dreams                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s24():
            play1("allsongs//Juice WRLD - Make Believe.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Make Believe                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s25():
            play1("allsongs//Juice WRLD - Relocate.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Relocate                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s26():
            play1("allsongs//Juice WRLD - Rich And Blind.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Rich And Blind                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s27():
            play1("allsongs//Juice WRLD - Righteous.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Righteous                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s28():
            play1("allsongs//Juice WRLD - Robbery.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Robbery                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s29():
            play1("allsongs//Juice WRLD - Rockstar In His Prime.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Rockstar In His Prime                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s30():
            play1("allsongs//Juice WRLD - Screw Juice.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Screw Juice                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s31():
            play1("allsongs//Juice WRLD - Stay High.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Stay High                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s32():
            play1("allsongs//Juice WRLD - Until The Plug Comes Back Around.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Until The Plug Comes Back Around                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s33():
            play1("allsongs//Juice WRLD - Wishing Well.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - Wishing Well                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s34():
            play1("allsongs//Juice WRLD - You Wouldn't Understand.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD - You Wouldn't Understand                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s35():
            play1("allsongs//Juice WRLD ft. Halsey - Life's A Mess.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD ft. Halsey - Life's A Mess                                                                ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s36():
            play1("allsongs//Juice WRLD ft. Marshmello - Come & Go.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD ft. Marshmello - Come & Go                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s37():
            play1("allsongs//Juice WRLD ft. Marshmello, Polo G & Kid Laroi - Hate The Other Side.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD ft. Marshmello, Polo G & Kid Laroi - Hate The Other Side                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s38():
            play1("allsongs//Juice WRLD – Wasted (feat. Lil Uzi Vert).mp3")
            lab__1 = ctk.CTkLabel(root, text="                                            Juice WRLD – Wasted (feat. Lil Uzi Vert)                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def s39():
            play1("allsongs//Juice WRLD - Titanic.mp3")
            lab__1 = ctk.CTkLabel(root, text="                                           Juice WRLD – Titanic                                                                 ",compound="right", width=2)
            lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
        def playju():
            queue2()
        def next2():
           queue2()
        def home():
                canvas2.destroy()
                b5.destroy()
                lab__1 = ctk.CTkLabel(root, text="                                                                                                                    ",compound="right", width=2)
                lab__1.place(relx=0.85, rely=0.1, anchor= CENTER)
                start()
        b=ctk.CTkButton(master=root,text="HOME",command=home)
        b.place(relx=0.91, rely=0.1, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - All Girls Are The Same", command=s1,width=2,height=1,)
        b.place(relx=0.26, rely=0.04, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Already Dead                ", command=s2,width=2,height=1,)
        b.place(relx=0.26, rely=0.095, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Bad Energy                    ", command=s3,width=2,height=1,)
        b.place(relx=0.26, rely=0.15, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Bandit ft. NBA Youngboy", command=s4,width=2,height=1,)
        b.place(relx=0.28, rely=0.2, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Black & White                ", command=s5,width=2,height=1,)
        b.place(relx=0.26, rely=0.25, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Burn                               ", command=s6,width=2,height=1,)
        b.place(relx=0.26, rely=0.3, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Candles                              ", command=s7,width=2,height=1,)
        b.place(relx=0.26, rely=0.35, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Can't Die                               ", command=s8,width=2,height=1,)
        b.place(relx=0.26, rely=0.4, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Conversations                     ", command=s9,width=2,height=1,)
        b.place(relx=0.26, rely=0.45, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Desire                               ", command=s10,width=2,height=1,)
        b.place(relx=0.26, rely=0.5, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Empty                               ", command=s11,width=2,height=1,)
        b.place(relx=0.26, rely=0.55, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - End Of The Road              ", command=s12,width=2,height=1,)
        b.place(relx=0.26, rely=0.6, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Fast                                 ", command=s13,width=2,height=1,)
        b.place(relx=0.26, rely=0.65, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Feel Alone                   ", command=s14,width=2,height=1,)
        b.place(relx=0.26, rely=0.7, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Hear Me Calling              ", command=s15,width=2,height=1,)
        b.place(relx=0.26, rely=0.75, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Feeling                             ", command=s16,width=2,height=1,)
        b.place(relx=0.26, rely=0.8, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Feline                          ", command=s17,width=2,height=1,)
        b.place(relx=0.26, rely=0.85, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Flaws and Sins               ", command=s18,width=2,height=1,)
        b.place(relx=0.26, rely=0.90, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - From My Window       ", command=s19,width=2,height=1,)
        b.place(relx=0.26, rely=0.95, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - I Want It          ", command=s20,width=2,height=1,)
        b.place(relx=0.72, rely=0.04, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Lean Wit Me      ", command=s21,width=2,height=1,)
        b.place(relx=0.72, rely=0.095, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Legends          ", command=s22,width=2,height=1,)
        b.place(relx=0.72, rely=0.15, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Lucid Dreams     ", command=s23,width=2,height=1,)
        b.place(relx=0.72, rely=0.2, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Make Believe     ", command=s24,width=2,height=1,)
        b.place(relx=0.72, rely=0.25, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Relocate          ", command=s25,width=2,height=1,)
        b.place(relx=0.72, rely=0.3, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Rich And Blind    ", command=s26,width=2,height=1,)
        b.place(relx=0.72, rely=0.3, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Righteous    ", command=s27,width=2,height=1,)
        b.place(relx=0.72, rely=0.35, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Robbery    ", command=s28,width=2,height=1,)
        b.place(relx=0.72, rely=0.4, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Rockstar In His Prime", command=s29,width=2,height=1,)
        b.place(relx=0.76, rely=0.45, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Screw Juice ", command=s30,width=2,height=1,)
        b.place(relx=0.72, rely=0.5, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Stay High    ", command=s31,width=2,height=1,)
        b.place(relx=0.72, rely=0.55, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Until The Plug.....", command=s32,width=2,height=1,)
        b.place(relx=0.72, rely=0.6, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - Wishing Well    ", command=s33,width=2,height=1,)
        b.place(relx=0.72, rely=0.65, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD - You Wouldn't Understand", command=s34,width=2,height=1,)
        b.place(relx=0.75, rely=0.7, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD ft. Halsey - Life's A Mess", command=s35,width=2,height=1,)
        b.place(relx=0.75, rely=0.75, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD ft. Marshmello - Come & Go", command=s36,width=2,height=1,)
        b.place(relx=0.75, rely=0.8, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD Hate The Other Side", command=s37,width=2,height=1,)
        b.place(relx=0.72, rely=0.85, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD – Wasted (feat. Lil Uzi Vert)", command=s38,width=2,height=1,)
        b.place(relx=0.75, rely=0.9, anchor= CENTER)
        b=ctk.CTkButton(master=canvas2, text="Juice WRLD – Titanic              ", command=s39,width=2,height=1,)
        b.place(relx=0.75, rely=0.95, anchor= CENTER)
        b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=playju)
        b5.place(relx=0.45, rely=0.965, anchor= CENTER)
        b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
        b6.place(relx=0.5, rely=0.965, anchor= CENTER)
        b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=next2)
        b7.place(relx=0.55, rely=0.965, anchor= CENTER)
    ju=Button(master=canvas1, image=im3,width=0.1,height=0.1,  command=juice)
    ju.place(relx=0.37, rely=0.5, anchor= CENTER)
    def more():
        ctk.set_default_color_theme("blue")  
        canvas1.destroy()
        lab__1.destroy()
        canvas2=Canvas(root,width=775,height=208)
        canvas2.pack(padx=0,pady=100)
        ai_im=canvas2.create_image(0,0,image=im4,anchor=NW)
        lab__5 = ctk.CTkLabel(root, text="More genres will be added later.",compound="right", width=2)
        lab__5.place(relx=0.35, rely=0.6, anchor= CENTER)
        def home():
                canvas2.destroy()
                lab__5.destroy()
                lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                start()
        bh=ctk.CTkButton(master=root,text="HOME",command=home)
        bh.place(relx=0.8, rely=0.1, anchor= CENTER)
        def rap():
                canvas2.destroy()
                lab__5.destroy()
                bh.destroy()
                canvas20=Canvas(root,width=670,height=208)
                canvas20.pack(padx=0,pady=100)
                ai_im=canvas20.create_image(0,0,image=im4,anchor=NW)
                ai_im=canvas20.create_image(10,0,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,25,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,50,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,75,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,100,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,125,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,150,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,170,image=im12,anchor=NW)
                ai_im=canvas20.create_image(10,190,image=im12,anchor=NW)
                def playr():
                    queuerap()
                def skip():
                   queuerap()
                b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=playr)
                b5.place(relx=0.45, rely=0.965, anchor= CENTER)
                b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
                b6.place(relx=0.5, rely=0.965, anchor= CENTER)
                b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=skip)
                b7.place(relx=0.55, rely=0.965, anchor= CENTER)
                def r1():
                      play1("allsongs//Travis Scott - Goosebumps.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Travis Scott - Goosebumps                                                                   ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r2():
                      play1("allsongs//Roddy Ricch - The Box.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Roddy Ricch - The Box                                                                   ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r3():
                      play1("allsongs//Post Malone - One Right Now.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Post Malone - One Right Now                                                                 ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r4():
                      play1("allsongs//Kendrick Lamar - All The Stars.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - All The Stars                                                                   ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r5():
                      play1("allsongs//Kendrick Lamar - Count Me Out.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Count Me Out                                                                   ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r6():
                      play1("allsongs//Kendrick Lamar - Die Hard.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Die Hard                                                           ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r7():
                      play1("allsongs//Kendrick Lamar - Humble.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Humble                                                            ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r8():
                      play1("allsongs//Kendrick Lamar - N95.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - N95                                                                 ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r9():
                      play1("allsongs//Kendrick Lamar - Purple Hearts.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Purple Hearts                                                                 ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r10():
                      play1("allsongs//Kendrick Lamar - Rich Spirit.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Rich Spirit                                                                 ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def r11():
                      play1("allsongs//Kendrick Lamar - Silent Hill.mp3")
                      lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - Silent Hill                                                               ",compound="right", width=2)
                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                def home():
                        canvas20.destroy()
                        bnxt.place_forget()
                        b5.place_forget()
                        b7.place_forget()
                        
                        
                        lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                        lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                        start()
                def pg2():
                      canvas20.destroy()
                      canvas21=Canvas(root,width=670,height=208)
                      canvas21.pack(padx=0,pady=100)
                      ai_im=canvas21.create_image(0,0,image=im4,anchor=NW)
                      ai_im=canvas21.create_image(10,0,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,25,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,50,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,75,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,100,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,125,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,150,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,170,image=im12,anchor=NW)
                      ai_im=canvas21.create_image(10,190,image=im12,anchor=NW)
                      def home():
                        canvas21.destroy()
                        bnxt.place_forget()
                        b5.place_forget()
                        b7.place_forget()
                        lab__1 = ctk.CTkLabel(root, text="                                ",compound="right", width=2)
                        lab__1.place(relx=0.4, rely=0.6, anchor= CENTER)
                        lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                        lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                        start()
                      def r12():
                              play1("allsongs//Kendrick Lamar - United In Grief.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Kendrick Lamar - United In Grief                                                          ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r13():
                              play1("allsongs//Lil Mosey - Blueberry Faygo.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Lil Mosey - Blueberry Faygo                                                            ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r14():
                              play1("allsongs//Lil Tecca - Ransom.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Lil Tecca - Ransom                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r15():
                              play1("allsongs//Metro Boomin - Calling.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Metro Boomin - Calling                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r16():
                              play1("allsongs//Metro Boomin - Space Cadet.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Metro Boomin - Space Cadet                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r17():
                              play1("allsongs//Mustard - Ballin.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Mustard - Ballin                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r18():
                              play1("allsongs//Post Malone - One Right Now.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Post Malone - One Right Now                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r19():
                              play1("allsongs//XXXTENTACION - Attention.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Attention                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r20():
                              play1("allsongs//The Weeknd - Starboy.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          The Weeknd - Starboy                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r21():
                              play1("allsongs//Travis Scott - Highest in the room.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Travis Scott - Highest in the room                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def r22():
                              play1("allsongs//Travis Scott - Sicko Mode.mp3")
                              lab__1 = ctk.CTkLabel(root, text="                                          Travis Scott - Sicko Mode                                                               ",compound="right", width=2)
                              lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                      def pg3():
                              canvas21.destroy()
                              bnxt=ctk.CTkLabel(master=root,text="        ")
                              bnxt.place(relx=0.4, rely=0.6, anchor= CENTER)
                              canvas22=Canvas(root,width=670,height=208)
                              canvas22.pack(padx=0,pady=100)
                              ai_im=canvas22.create_image(0,0,image=im4,anchor=NW)
                              ai_im=canvas22.create_image(10,0,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,25,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,50,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,75,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,100,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,125,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,150,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,170,image=im12,anchor=NW)
                              ai_im=canvas22.create_image(10,190,image=im12,anchor=NW)
                              def home():
                                canvas22.destroy()
                                bnxt.destroy()
                                lab__1 = ctk.CTkLabel(root, text="       ",compound="right", width=2)
                                lab__1.place(relx=0.4, rely=0.6, anchor= CENTER)
                                b5.destroy()
                                b7.destroy()
                                lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                                lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                                start()
                              def r23():
                                      play1("allsongs//XXXTENTACION - Bad vibes forever.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Bad vibes forever                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r24():
                                      play1("allsongs//XXXTENTACION - Changes.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Changes                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r25():
                                      play1("allsongs//XXXTENTACION - Everybody Dies In Their Nightmares.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Everybody Dies In Their Nightmares                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r26():
                                      play1("rap/XXXTENTACION - Look At Me.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Look At Me                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r27():
                                      play1("allsongs//XXXTENTACION - Moonlight.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Moonlight                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r28():
                                      play1("allsongs//XXXTENTACION- Hope.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION- Hope                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)
                              def r29():
                                      play1("allsongs//XXXTENTACION - Sad.mp3")
                                      lab__1 = ctk.CTkLabel(root, text="                                          XXXTENTACION - Bad vibes forever                                                               ",compound="right", width=2)
                                      lab__1.place(relx=0.4, rely=0.82, anchor= CENTER)   
                              b=ctk.CTkButton(master=root,text="HOME",command=home)
                              b.place(relx=0.8, rely=0.1, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="The Weeknd - Starboy",width=0.1,height=0.1,command=r20)
                              b.place(relx=0.23, rely=0.07, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="Travis Scott - Highest in the room",width=0.1,height=0.1,command=r21)
                              b.place(relx=0.23, rely=0.15, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="Travis Scott - Sicko Mode",width=0.1,height=0.1,command=r22)
                              b.place(relx=0.23, rely=0.25, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION - Bad vibes forever",width=0.1,height=0.1,command=r23)
                              b.place(relx=0.28, rely=0.35, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION - Changes",width=0.1,height=0.1,command=r24)
                              b.place(relx=0.23, rely=0.45, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION - Everybody Dies In Their Nightmares",width=0.1,height=0.1,command=r25)
                              b.place(relx=0.35, rely=0.55, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION - Look At Me",width=0.1,height=0.1,command=r26)
                              b.place(relx=0.23, rely=0.65, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION - Moonlight",width=0.1,height=0.1,command=r27)
                              b.place(relx=0.23, rely=0.75, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="XXXTENTACION- Hope",width=0.1,height=0.1,command=r28)
                              b.place(relx=0.23, rely=0.85, anchor= CENTER)
                              b=ctk.CTkButton(master=canvas22,text="The Weeknd - Starboy",width=0.1,height=0.1,command=r29)
                              b.place(relx=0.23, rely=0.95, anchor= CENTER)
                              
                      b=ctk.CTkButton(master=canvas21,text="Kendrick Lamar - Silent Hill",width=0.1,height=0.1,command=r11)
                      b.place(relx=0.23, rely=0.07, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Kendrick Lamar - United In Grief",width=0.1,height=0.1,command=r12)
                      b.place(relx=0.23, rely=0.15, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Lil Mosey - Blueberry Faygo",width=0.1,height=0.1,command=r13)
                      b.place(relx=0.23, rely=0.25, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Lil Tecca - Ransom",width=0.1,height=0.1,command=r14)
                      b.place(relx=0.23, rely=0.35, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Metro Boomin - Calling",width=0.1,height=0.1,command=r15)
                      b.place(relx=0.23, rely=0.45, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Metro Boomin - Space Cadet",width=0.1,height=0.1,command=r16)
                      b.place(relx=0.23, rely=0.55, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Mustard - Ballin",width=0.1,height=0.1,command=r17)
                      b.place(relx=0.23, rely=0.65, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="Post Malone - One Right Now",width=0.1,height=0.1,command=r18)
                      b.place(relx=0.23, rely=0.75, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="XXXTENTACION - Attention",width=0.1,height=0.1,command=r19)
                      b.place(relx=0.23, rely=0.85, anchor= CENTER)
                      b=ctk.CTkButton(master=canvas21,text="The Weeknd - Starboy",width=0.1,height=0.1,command=r20)
                      b.place(relx=0.23, rely=0.95, anchor= CENTER)
                      b=ctk.CTkButton(master=root,text="HOME",command=home)
                      b.place(relx=0.8, rely=0.1, anchor= CENTER)
                      bnxt=ctk.CTkButton(master=root,text="3",width=0.1,height=0.1,command=pg3)
                      bnxt.place(relx=0.4, rely=0.6, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Travis Scott - Goosebumps",width=0.1,height=0.1,command=r1)
                b.place(relx=0.23, rely=0.07, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Roddy Ricch - The Box         ",width=0.1,height=0.1,command=r2)
                b.place(relx=0.23, rely=0.17, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Post Malone - One Right Now",width=0.1,height=0.1,command=r3)
                b.place(relx=0.23, rely=0.27, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - All The Stars",width=0.1,height=0.1,command=r4)
                b.place(relx=0.23, rely=0.37, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - Count Me Out",width=0.1,height=0.1,command=r5)
                b.place(relx=0.23, rely=0.47, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - Die Hard ",width=0.1,height=0.1,command=r6)
                b.place(relx=0.23, rely=0.57, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - Humble       ",width=0.1,height=0.1,command=r7)
                b.place(relx=0.23, rely=0.67, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - N95          ",width=0.1,height=0.1,command=r8)
                b.place(relx=0.23, rely=0.77, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - Purple Hearts",width=0.1,height=0.1,command=r9)
                b.place(relx=0.23, rely=0.86, anchor= CENTER)
                b=ctk.CTkButton(master=canvas20,text="Kendrick Lamar - Rich Spirit",width=0.1,height=0.1,command=r10)
                b.place(relx=0.23, rely=0.95, anchor= CENTER)
                bnxt=ctk.CTkButton(master=root,text="2",width=0.1,height=0.1,command=pg2)
                bnxt.place(relx=0.4, rely=0.6, anchor= CENTER)
                
                b=ctk.CTkButton(master=root,text="HOME",command=home)
                b.place(relx=0.8, rely=0.1, anchor= CENTER)
        def pop():
                canvas2.destroy()
                lab__5.destroy()
                bh.destroy()
                canvas20=Canvas(root,width=670,height=208)
                canvas20.pack(padx=0,pady=100)
                
                ai_im=canvas20.create_image(0,0,image=im4,anchor=NW)
                def bl():
                     canvas20.destroy()
                     canvas29=Canvas(root,width=670,height=208,bg="black")
                     canvas29.pack(padx=0,pady=100)
                     def skip():
                        queueb()
                     b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=queueb)
                     b5.place(relx=0.45, rely=0.965, anchor= CENTER)
                     def home():
                        canvas29.destroy()
                        b5.destroy()
                        lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                        lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                        start()
                     b=ctk.CTkButton(master=root,text="HOME",command=home)
                     b.place(relx=0.8, rely=0.1, anchor= CENTER)
                     b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
                     b6.place(relx=0.5, rely=0.965, anchor= CENTER)
                     b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=skip)
                     b7.place(relx=0.55, rely=0.965, anchor= CENTER)
                def home():
                        canvas20.destroy()
                        """b5.destroy()
                        b7.destroy()
                        b8.destroy()"""
                        
                        lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                        lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                        start()
                b=ctk.CTkButton(master=root,text="HOME",command=home)
                b.place(relx=0.8, rely=0.1, anchor= CENTER)
                def oth():
                     canvas20.destroy()
                     canvas29=Canvas(root,width=670,height=208,bg="black")
                     canvas29.pack(padx=0,pady=100)
                     ai_im=canvas29.create_image(300,10,image=im10,anchor=NW)
                     def skip():
                        queuepop()
                     b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=queuepop)
                     b5.place(relx=0.45, rely=0.965, anchor= CENTER)
                     def home():
                        canvas29.destroy()
                        b5.destroy()
                        lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                        lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                        start()
                     b=ctk.CTkButton(master=root,text="HOME",command=home)
                     b.place(relx=0.8, rely=0.1, anchor= CENTER)
                     b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
                     b6.place(relx=0.5, rely=0.965, anchor= CENTER)
                     b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=skip)
                     b7.place(relx=0.55, rely=0.965, anchor= CENTER)
                b=Button(master=canvas20,image=im10,command=oth)
                b.place(relx=0.85, rely=0.5, anchor= CENTER)
        def rock():
               canvas2.destroy()
               lab__5.destroy()
               bh.destroy()
               canvas20=Canvas(root,width=670,height=208)
               canvas20.pack(padx=0,pady=100)
               ai_im=canvas20.create_image(0,0,image=im4,anchor=NW)
               ai_im=canvas20.create_image(200,0,image=im11,anchor=NW)
               def skip():
                    queuerock()
               b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=queuerock)
               b5.place(relx=0.45, rely=0.965, anchor= CENTER)
               def home():
                    canvas20.destroy()
                    b5.destroy()
                    lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                    lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                    start()
               b=ctk.CTkButton(master=root,text="HOME",command=home)
               b.place(relx=0.8, rely=0.1, anchor= CENTER)
               b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
               b6.place(relx=0.5, rely=0.965, anchor= CENTER)
               b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=skip)
               b7.place(relx=0.55, rely=0.965, anchor= CENTER)
                
        b=Button(master=canvas2,image=im9, width=0,height=0.1,command=rap)
        b.place(relx=0.237, rely=0.5, anchor= CENTER)
        b=Button(master=canvas2,image=im10, width=0,height=0.1,command=pop)
        b.place(relx=0.597, rely=0.5, anchor= CENTER)
        b=Button(master=canvas2,image=im11, width=0,height=0.1,command=rock)
        b.place(relx=0.86, rely=0.5, anchor= CENTER)
    def favs():
          try:
             d=os.listdir("favourites/")
             canvas1.destroy()
             lab__1.destroy()
             bs.destroy()
             canvasf=Canvas(root,width=750,height=350,bg="black")
             canvasf.place(relx=0.5,rely=0.45,anchor=CENTER)
             ent5=ctk.CTkEntry(master=canvasf,placeholder_text="search for a song to add to favourites",width=300,border_width=2,corner_radius=10)
             ent5.place(relx=0.25, rely=0.1, anchor= CENTER)
             ent6=ctk.CTkEntry(master=canvasf,placeholder_text="search for your favourite song to check if its in your favourites",width=370,border_width=2,corner_radius=10)
             ent6.place(relx=0.7, rely=0.1, anchor= CENTER)
             def sea():
                song=ent5.get()
                song=song.capitalize()
                song=song.replace(" ","")
                m=os.listdir("allsongs/")
                ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
                ctk.set_default_color_theme("green")  
                root56=ctk.CTk()
                root56.geometry("400x450")
                root56.iconbitmap("im//jwrld.ico")
                root56.title("Search results")
                xy=[]
                
                for d in m:
                     i=d
                     i=i.replace(" ","")
                     n=""
                     if "-" in i:
                          x=i.index("-")
                     for y in range(x+1):
                          n=n+i[y]
                     i=i.replace(n,"")
                     i=i.capitalize()
                     
                     if len(song)>0:
                          if song in i:
                               
                               xy.append(d)
                          else:
                               lab_1 = ctk.CTkButton(root56, text="song not found",compound="right", width=2)
                               lab_1.place(relx=0.5, rely=0.2, anchor= CENTER)
                     else:
                         lab_1 = ctk.CTkButton(root56, text="please type something",compound="right", width=2)
                         lab_1.place(relx=0.5, rely=0.5, anchor= CENTER)
                for i in range(len(xy)):
                     nn="allsongs//"+xy[i]
                     def add():
                         dest = shutil.move(nn,"favourites")
                     
                     
                     lab_1 = ctk.CTkButton(root56, text=xy[i],compound="right", width=2,command=add)
                     lab_1.place(relx=0.5, rely=0.2+(i*0.1), anchor= CENTER)
                
                     
                root56.mainloop()
             def seap():
                song=ent6.get()
                song=song.capitalize()
                song=song.replace(" ","")
                m=os.listdir("favourites/")
                xy=[]
                
                for d in m:
                     i=d
                     i=i.replace(" ","")
                     n=""
                     x=i.index("-")
                     for y in range(x+1):
                          n=n+i[y]
                     i=i.replace(n,"")
                     i=i.capitalize()
                     
                     if len(song)>0:
                          if song in i:
                               
                               xy.append(d)
                          
                for i in range(len(xy)):
                     nn="favourites//"+xy[i]
                     
                     
                     lab_1 = ctk.CTkButton(canvasf, text=xy[i],compound="right", width=2)
                     lab_1.place(relx=0.5, rely=0.3+(i*0.1), anchor= CENTER)
                
                     
                
             s=Button(master=canvasf, image=se, text="", width=0.1,height=0.1,command=sea)
             s.place(relx=0.4, rely=0.1, anchor= CENTER)
             s2=Button(master=canvasf, image=se, text="", width=0.1,height=0.1,command=seap)
             s2.place(relx=0.96, rely=0.1, anchor= CENTER)
             
             def clear():
                lab__1 = ctk.CTkLabel(canvasf,image=im4,compound="right", width=2)
                lab__1.place(relx=0.4, rely=1.1, anchor= CENTER)  
             cl=ctk.CTkButton(master=root,text="clear searches",command=clear)
             cl.place(relx=0.8, rely=0.7, anchor= CENTER) 
             
             def playf():
                   queuefav()
             def skip():
                   queuefav()
             b5=Button(master=root, image=pl, text="",width=0.1,height=0.1,command=playf)
             b5.place(relx=0.45, rely=0.965, anchor= CENTER)
             b6=Button(master=root, image=pa, text="",width=0.1,height=0.1,command=pause1)
             b6.place(relx=0.5, rely=0.965, anchor= CENTER)
             b7=Button(master=root, image=sk, text="",width=0.1,height=0.1,command=skip)
             b7.place(relx=0.55, rely=0.965, anchor= CENTER)
             def home():
                canvasf.destroy()
                cl.destroy()
                b5.destroy()
                lab__1 = ctk.CTkLabel(root, text="                                                                                              ",compound="right", width=2)
                lab__1.place(relx=0.8, rely=0.1, anchor= CENTER)
                start()
             b=ctk.CTkButton(master=root,text="HOME",command=home)
             b.place(relx=0.8, rely=0.1, anchor= CENTER)
          except FileNotFoundError:
               os.mkdir('favourites')

               
    bs=Button(master=canvas1,image=im8, width=0.1,height=0.1,command=favs)
    bs.place(relx=0.87, rely=0.5, anchor= CENTER)
    bs=Button(master=canvas1,image=im7, width=0.1,height=0.1,command=more)
    bs.place(relx=0.625, rely=0.5, anchor= CENTER)    
b=ctk.CTkButton(master=root, text="START", command=start)
b.place(relx=0.5, rely=0.9, anchor= CENTER)
b=Button(master=root, image=sett,  text="",width=0.1,height=0.1,command=setting)
b.place(relx=0.96, rely=0.96, anchor= CENTER)
def disable_event():
   #root.destroy()
   pygame.mixer.quit()
   quit()

root.protocol("WM_DELETE_WINDOW", disable_event)
root.resizable(False, False)
root.mainloop()
