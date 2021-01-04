from tkinter import *
import random

root = Tk()

##CODE##

moves = ['Rock','Paper','Scissor']

computer_move = random.choice(moves)


# Scores
player_score = int()
computer_score = int()



#Functions

def rock():
	global player_move
	player_move = 'Rock'
	main()


def paper():
	global player_move
	player_move = 'Paper'
	main()



def scissor():
	global player_move
	player_move = 'Scissor'
	main()


# Scoring system, restart and main functions.

def check_if_won():
	global player_score
	global computer_score

	# Scoring System

	if player_move == "Rock":
		if computer_move == "Paper":
			computer_score += 1
		else:
			player_score += 1


	elif player_move == "Paper":
		if computer_move == "Scissor":
			computer_score += 1
		else:
			player_score += 1


	elif player_move == "Scissor":
		if computer_move == "Rock":
			computer_score += 1
		else:
			player_score += 1


def restart():
	# Restart Function (restarts the game)
	global computer_move
	computer_move = random.choice(moves)



def main():
	# Main function (the main function that is run)
	output.delete('1.0',END)
	won = check_if_won()
	result = f'Your Choice: {player_move}\nComputer\'s Choice: {computer_move}\n Your Score : {player_score}\n Computer Score : {computer_score}\n\n'
	output.insert(END,result)
	restart()



# Size
root.geometry('400x400')

# Title
root.title('Rock Paper Scissors Game')


# Unresizable
root.resizable(0,0)

# Buttons
button_rock = Button(root, text='Rock', padx=20, bg='cyan', fg='black', command=rock) # Cyan
button_paper = Button(root, text='Paper', padx=17, bg='pink', fg='black', command=paper) # Pink
button_scissor = Button(root, text='Scissor', padx=13, bg='green', fg='black', command=scissor) # Green

button_rock.pack()
button_paper.pack()
button_scissor.pack()


output = Text(root, width=40, height=17, background='yellow', fg='black')
output.pack(anchor=W)


##END##



root.mainloop()