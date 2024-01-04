from cProfile import label
from email.mime import image
# for GUI
from tkinter import *
from logging import root
from tkinter.tix import COLUMN
# Python Imaging Library , support for opening, manipulating
from PIL import ImageTk, Image

import random


# main window
mw = Tk()
mw.title("Rock Paper Scissor Game for Python MINI_PROJECT")
mw.configure(background="black")


# for picture
rock = ImageTk.PhotoImage(Image.open("rock.jpg"))
paper = ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor = ImageTk.PhotoImage(Image.open("scissor.jpg"))
cmp_rock = ImageTk.PhotoImage(Image.open("rock.jpg"))
cmp_paper = ImageTk.PhotoImage(Image.open("paper.jpg"))
cmp_scissor = ImageTk.PhotoImage(Image.open("scissor.jpg"))


defa = ImageTk.PhotoImage(Image.open("default.jpg"))
cmp_defa = ImageTk.PhotoImage(Image.open("default.jpg"))


# to insert picture --- Label

cmp_lable = Label(mw, image=cmp_defa, background="black")
cmp_lable.grid(row=1, column=0)

usr_lable = Label(mw, image=defa, background="black")
usr_lable.grid(row=1, column=4)

# for score

cmp_score = Label(mw, text="0", font=100, background="grey",
                  foreground="yellow")
cmp_score.grid(row=1, column=1)

pl_score = Label(mw, text="0", font=100, background="grey",
                 foreground="yellow")
pl_score.grid(row=1, column=3)


# indicator
cmp_indi = Label(mw, font=20, text="COMPUTER", background="black",
                 foreground="white") . grid(row=0, column=1)
pl_indi = Label(mw, font=20, text="USER", background="black",
                foreground="white") . grid(row=0, column=3)


# message
msg = Label(mw, font=100)
msg.grid(row=3, column=2)

# To update message


def updateMessage(x):
    msg['text'] = x

# To update user Score


def updateUserScore():
    score = int(pl_score["text"])
    score += 1
    pl_score["text"] = str(score)

# To update computer Score


def updateCmpScore():
    score = int(cmp_score["text"])
    score += 1
    cmp_score["text"] = str(score)


# button
rock_btn = Button(mw, text="ROCK", width=20, height=2,
                  bg="RED", fg="white", command=lambda: updatechoice("rock")) .grid(row=2, column=1)
paper_btn = Button(mw, text="PAPER", width=20, height=2,
                   bg="GREEN", fg="white", command=lambda: updatechoice("paper")).grid(row=2, column=2)
scissor_btn = Button(mw, text="SCISSOR", width=20, height=2,
                     bg="BLUE", fg="white", command=lambda: updatechoice("scissor")).grid(row=2, column=3)


# to UPDATE choice

chs = ['rock', 'paper', 'scissor']


def updatechoice(x):

    # for COMPUTER
    cmp_chs = chs[random.randint(0, 2)]
    if (cmp_chs == "rock"):
        cmp_lable.configure(image=rock, background="black")
    elif cmp_chs == "paper":
        cmp_lable.configure(image=paper, background="black")
    else:
        cmp_lable.configure(image=scissor, background="black")

    # for USER
    if (x == "rock"):
        usr_lable.configure(image=rock, background="black")
    elif x == "paper":
        usr_lable.configure(image=paper, background="black")
    else:
        usr_lable.configure(image=scissor, background="black")

    winner(x, cmp_chs)


# To check WINNER
def winner(pl, com):
    if pl == com:
        updateMessage("Match Tie 🪢")

    elif pl == "rock":
        if com == "paper":
            updateMessage("You loose 🃏")
            updateCmpScore()
        else:
            updateMessage("You Win 👑")
            updateUserScore()

    elif pl == "paper":
        if com == "scissor":
            updateMessage("You loose 🃏")
            updateCmpScore()
        else:
            updateMessage("You Win 👑")
            updateUserScore()

    elif pl == "scissor":
        if com == "rock":
            updateMessage("You loose 🃏")
            updateCmpScore()
        else:
            updateMessage("You Win 👑")
            updateUserScore()
    else:
        pass


mw.mainloop()
