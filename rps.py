import tkinter
import tkinter.font as font
from time import sleep
from random import randint

class window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("400x500")
        self.window.title("Rock🪨, Paper📄, Scissors✂️")

        self.hasChosen = False
        self.player_choice = None
        self.player_points = 0

        self.font = font.Font(family="Mochiy Pop One")

        self.rock = tkinter.Button(self.window, text="Rock🪨", command=self.choose_rock, height=2, width=11, font=self.font, borderwidth=1, bg="#242124", fg="#FFFFFF")
        self.rock.place(relx=1.0, y=0, anchor=tkinter.NW)
        self.paper = tkinter.Button(self.window, text="Paper📄", command=self.choose_paper, height=2, width=11, font=self.font, borderwidth=1, bg="#242124", fg="#FFFFFF")
        self.paper.place(relx=1.0, y=0, anchor=tkinter.W)
        self.scissors = tkinter.Button(self.window, text="Scissors✂️", command=self.choose_scissors, height=2, width=12, font=self.font, borderwidth=1, bg="#242124", fg="#FFFFFF")
        self.scissors.place(relx=1.0, y=0, anchor=tkinter.NE)

        self.your_choice = tkinter.Label(self.window, text="", font=self.font, width=30)
        self.bot_choice = tkinter.Label(self.window, text="", font=self.font)

        self.round_status = tkinter.Label(self.window, text="", font=self.font)
        self.points_text = tkinter.Label(self.window, text="Points: " + str(self.player_points), font=self.font)

        self.rock.pack()
        self.paper.pack()
        self.scissors.pack()
        self.your_choice.pack()
        self.round_status.pack(anchor=tkinter.CENTER)
        self.bot_choice.pack(side=tkinter.BOTTOM)
        self.points_text.pack(side=tkinter.LEFT)
        self.window.mainloop()

    def choose_rock(self):
        if self.hasChosen == False:
            self.your_choice["text"] = "You chose: rock"
            self.player_choice = "rock"
            self.hasChosen = True
            self.choose()

    def choose_paper(self):
        if self.hasChosen == False:
            self.your_choice["text"] = "You chose: paper"
            self.player_choice = "paper"
            self.hasChosen = True
            self.choose()

    def choose_scissors(self):
        if self.hasChosen == False:
            self.your_choice["text"] = "You chose: scissors"
            self.player_choice = "scissors"
            self.hasChosen = True
            self.choose()

    # Bot

    def choose(self):
        self.bot_choice_v = None
        if self.hasChosen == True:
            print("Bot is choosing!")
            sleep(3)
            self.random = randint(1, 3)
            if self.random == 1:
                self.bot_choice_v = "rock"
                self.bot_choice["text"] = "Bot chose: " + self.bot_choice_v
                print("Calculating results!")
                sleep(5)
                self.check()
            elif self.random == 2:
                self.bot_choice_v = "paper"
                self.bot_choice["text"] = "Bot chose: " + self.bot_choice_v
                print("Calculating results!")
                sleep(5)
                self.check()
            elif self.random == 3:
                self.bot_choice_v = "scissors"
                self.bot_choice["text"] = "Bot chose: " + self.bot_choice_v
                print("Calculating results!")
                sleep(5)
                self.check()

    # Check results

    def check(self):
        if self.player_choice == "rock" and self.bot_choice_v == "paper":
            self.lose()
        elif self.player_choice == "paper" and self.bot_choice_v == "rock":
            self.win()
        elif self.player_choice == "scissors" and self.bot_choice_v == "paper":
            self.win()
        elif self.player_choice == "paper" and self.bot_choice_v == "scissors":
            self.lose()
        elif self.player_choice == "rock" and self.bot_choice_v == "scissors":
            self.win()
        elif self.player_choice == "scissors" and self.bot_choice_v == "rock":
            self.lose()
        elif self.player_choice == self.bot_choice_v:
            self.draw()
        else:
            print("Wrong!")


    def win(self):
        self.round_status["text"] = "You win!🏆"
        print("won")
        self.player_points += randint(10, 20)
        self.points_text["text"] = "Points: " + str(self.player_points)
        self.player_choice = None
        self.bot_choice_v = None
        self.hasChosen = False

    def lose(self):
        self.round_status["text"] = "You lose!😟"
        print("lose")
        self.player_choice = None
        self.bot_choice_v = None
        self.hasChosen = False

    def draw(self):
        self.round_status["text"] = "Draw!❌"
        print("draw")
        self.player_choice = None
        self.bot_choice_v = None
        self.hasChosen = False


if __name__ == "__main__":
    w = window()
