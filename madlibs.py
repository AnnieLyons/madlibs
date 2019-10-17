"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user and asks for name."""

    return render_template("hello.html")

@app.route('/greet')
def play_game():
    """Ask user to play game."""

    player = request.args.get("person")
    compliment = choice(AWESOMENESS)

    return render_template("greet.html",
                           person=player,
                           compliment=compliment)

@app.route('/goodbye')
def say_goodbye():
    """Says goodbye"""
    no_play = request.args.get("play_game")
    play = request.args.get("play_game")
    # player = request.args.get("person")
    # if no_play:
    if no_play == "No":
        return render_template("goodbye.html",
                            # person=player,
                            yesno=no_play)
    else:
        return render_template("lets_play.html",
                            # person=player,
                            yesno=play)


@app.route('/madlib')
def madlib():
    """Plays madlib game."""
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")


    return render_template("madlib.html",
                            person=person,
                            color=color,
                            noun=noun,
                            adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)



# @app.route('/game')
# def greet_person():
#     """Greet user with compliment."""

#     player = request.args.get("person")

#     compliment = choice(AWESOMENESS)

#     return render_template("compliment.html",
#                            person=player,
#                            compliment=compliment)



    # return render_template("goodbye.html",
    #                         person=player,
    # if no_play:
    #     return render_template("goodbye.html",                      
    #                             yes=play,
    #                             no=no_play)