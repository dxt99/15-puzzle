import copy
from hashlib import new #deepcopy
import heapq as pq #priority queue

class puzzlesolver:
    dxy = [(1,0),(0,1),(-1,0),(0,-1)] #move directions
    X = 0 #initial X value
    puzzle = [] #initial puzzle
    mincost = 1e9+7 #minimum cost, initialized at 1e9+7
    answer = [] #answer to puzzle, empty if unsolvable

    def __init__(self, filename):
        self.getPuzzle(filename)
        print(self.solve())

    def getPuzzle(self,filename): #gets puzzle from test folder
        temp_puzzle = []
        with open("./test/"+filename) as f:
            lines = f.readlines()
            for line in lines:
                temp_puzzle.append([int(i) for i in line.split()])
        self.puzzle = temp_puzzle

    def calcKurang(self): #calculates sum of KURANG(i) + X
        flat = [i for j in self.puzzle for i in j]
        cost = 0
        for i in range(len(flat)):
            if flat[i]==0 and (((i//4)%2 == 0 and i%2==1) or (i//4)%2 == 1 and i%2 == 0):
                cost += 1 # X
            for j in range(i+1,len(flat)):
                if (flat[i]>flat[j] and flat[j]!=0):
                    cost+=1
        return cost

    def isSolved(self): #checks whether puzzle is solved
        return self.puzzle == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    
    def calcCost(self, puzzle): #calculates cost
        flat = [i for j in puzzle for i in j]
        cost = 0
        for i in range(len(flat)):
            if ((i+1)%16 != flat[i]):
                cost+=1
        return cost

    def getZeroPos(self, puzzle):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if puzzle[i][j]==0:
                    return (i,j)
        return (-1,-1)
    
    def validIndex(self, x, y):
        return (0<=x<4 and 0<=y<4)
    
    def solve(self): #main puzzle solver
        kurang = self.calcKurang()
        print("Nilai fungsi kurang = " + str(kurang))
        if kurang%2!=0:
            return "Puzzle tidak dapat diselesaikan"
        
        cost = self.calcCost(self.puzzle)
        heap = [] #current total cost, depth, puzzle, moves to puzzle
        pq.heappush(heap,(cost,0,copy.deepcopy(self.puzzle),[]))

        while len(heap)>0:
            curCost, depth, curPuzzle, path = pq.heappop(heap)
            if (curCost>self.mincost): #bound
                continue
            if (curCost == depth): #answer found
                if (curCost<self.mincost):
                    self.mincost = curCost
                    self.answer = path
                continue
            
            #transitions
            x,y = self.getZeroPos(curPuzzle)
            for dx,dy in self.dxy:
                if (not self.validIndex(x+dx, y+dy)):
                    continue
                newPuzzle = copy.deepcopy(curPuzzle)
                newPuzzle[x][y], newPuzzle[x+dx][y+dy] = newPuzzle[x+dx][y+dy], newPuzzle[x][y]
                newPath = copy.deepcopy(path)
                newPath.append((dx,dy))
                cost = self.calcCost(newPuzzle)
                pq.heappush(heap,(cost+depth+1, depth+1, newPuzzle, newPath))
        return "Puzzle berhasil diselesaikan"

pz = puzzlesolver("1.txt")
print(pz.answer)
print(pz.mincost)