import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image # Python Image Library

#Game window
game_window=Tk()
game_window.title("Sunny's Snake & ladder Game")
icons = PhotoImage(file='images/icon3.ico')
game_window.iconphoto(True,icons)
game_window.geometry("1500x800+0+0")

# Loading and displaying the background image
bg_image = Image.open("images\main_board.jpg")  # Replace with your image file
bg_photo = bg_image.resize((1600,800), Image.ANTIALIAS)
bg_photo_img = ImageTk.PhotoImage(bg_photo)
bg_label = Label(game_window, image=bg_photo_img)

#specifying the Board Size and each square size
BOARD_SIZE = 10 #10*10
SQUARE_SIZE = 70 

#Loading the Imnages of players, Snakes, ladders, grass and leaf
player1_image = Image.open("images\piece_02.png")  
player2_image = Image.open("images\piece_03.png")  
snake1_image = Image.open("images\snake.png")  
snake2_image = Image.open("images\snake2.png")  
snake3_image = Image.open("images\snake3.png")
snake4_image = Image.open("images\snake.png")
ladder1_image = Image.open("images\ladder_04.png") 
snake_logo = Image.open("images\snake_show2.jpg")
grass1 = Image.open("images\grass1.jpg")
leafs = Image.open("images\leafs.jpg")


#REsizing the Images
player1_image = player1_image.resize((SQUARE_SIZE - 20, SQUARE_SIZE - 20), Image.ANTIALIAS)
player2_image = player2_image.resize((SQUARE_SIZE - 40, SQUARE_SIZE - 35), Image.ANTIALIAS)
snake1_image = snake1_image.resize((SQUARE_SIZE - 20, 350), Image.ANTIALIAS)
snake2_image = snake2_image.resize((SQUARE_SIZE - 20, 570), Image.ANTIALIAS)
snake3_image = snake3_image.resize((SQUARE_SIZE - 20, 300), Image.ANTIALIAS)
snake4_image = snake4_image.resize((SQUARE_SIZE - 20, 550), Image.ANTIALIAS)
ladder1_image = ladder1_image.resize((SQUARE_SIZE-15, 440), Image.ANTIALIAS)
ladder2_image = ladder1_image.resize((SQUARE_SIZE-15, 140), Image.ANTIALIAS)
ladder3_image = ladder1_image.resize((SQUARE_SIZE-15, 100), Image.ANTIALIAS)

# Creating the player
player1_img = ImageTk.PhotoImage(player1_image)
player2_img = ImageTk.PhotoImage(player2_image)
snake1_img = ImageTk.PhotoImage(snake1_image)
snake2_img = ImageTk.PhotoImage(snake2_image)
snake3_img = ImageTk.PhotoImage(snake3_image)
snake4_img = ImageTk.PhotoImage(snake4_image)
ladder1_img = ImageTk.PhotoImage(ladder1_image)
ladder2_img = ImageTk.PhotoImage(ladder2_image)
ladder3_img = ImageTk.PhotoImage(ladder3_image)

snake_logo_image = snake_logo.resize((500,400), Image.ANTIALIAS)
grass1_image = grass1.resize((170,230),Image.ANTIALIAS)
leafs_image = leafs.resize((170,250),Image.ANTIALIAS)
snake_logo_image = ImageTk.PhotoImage(snake_logo_image)
grass1_image = ImageTk.PhotoImage(grass1_image)
leafs_image = ImageTk.PhotoImage(leafs_image)
snake_logo_label = Label(image=snake_logo_image,border=NO)
grass1_image_label = Label(image=grass1_image,border=NO)
leafs_image_label = Label(image=leafs_image,border=NO)


#Game Window/Page
def open_game_window():
    #storing the plauers name in variables 
    p1_name = player1_name.get()
    p2_name = player2_name.get()

    #Checking whether the both players have entered thier names or not
    if p1_name=="" or p2_name=="":
        #Giving Warning to the players to enter their names
        message_to_name = messagebox.showwarning("Warning","Please Enter the Players Name first to Start the Game!") 
        return

    global BOARD_SIZE
    global SQUARE_SIZE
    global player1_img
    global player1_img
    global snake1_img
    global snake2_img
    global snake3_img
    global snake4_img
    global ladder1_img
    global ladder2_img
    global ladder3_img
    global snake_logo_label
    global grass1_image_label
    global leafs_image_label

    global current_position_player1
    global current_position_player2
    global alter

    #Removig All Widgets of First Main Window
    bg_label.destroy()
    main_title.destroy()
    player1_name_label.destroy()
    player2_name_label.destroy()
    player1_name.destroy()
    player2_name.destroy()
    start_button.destroy()

    game_window.config(bg='black')
    frame_count_rev = 100
    frame_count_forward = 1
    frame_array = []

    #Creating Main Frame
    main_frame = Frame(game_window,relief="groove",height=800,width=800,borderwidth=15)
    main_frame.grid(row=0,column=1,padx=40,pady=30)

    # Main Gaming Board
    canvas = Canvas(main_frame, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE)
    canvas.grid()

    snake_logo_label.grid(row=0, column=2, padx=(180, 0), pady=(0, 30))
    grass1_image_label.grid(row=0,column=2,padx=(0,500),pady=(470,0))
    leafs_image_label.grid(row=0,column=2,padx=(0,550),pady=(0,250))

    #Dictionary of Snake position
    snake_positions = {
        "99": 19,  # Snake 1: Head at box label "99", Tail at box label "19"
        "96": 45,  
        "67": 27,  
        "90": 10   
    }
    #Dictionary of Ladder position
    ladder_positions = {
        "20":80,
        "43":63,
        "5":25,
        "66":86,
        "29":89
    }

    #Checking the Winner
    def check_winner(player):
        if player == 1 and current_position_player1 >= 100:
            return "Player 1 wins!"
        elif player == 2 and current_position_player2 >= 100:
            return "Player 2 wins!"
        return None

    #Function to Move players
    def move_player(dice_result):
        global alter
        if alter == 0:
            global current_position_player1
            new_position_p1 = current_position_player1 + dice_result

            snake_head_p1 = str(new_position_p1)
            ladder_btm_p1 = str(new_position_p1)

            if new_position_p1 <= BOARD_SIZE**2:
                if snake_head_p1 in snake_positions.keys():
                    new_position_p1 = snake_positions[snake_head_p1]
                elif ladder_btm_p1 in ladder_positions.keys():
                    new_position_p1 = ladder_positions[ladder_btm_p1]

                row = (BOARD_SIZE - 1) - (new_position_p1 - 1) // BOARD_SIZE
                if row % 2 != 0:
                    col = (new_position_p1 - 1) % BOARD_SIZE
                else:
                    col = (BOARD_SIZE - 1) - (new_position_p1 - 1) % BOARD_SIZE

                new_position_p1_coordinates = ((col + 0.5) * SQUARE_SIZE, (row + 0.5) * SQUARE_SIZE)
                canvas.coords(player1, new_position_p1_coordinates)
                current_position_player1 = new_position_p1
            winner = check_winner(1)
            if winner:
                title.destroy()
                winner_label = Label(game_window, text='CONGRATULATIONS!! '+p1_name+' IS WINNER', padx=40, pady=10, border=5, 
                         font=("Comic Sans MS", 20, "bold"), foreground="black",
                        background="yellow", relief="groove")
                winner_label.grid(row=0, column=2, padx=(0, 0),pady=(0,650))
                roll_button.config(state=DISABLED)  # Disable the roll button
                result_label.destroy()
                player_label.destroy()
                game_over_label = Label(game_window, text="GAME OVER...!!",padx=60,pady=10,border=5, 
                         font=("Times New Roman", 16, "bold"), foreground="black",
                         background="yellow",relief="groove")
                game_over_label.grid(row=0,column=2,padx=(265,0),pady=(500,0))
                return
            alter = 1  # Update alter after moving player 1

        elif alter == 1:
            global current_position_player2
            new_position_p2 = current_position_player2 + dice_result

            snake_head_p2 = str(new_position_p2)
            ladder_btm_p2 = str(new_position_p2)

            if new_position_p2 <= BOARD_SIZE**2:
                if snake_head_p2 in snake_positions.keys():
                    new_position_p2 = snake_positions[snake_head_p2]
                elif ladder_btm_p2 in ladder_positions.keys():
                    new_position_p2 = ladder_positions[ladder_btm_p2]

                row = (BOARD_SIZE - 1) - (new_position_p2 - 1) // BOARD_SIZE
                if row % 2 != 0:
                    col = (new_position_p2 - 1) % BOARD_SIZE
                else:
                    col = (BOARD_SIZE - 1) - (new_position_p2 - 1) % BOARD_SIZE

                new_position_p2_coordinates = ((col + 0.5) * SQUARE_SIZE, (row + 0.5) * SQUARE_SIZE)
                canvas.coords(player2, new_position_p2_coordinates)
                current_position_player2 = new_position_p2
            winner = check_winner(2)
            if winner:
                title.destroy()
                winner_label = Label(game_window, text='CONGRATULATIONS!! '+p2_name+' IS WINNER', padx=40, pady=10, border=5, 
                         font=("Comic Sans MS", 20, "bold"), foreground="black",
                        background="yellow", relief="groove")
                winner_label.grid(row=0, column=2, padx=(0,0),pady=(0,650))
                roll_button.config(state=DISABLED)  # Disable the roll button
                result_label.destroy()
                player_label.destroy()
                game_over_label = Label(game_window, text="GAME OVER...!!",padx=60,pady=10,border=5, 
                         font=("Times New Roman", 16, "bold"), foreground="black",
                         background="yellow",relief="groove")
                game_over_label.grid(row=0,column=2,padx=(265,0),pady=(500,0))
                return

            alter = 0  # Update alter after moving player 2


    # Function to roll the dice and start the game
    def roll_dice():
        dice_result = np.random.randint(1, 6)
        result_label.config(text=f"Dice Result: {dice_result}")
        move_player(dice_result)
        if alter==0:
           player_label.config(text="Player 1")
        else:
           player_label.config(text="Player 2")

    # Creating Boxes/Squares
    for i in range(BOARD_SIZE):
        row_list = []
        for j in range(BOARD_SIZE):
            color = "orange" if (i + j) % 2 == 0 else "yellow"
            box_frame = canvas.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE, (j + 1) * SQUARE_SIZE, (i + 1) * SQUARE_SIZE,
                                    fill=color)

            box_label = frame_count_rev if (i)%2 == 0 else ' '
            canvas.create_text((j + 0.5) * SQUARE_SIZE, (i + 0.5) * SQUARE_SIZE, text=box_label, fill="black")
            frame_count_rev-=1

    for i in range(9,-1,-1):
        for j in range(BOARD_SIZE):
            box_label = frame_count_forward if (i)%2 != 0 else ' '
            canvas.create_text((j + 0.5) * SQUARE_SIZE, (i + 0.5) * SQUARE_SIZE, text=box_label, fill="black")
            frame_count_forward+=1

    current_position_player1 = 1
    current_position_player2 = 1
    alter=0 #Initializing alter to 0 to give first turn to player 1

    #creating Images On the Board Canvas
    snake1 = canvas.create_image(320,210,image=snake1_img)
    snake2 = canvas.create_image(105,300,image=snake2_img)
    snake3 = canvas.create_image(460,370,image=snake3_img)
    snake4 = canvas.create_image(670,390,image=snake4_img)
    ladder1 = canvas.create_image(35,390,image=ladder1_img)
    ladder2 = canvas.create_image(595,320,image=ladder1_img)
    ladder3 = canvas.create_image(315,600,image=ladder2_img)
    ladder4 = canvas.create_image(175,320,image=ladder2_img)
    ladder5 = canvas.create_image(385,180,image=ladder2_img)

    player1 = canvas.create_image(SQUARE_SIZE // 1.5, (BOARD_SIZE - 1) * SQUARE_SIZE + SQUARE_SIZE // 2.3, image=player1_img)
    player2 = canvas.create_image(SQUARE_SIZE // 3.3, (BOARD_SIZE - 1) * SQUARE_SIZE + SQUARE_SIZE // 1.8, image=player2_img)

    # Create the dice roll button
    roll_button = Button(game_window, text="Roll Dice",relief="raised",padx=20,pady=10,border=5,
                         font=("Times New Roman", 20, "bold"), 
                         foreground="maroon", command=roll_dice)

    roll_button.grid(row=0,column=2,padx=(100,300),pady=(500,0))
    player_label = Label(game_window,text="Player 1",padx=20,pady=10,border=5, 
                         font=("Times New Roman", 16, "bold"), foreground="white",
                         background="red",relief="groove")
    result_label = Label(game_window, text="Dice Result: ",padx=20,pady=10,border=5, 
                         font=("Times New Roman", 16, "bold"), foreground="white",
                         background="red",relief="groove")
    title = Label(game_window, text='Scale the Snakes and Climb the Ladders!', padx=40, pady=10, border=5, 
                         font=("Comic Sans MSComic Sans MS", 20, "bold"), foreground="white",
                        background="blue", relief="groove")
    title.grid(row=0, column=2, padx=(10, 0),pady=(0,650))
    result_label.grid(row=0,column=2,padx=(150,0),pady=(500,0))
    player_label.grid(row=0,column=2,padx=(430,0),pady=(500,0))


#Declaring the Main Window's Widgets
main_title = Label(game_window,text="Snake & Ladders Adventure: Roll the Dice and Climb to Victory!", padx=50, pady=5, border=NO, 
                         font=("Comic Sans MS", 20, "bold"), foreground="white",
                        background="green", relief="groove")
player1_name_label = Label(game_window,text="ENTER FIRST PLAYER'S NAME",padx=20, pady=5, border=NO, 
                         font=("Comic Sans MS", 15, "bold"),background="white")
player1_name = Entry(game_window,width=50,font=("Arial", 16),relief="sunken",border=2)
player2_name_label = Label(game_window,text="ENTER SECOND PLAYER'S NAME",padx=20, pady=5, border=NO, 
                         font=("Comic Sans MS", 15, "bold"),background="white")
player2_name = Entry(game_window,width=50,font=("Arial", 16),relief="sunken",border=2)
start_button = Button(game_window, text="Start Game",relief="raised",padx=50,pady=5,border=5,
                         font=("Times New Roman", 20, "bold"), 
                         foreground="maroon",command=open_game_window)

# First Main Window Widgets Specification
def open_main_window():
    global bg_label
    global main_title
    global player1_name
    global player2_name
    global player1_name_label
    global player2_name_label
    global start_button

    bg_label.place(relwidth=1, relheight=1)
    main_title.grid(padx=(300,0),pady=(200,0))
    player1_name_label.grid(padx=(300,0),pady=(30,0))
    player1_name.grid(padx=(300,0),pady=(10,0))
    player2_name_label.grid(padx=(300,0),pady=(30,0))
    player2_name.grid(padx=(300,0),pady=(10,0))
    start_button.grid(padx=(300,0),pady=(30,0))

#Opening the First Main Window
open_main_window()
game_window.mainloop()