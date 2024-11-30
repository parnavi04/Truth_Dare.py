from tkinter import *
import random
from tkinter import messagebox
COLOR = "#121822"
Yellow = "#fef65b"
red = "#cf171e"
TEXT = ""
# ----------------------------------OPERATION----------------------------
def truth():
    truth_questions = [
        "What’s the biggest lie you’ve ever told?",
        "What’s your most embarrassing moment?",
        "Have you ever had a crush on someone in this room?",
        "If you could swap lives with someone for a day, who would it be and why?",
        "What’s something you’re glad your parents don’t know about you?",
        "Have you ever cheated on a test?",
        "What’s the most childish thing you still do?",
        "What’s a secret you’ve never told anyone?",
        "If you had to date someone in this room, who would it be?",
        "What’s the most illegal thing you’ve done?",
        "Have you ever broken someone’s heart?",
        "What’s your worst habit?",
        "What’s the most embarrassing text you’ve ever sent?",
        "What’s the craziest thing you’ve done in public?",
        "If you had to marry one celebrity, who would it be?",
        "Have you ever told a lie to get out of trouble?",
        "Who is your secret crush?",
        "What’s something you’ve done that you still regret?",
        "Have you ever snuck out of the house at night?",
        "What’s the worst thing you’ve ever said to someone?",
        "Have you ever lied to get a job?",
        "What’s the most embarrassing thing you’ve searched online?",
        "What’s the dumbest thing you’ve done on a dare?",
        "Have you ever been caught cheating on an exam?",
        "What’s your weirdest talent?",
        "If you could erase one past experience, what would it be?",
        "What’s the most awkward conversation you’ve had?",
        "Who is the last person you stalked on social media?",
        "What’s your biggest insecurity?",
        "Have you ever had a crush on your teacher?"
    ]
    truth_question = random.choice(truth_questions)
    result.config(text = truth_question, fg= Yellow, font=("Arial",13))

def dare():
    dare_questions = [
        "Do your best dance move for 30 seconds.",
        "Let the person to your left draw on your face with a marker.",
        "Wear socks on your hands for the next 3 rounds.",
        "Call your crush and confess your feelings.",
        "Let someone tickle you for 30 seconds.",
        "Eat a raw onion slice.",
        "Post an embarrassing photo on your social media.",
        "Talk in an accent for the next 10 minutes.",
        "Let someone in the room redo your hairstyle.",
        "Try to juggle 3 items in the room.",
        "Walk around like a duck until your next turn.",
        "Call your best friend and sing 'Happy Birthday' to them.",
        "Do 20 pushups in a row.",
        "Speak only in rhymes for the next 3 rounds.",
        "Share the last 5 photos on your phone with everyone.",
        "Hold your breath for 30 seconds.",
        "Let someone else write a text to anyone on your phone.",
        "Act like a monkey until your next turn.",
        "Do a cartwheel (or try if you can't).",
        "Eat a spoonful of mustard or hot sauce.",
        "Dance without music for 1 minute.",
        "Let someone else give you a new nickname.",
        "Run around the outside of the house (or building) three times.",
        "Share your most embarrassing story.",
        "Allow the person to your right to send a text from your phone.",
        "Wear a silly hat for the rest of the game.",
        "Imitate your favorite celebrity.",
        "Let the group come up with a nickname for you, and you have to be called that for the rest of the night.",
        "Hug the person closest to you.",
        "Sing the chorus of your favorite song out loud."
    ]
    dare_question = random.choice(dare_questions)
    result.config(text=dare_question, fg=Yellow, font=("Arial", 13))

def punish():
    punishments = [
        "Do 10 pushups right now.",
        "Eat a spoonful of hot sauce or chili powder.",
        "Wear your clothes inside out for the next hour.",
        "Let the group choose a word that you have to include in every sentence for the next 10 minutes.",
        "Hold an ice cube in your hand until it melts.",
        "Let someone in the group give you a new hairstyle.",
        "Do a silly dance for 1 minute without any music.",
        "Let the person next to you send a text from your phone.",
        "Give the person on your right a piggyback ride across the room.",
        "Do 20 squats while everyone watches.",
        "Sing a song chosen by the group, but sing it in a funny voice.",
        "Let someone draw a mustache on your face with a marker.",
        "Speak in a robot voice for the next 5 minutes.",
        "Let the group decide what you have to post on your social media.",
        "Eat a raw egg.",
        "Let someone else control your phone for the next 5 minutes.",
        "Pretend to be a waiter/waitress and serve snacks to everyone.",
        "Do a handstand (or attempt it) and hold it for 10 seconds.",
        "Wear someone else's shoes for the next 15 minutes.",
        "Take a selfie with the funniest face possible and send it to your crush.",
        "Do an impression of a celebrity chosen by the group until the next round.",
        "Tell an embarrassing story about yourself that no one knows.",
        "Let the group pick a song and you have to dance to it.",
        "Put makeup on in the weirdest way possible (if applicable).",
        "Wear a blindfold for the next two rounds.",
        "Let the group pick a nickname for you and call you that for the rest of the game.",
        "Do the chicken dance for 1 minute.",
        "Let someone tickle you for 30 seconds straight.",
        "Sing everything you say for the next 5 minutes."
    ]
    punishment = random.choice(punishments)
    messagebox.showinfo(title= "You Coward", message= punishment)
    result.config(text=TEXT)

# ____________________________UI_____________________________________
window = Tk()
window.minsize(width=700, height=400)
window.title("Truth Dare Game")
window.config(padx= 20, pady= 20)
window.config(bg= COLOR)

# canvas
canvas = Canvas(width=600, height=300, bg= COLOR, highlightthickness=0)
poster_img = PhotoImage(file="TruthDare_1.png")
canvas.create_image(300, 150, image= poster_img)
canvas.grid(column= 1, row=0)

# Buttons
Truth_button = Button(text= "Truth", width= 10, bg= Yellow, command= truth)
Truth_button.grid(column= 0, row= 1)

Dare_button = Button(text= "Dare", width= 10, bg= Yellow, command= dare)
Dare_button.grid(column= 2, row= 1)

punish_button = Button(text="Punish",width= 10, bg= red, command= punish)
punish_button.grid(column = 1, row = 2)
# label
result = Label(text = TEXT, bg = COLOR)
result.grid(column= 1, row= 1)
window.mainloop()