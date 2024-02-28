from tkinter import *
import random

root = Tk()
root.title("ROCK / PAPER / SCISSOR GAME")
root.geometry("900x600")

def game(event):
    global player_image,player_label,vs_image,vs_label,computer_image,computer_label,winner_label
    option=["ROCK","PAPER","SCISSOR"]
    player_select=event.widget.cget("text")
    computer_select=random.choice(option)
    print(f"player:",{player_select},"copmuter :",{computer_select})


    try:
        if(player_select==computer_select):
            player_image = PhotoImage(file=f"{player_select.lower()}.png")
            computer_image = PhotoImage(file=f"{computer_select.lower()}.png")

            player_label.configure(image=player_image)
            player_label.image=player_image

            computer_label.configure(image=computer_image)
            computer_label.image=computer_image

            winner_label.configure(text="GAME DRAW")
            game()

        elif player_select=="ROCK" and computer_select=="SCISSOR" or (player_select=="PAPER" and computer_select=="ROCK") or(player_select=="SCISSOR" and computer_select=="PAPER"):
            print("YOU WIN") 

            player_image = PhotoImage(file=f"{player_select.lower()}.png")
            computer_image = PhotoImage(file=f"{computer_select.lower()}.png")

            player_label.configure(image=player_image)
            player_label.image=player_image

            computer_label.configure(image=computer_image)
            computer_label.image=computer_image

            winner_label.configure(text="GAME WIN")
            game()

        else:
            print("YOU LOSE")

            player_image = PhotoImage(file=f"{player_select.lower()}.png")
            computer_image = PhotoImage(file=f"{computer_select.lower()}.png")

            player_label.configure(image=player_image)
            player_label.image=player_image

            computer_label.configure(image=computer_image)
            computer_label.image=computer_image

            winner_label.configure(text="GAME LOSE")
            game()
    except Exception as err:
        pass
 
heading = Label(text="ROCK / PAPER / SCISSOR GAME:", font="Algerian 20 bold")
heading.grid(row=1, column=0, padx=0, pady=15)

frame = Frame(root)
frame.grid(row=2, column=0)

title_label = Label(frame, text="PLAYER", font="Sitka 17 bold")
title_label.grid(row=1, column=3, padx=150, pady=0)

title_label = Label(frame, text="COMPUTER", font="Sitka 17 bold")
title_label.grid(row=1, column=11, padx=150, pady=0)


player_image = PhotoImage(file="rock.png")
player_label = Label(frame, image=player_image)
player_label.grid(row=4, column=3, pady=10)

# vsimage=PhotoImage(file="vs.png")
# vsimglabel=Label(image=vsimage)
# vsimglabel.grid(row=4,column=5)


vsimage=PhotoImage(file="vs.png")
vs_label = Label(frame, image=vsimage)
vs_label.grid(row=4, column=5, pady=10)

computer_image=PhotoImage(file="rock.png")
computer_label = Label(frame, image=computer_image)
computer_label.grid(row=4, column=11, pady=10)

Button_frame=Frame(root)
Button_frame.grid(row=6,column=0)

winner_label=Label(Button_frame,text="WINNER",font="Satika 20 bold")
winner_label.grid(row=7,column=1,pady=10)

r=Button(Button_frame,text="ROCK",font="Arail 20 bold",width=8,height=1)
r.grid(row=8,pady=10)
r.bind("<Button-1>", game)

p=Button(Button_frame,text="PAPER",font="Arail 20 bold",width=8,height=1)
p.grid(row=8,column=1,pady=10)
p.bind("<Button-1>", game)

s=Button(Button_frame,text="SCISSOR",font="Arail 20 bold",width=8,height=1)
s.grid(row=8,column=2,pady=10)
s.bind("<Button-1>", game)



root.mainloop()


# from PIL import Image,ImageTk

# root=Tk()
# root.geometry("500x400")
# image = Image.open(r"D:\phython\download.png")
# label=Label(root,text="hi")
# photo = ImageTk.PhotoImage(image)
# label.config(image=photo)
# label.pack(side=LEFT)
