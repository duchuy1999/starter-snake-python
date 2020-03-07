"""import heapq

EMPTY = 0
FOOD = 1
BODY = 2

class Cell:
    def __init__ (x, y, status):
        self.x = x
        self.y = y
        self.status = status
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None
        self.neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    
    def __lt__(self, other):
        return self.f < other.f
    
    
    def setValues(parent, end):
        self.parent = parent
        self.g = parent.g + 1
        self.f = self.g + self.h
        self.h = abs(self.x - end[0]) +  abs(self.y - end[1]) #Manhattan distance as heuristics
        
    def getParent():
        return self.parent
        

def astar(board, start, end):
    #start, end should be a tuple (x, y) 
      
    open_list = []
    closed_list = []
    headCell = Cell(start[0], start[1], end)
    endCell = None
    open_list.append(headCell)
    heapq.heapify(open_list)
    
    while len(open_list) != 0:
        parent = heapq.heappop(open_list)
        #initiate 4 adjacent cells
        
        for neighbor in parent.neighbors:
            if neighbor == end:
                endCell = Cell(neighbor[0], neighbor[1], end)
                endCell.setValues(parent)
           
       
        leftCell = Cell(start[0]-1, start[1], end)
        rightCell = Cell(start[0]+1, start[1], end)
        upCell = Cell(start[0], start[1]-1, end)
        downCell = Cell(start[0], start[1]+1, end)
        
        leftCell.setValues(parent)
        rightCell.setValues(parent)
        upCell.setValues(parent)
        downCell.setValues(parent)
        
        successors[]
        successors.append(leftCell)
        successors.append(rightCell)
        successors.append(upCell)
        successors.append(downCell)
        
        for successor in successors:
            if successor.x == end[0] and successor.y == end[1]:
                #found the food
        """