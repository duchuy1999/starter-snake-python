import json
import os
import random

import bottle
from bottle import HTTPResponse

EMPTY = 0
FOOD = 1
BODY = 2

@bottle.route("/")
def index():
    return "Your Battlesnake is alive!"


@bottle.post("/ping")
def ping():
    """
    Used by the Battlesnake Engine to make sure your snake is still working.
    """
    return HTTPResponse(status=200)


@bottle.post("/start")
def start():
    """
    Called every time a new Battlesnake game starts and your snake is in it.
    Your response will control how your snake is displayed on the board.
    """
    data = bottle.request.json
    print("START:", json.dumps(data))

    response = {"color": "#00FF00", "headType": "regular", "tailType": "regular"}
    return HTTPResponse(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps(response),
    )


@bottle.post("/move")
def move():
    """
    Called when the Battlesnake Engine needs to know your next move.
    The data parameter will contain information about the board.
    Your response must include your move of up, down, left, or right.
    """
    data = bottle.request.json
    #print("MOVE:", json.dumps(data))

    #gameID = data["game"]["id"]
    height = data["board"]["height"]
    width = data["board"]["width"]
    board = [[EMPTY]*height]*width
    for food in data["board"]["food"]:
        print(food)
        print(food["x"], food["y"])
        board[food["x"]][food["y"]] = FOOD

    for snakes in data["board"]["snakes"]:
        for body in snakes["body"]:
            board[body["x"]][body["y"]] = BODY
    #print(data)
    #print(board)


    # Choose a random direction to move in
    directions = ["up", "down", "left", "right"]
    #move = random.choice(directions)
    #move = "up"
    myHeadX = data["you"]["body"][0]["x"]
    myHeadY = data["you"]["body"][0]["y"]
    myHealth = data["you"]["health"]

    if myHeadX - 1 < 0 or board[myHeadX - 1][myHeadY] == BODY:
        directions.remove("left")
    if myHeadX + 1 >= width or board[myHeadX + 1][myHeadY] == BODY:
        directions.remove("right")
    if myHeadY - 1 < 0 or board[myHeadX][myHeadY - 1] == BODY:
        directions.remove("up")
    if myHeadY + 1 >= height or board[myHeadX][myHeadY + 1] == BODY:
        directions.remove("down")

    if len(directions) == 0:
        move = "up"
    else:
        move = random.choice(directions)

    # Shouts are messages sent to all the other snakes in the game.
    # Shouts are not displayed on the game board.
    shout = "I am a python snake!"

    response = {"move": move, "shout": shout}
    return HTTPResponse(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps(response),
    )


@bottle.post("/end")
def end():
    """
    Called every time a game with your snake in it ends.
    """
    data = bottle.request.json
    print("END:", json.dumps(data))
    return HTTPResponse(status=200)


def main():
    bottle.run(
        application,
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8080"),
        debug=os.getenv("DEBUG", True),
    )


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == "__main__":
    main()
