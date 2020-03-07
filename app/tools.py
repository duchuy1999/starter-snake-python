#pip install astarlib
from astarlib import aStar
import sys

def find_food(board, food_list, head):
    nearest_food = None
    nearest_path = None
    path_length = sys.maxsize
    
    for food in food_list:
        normalized_board = aStar(board)
        food_path = None
        try:
            food_path = normalized_board.find_path(head, food)
        except:
            continue
        if food_path != None and food_path[1] < path_length:
            path_length = food_path[1]
            nearest_food = food
            nearest_path = food_path[0]
        else:
            return None
            
    print(nearest_path)
        
    if nearest_path != None:
        return nearest_path[1]
    else:
        return None
    
def get_dir(head, neighbor):
    if neighbor[0] == head[0] - 1 and neighbor[1] == head[1]:
        return "left"
    elif neighbor[0] == head[0] + 1 and neighbor[1] == head[1]:
        return "right"
    elif neighbor[0] == head[0] and neighbor[1] == head[1] - 1:
        return "up"
    elif neighbor[0] == head[0] and neighbor[1] == head[1] + 1:
        return "down"
    else:   
        return None