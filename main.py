import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

total_states_correct = 0
data = pandas.read_csv("./50_states.csv")
states_list = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{total_states_correct}/50 - Guess the US State", prompt="What's another "
                                                                                                    "state?")
    answer_state = answer_state.title()

    if answer_state in states_list:
        guessed_states.append(answer_state)
        total_states_correct += 1
        state = turtle.Turtle()
        state.hideturtle()
        state.pu()
        state_data = data[data.state == answer_state]
        cor_x = state_data["x"]
        cor_y = state_data["y"]
        state.goto(int(cor_x), int(cor_y))
        state.write(answer_state)
        # alternatief om van de pandas series een specifieke ruw waarde van de Series te krijgen
        # state.write(state_data.state.item())

screen.exitonclick()


