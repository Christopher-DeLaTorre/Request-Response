from flask import Flask
import random as r

app = Flask(__name__) #setup for routes

@app.route('/') #url indication
def homepage(): #action at url
    """Shows a greeting to the user.""" #removeable/not-needed
    return 'Are you there, world? It\'s me, Ducky!' #content-return

@app.route('/animal/<users_animal>') 
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>') 
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite food."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>') 
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their adj. and noun."""
    return f'{noun} are just soooo {adjective}!'

@app.route('/multiply/<number1>/<number2>') 
def multiply(number1, number2):
    """Display a message to the user that changes based on their numbers given."""
    product = 0
    if number1.isdigit() & number2.isdigit():
        product = int(number1)*int(number2)
        return f'{number1} times {number2} is {product}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>') 
def sayntimes(word, n):
    """Display a message to the user that changes based on their word and amount."""
    n1 = int(n)
    hold = ""
    if n.isdigit():
        while n1 > 0:
            hold += word + ' '
            n1 -= 1
        return hold
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

@app.route('/dicegame/') 
def dicerole():
    """Display the random throw of a 6 side die"""
    num = r.randint(1, 6)
    if num == 6:
        return f'You rolled a 6. You won!'
    else:
        return f'You rolled a {num}. You lost!'

if __name__ == '__main__':
    app.run(debug=True)
