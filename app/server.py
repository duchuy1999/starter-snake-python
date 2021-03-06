import json
import os
import random

# Edited from Luciano's code
try:
    from tools import find_food, get_dir
except:
    from app.tools import find_food, get_dir

import bottle
from bottle import HTTPResponse

BODY = 0
EMPTY = 1
FOOD = 2

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
    #get board
    height = data["board"]["height"]
    width = data["board"]["width"]
    board = [[EMPTY for i in range(height)] for j in range(width)]
    food_list = []
    
    for food in data["board"]["food"]:
        board[food["x"]][food["y"]] = FOOD
        food_list.append((food["x"], food["y"]))

    for snakes in data["board"]["snakes"]:
        for body in snakes["body"]:
            board[body["x"]][body["y"]] = BODY
    

    directions = ["up", "down", "left", "right"]
    move = "up"

    myHeadX = data["you"]["body"][0]["x"]
    myHeadY = data["you"]["body"][0]["y"]
    myHead = (myHeadX, myHeadY)
    myHealth = data["you"]["health"]
    
    grid_on_path = find_food(board, food_list, myHead)
    print(grid_on_path)
    if grid_on_path == None:
        #Avoid walls and bodies, make this def IsWall later
        if myHeadX - 1 < 0 or board[myHeadX - 1][myHeadY] == BODY:
            directions.remove("left")
        if myHeadX + 1 >= width or board[myHeadX + 1][myHeadY] == BODY:
            directions.remove("right")
        if myHeadY - 1 < 0 or board[myHeadX][myHeadY - 1] == BODY:
            directions.remove("up")
        if myHeadY + 1 >= height or board[myHeadX][myHeadY + 1] == BODY:
            directions.remove("down")
        if len(directions) != 0:
            move = random.choice(directions)
                  
    else:
        if get_dir(myHead, grid_on_path) != None:
            move = get_dir(myHead, grid_on_path)
    
    
    
    """
    #Avoid walls and bodies, make this def IsWall later
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
    """
    
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
