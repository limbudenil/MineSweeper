#This the minesweeper game of group no. 5 which includes following members:
#Reynold Dmello 0997039
#Denil Limbu 0997147
#Prasad Modi 0995626

import random
from tkinter import *
from functools import partial

a= random.randint(0,8)     #random mines to be placed
b= random.randint(0,8)
c= random.randint(0,8)
d= random.randint(0,8)
e= random.randint(0,8)
fgg=0                       #flag counter
count=0

class minesweeper:
    def __init__(self):                         #intialization of mines,images,frames,width and height
        self.x= 9                               #this is the rows
        self.y= 9                               #this is the columns
        self.mines_count = 10
        self.mines = []
        self.button_list = {}
        self.root = Tk()
        self.frame=Frame()
        self.frame.grid()
        self.frame2=Frame()
        self.frame2.grid()
        self.empty_image = PhotoImage(file='C:\\temp\\tile_plain.gif')  #this image displays the empty image button
        self.min=PhotoImage(file='C:\\temp\\tile_mine.gif')  #this image displays the mine when the button is pressed
        self.photo1= PhotoImage(file='C:\\temp\\minesweeper.gif') #these images displays the number of  mines
        self.photo2= PhotoImage(file='C:\\temp\\tile_2.gif')
        self.photo3= PhotoImage(file='C:\\temp\\tile_3.gif')
        self.photo4= PhotoImage(file='C:\\temp\\tile_4.gif')
        self.photo5= PhotoImage(file='C:\\temp\\tile_5.gif')
        self.photo_new = PhotoImage(file='C:\\temp\\new_game_button.png')#this image shows a smiling face for new game
        self.lost= PhotoImage(file='C:\\temp\\lost.png')#this image frowns when the game is lost
        self.flag= PhotoImage(file='C:\\temp\\tile_flag.gif')#this image flags any button
        self.won= PhotoImage(file='C:\\temp\\won.png')#this image displays a happy face when wins

        row=0
        col=0
        self.Btn = Button(self.frame, width=30, height=35,image=self.photo_new,command= self.refresh )
        self.Btn.grid(row=0,column=3,columnspan=3, sticky=N)
        #the below loops are used to produce the buttons by using the rows and columns
        for i in range(self.x):
            for j in range(self.y):
                loc = (i, j)
                #btn=Button(self.root,width=20,height=20,image=self.empty_image)
                btn = Button(self.frame2, width=20, height=20, image = self.empty_image, command= lambda l = loc: self.check(l,row,col))
                btn.grid(column=j,row=i)
                btn.bind("<Button-3>", lambda event, l =loc: self.mark(l) )
                self.button_list[loc] = btn

        self.root.mainloop()

    def mark(self,l):           #this fucntion flags the buttons
        global fgg,count
        if fgg < 10 :
            count=count+1
            btn=self.button_list[l]
            btn.config(image=self.flag,width=10,height=15,state=DISABLED)
            fgg=fgg+1

        else:
            print("You cant press more than 10 flags...........")

    def refresh(self):          #this function refreshes the game when the smiley image button is pressed
        global a,b,c,d,e
        a= random.randint(0,8)
        b= random.randint(0,8)
        c= random.randint(0,8)
        d= random.randint(0,8)
        e= random.randint(0,8)

        self.Btn.configure(image=self.photo_new, height=30, width=35)
        for i in range(0,9):
            for j in range(0,9):
                btn=self.button_list[(i,j)]
                btn.config(image = self.empty_image, relief=RAISED, width=20,height=20,state=ACTIVE)

    def check(self, l,row,col):     #this function checks the button if its a mine or not and if there is a neighbouring mine it displays the number of mines
        global count
        btn = self.button_list[l]
        btn.config(image="", relief=SUNKEN, width=2, height=1)
        count=count+1
        #this condition checks whether the game is won
        if count== 71:
            print("You win!! GAME OVER")
            self.Btn['image']= self.won
            return
           # if this cell is a mine, then:
        mines1=(0,a)
        mines2=(1,b)
        mines3=(2,c)
        mines4=(3,d)
        mines5=(4,a)
        mines6=(5,b)
        mines7=(6,c)
        mines8=(7,d)
        mines9=(8,e)
        mines10=(4,d)
        #these conditions is for the button pressed which turn out to be mine to display game over
        if l==mines1 or l== mines2 or l== mines3 or l== mines4 or l== mines5 or l== mines6 or l== mines7 or l== mines8 or l== mines9 or l== mines10:
            print("Sorry...The Game is Over..........You pressed on the mine!!")
            self.Btn.configure(image=self.lost, height=30, width=35)
            btn=self.button_list[mines1]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines2]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines3]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines4]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines5]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines6]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines7]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines8]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines9]
            btn.config(image=self.min, width=20, height=15)

            btn=self.button_list[mines10]
            btn.config(image=self.min, width=20, height=15)

            return

        total=0
#this loops checks the total number of neighbouring mines and displays on the button which is currently pressed
        for i in range(l[0]-1, l[0] + 2):
            for j in range(l[1] - 1, l[1] + 2):
                if i > -1 and i < 9 and j > -1 and i < 9:
                    if (i,j) == mines1:
                        total=total+1
                    elif (i,j)==mines2:
                        total=total+1
                    elif (i,j)==mines3:
                        total=total+1
                    elif (i,j)==mines4:
                        total=total+1
                    elif (i,j)==mines5:
                        total=total+1
                    elif (i,j)==mines6:
                        total=total+1
                    elif (i,j)==mines7:
                        total=total+1
                    elif (i,j)==mines8:
                        total=total+1
                    elif (i,j)==mines9:
                        total=total+1
                    elif (i,j)==mines10:
                        total=total+1
                    '''elif (i,j)!=mines1 or (i,j)!=mines2 or (i,j)!=mines3 or (i,j)!=mines4 or (i,j)!=mines5 or (i,j)!=mines6 or (i,j)!=mines7 or (i,j)!=mines8 or (i,j)!=mines9 or (i,j)!=mines10:
                            btn=self.button_list[(i,j)]
                            btn.config(image="",relief=SUNKEN,width=2, height=1)'''

        b1=self.button_list[l]
        if total==1:
            b1.config(image=self.photo1, relief=SUNKEN,width=20, height=15)

        if total==2:
            b1.config(image=self.photo2, relief=SUNKEN,width=20, height=15)

        if total==3:
            b1.config(image=self.photo3, relief=SUNKEN,width=20, height=15)

        if total==4:
            b1.config(image=self.photo4, relief=SUNKEN,width=20, height=15)

        if total==5:
            b1.config(image=self.photo5, relief=SUNKEN,width=20, height=15)

DY = minesweeper()
