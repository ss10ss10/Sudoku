import random
import os

class board:
    
    def __init__(self,d):
        self.d = {
            1: [[4, 3, 5, 2, 6, 9, 7, 3, 1], [6, 8, 2, 5, 7, 1, 4, 9, 3], [1, 9, 7, 8, 3, 4, 5, 6, 2],
               [8, 2, 6, 1, 9, 5, 3, 4, 7], [3, 7, 4, 6, 8, 2, 9, 1, 5], [9, 5, 1, 7, 4, 3, 6, 2, 8],
               [5, 1, 9, 3, 2, 6, 8, 7, 4], [2, 4, 8, 9, 5, 7, 1, 3, 6], [7, 6, 3, 4, 1, 8, 2, 5, 9]],
            2: [[1, 5, 2, 4, 8, 9, 3, 7, 6], [7, 3, 9, 2, 5, 6, 8, 4, 1], [4, 6, 8, 3, 7, 1, 2, 9, 5],
               [3, 8, 7, 1, 2, 4, 6, 5, 9], [5, 9, 1, 7, 6, 3, 4, 2, 8], [2, 4, 6, 8, 9, 5, 7, 1, 3],
               [9, 1, 4, 6, 3, 7, 5, 8, 2], [6, 2, 5, 9, 4, 8, 1, 3, 7], [8, 7, 3, 5, 1, 2, 9, 6, 4]],
            3: [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]],
            4: [[9, 5, 7, 6, 1, 3, 2, 8, 4], [4, 8, 3, 2, 5, 7, 1, 9, 6], [6, 1, 2, 8, 4, 9, 5, 3, 7],
               [1, 7, 8, 3, 6, 4, 9, 5, 2], [5, 2, 4, 9, 7, 1, 3, 6, 8], [3, 6, 9, 5, 2, 8, 7, 4, 1],
               [8, 4, 5, 7, 9, 2, 6, 1, 3], [2, 9, 1, 4, 3, 6, 8, 7, 5], [7, 3, 6, 1, 8, 5, 4, 2, 9]],
            5: [[2, 7, 6, 3, 1, 4, 9, 5, 8], [8, 5, 4, 9, 6, 2, 7, 1, 3], [9, 1, 3, 8, 7, 5, 2, 6, 4],
               [4, 6, 8, 1, 2, 7, 3, 9, 5], [5, 9, 7, 4, 3, 8, 6, 2, 1], [1, 3, 2, 5, 9, 6, 4, 8, 7],
               [3, 2, 5, 7, 8, 9, 1, 4, 6], [6, 4, 1, 2, 5, 3, 8, 7, 9], [7, 8, 9, 6, 4, 1, 5, 3, 2]]}
        self.a = {
            1: [[(2,2),(1,2),(0,2)],[(5,3),(4,3),(3,3)],[(3,5),(2,5),(1,5)],[(6,6),(6,5),(6,4)]],
            2: [[(1,0),(0,1),(0,2)],[(3,1),(3,2),(3,3)],[(6,5),(7,4),(8,4),(8,5)],[(8,0),(7,0),(7,1)]],
            3: [[(1,1),(1,0),(2,0)],[(4,7),(3,6),(2,6)],[(4,7),(5,7),(4,8),(3,8)]],
            4: [[(7,2),(6,2),(6,3),(7,4)],[(0,2),(0,3),(0,4)],[(1,7),(1,6),(2,6),(2,7)],[(4,3),(4,2),(4,1),(5,0)]],
            5: [[(2,0),(1,1),(2,1),(2,2)],[(3,7),(3,6),(2,7),(1,7)],[(7,8),(8,7),(8,6),(8,5)]]
    }
        self.arrowLst = []
        self.dChoose=0
        self.lst = []
        self.solveLst = []
        self.remaining = 0
        self.populate(d)

    def populate(self, diff): # this function is called to populate the sudoku matrix. Every list at every index is populated with 1-9.
        if diff == 3: no_hints = random.randint(19,26)
        elif diff == 2: no_hints = random.randint(27,36)
        elif diff == 1: no_hints = random.randint(36,50)

        self.remaining = 81 - no_hints

#################################################### The following code is experimental and we will explain in viva############################################################################## 
        # the following code shuffles the matrix. At first it moves each row forward by an index then the columns and the matrix is transposed and reshuffled.
        # self.lst = [[(a + b) % 9 + 1 for a in range(1, 10)] for b in range(9)]
        # random.shuffle(self.lst)
        # self.lst = [[self.lst[row][column] for row in range(9)] for column in range(9)]
        # random.shuffle(self.lst)
############################################################################################################
        self.dChoose = random.randint(1,5)
        self.lst = self.d[self.dChoose]
        self.arrowLst = self.a[self.dChoose]
        # this code removes random indices by taking the row and column indices randomly and then storing them in a new list in the form (element, row, column)
        for i in range(self.remaining):
            r = random.randint(0,8)
            c = random.randint(0,8)
            n = self.remove(r,c)
            if isinstance(n, list):
                self.solveLst.append(n)

    def remain(self): # this method returns the remaining free spaces on the grid
        return self.remaining

    def setremain(self, b): # this method sets the variable with remaining free spaces
        self.remaining = b

    def check(self,n,r,c): # this check ensures the main rules of the game
        row, column = r, c
        if self.lst[row][column] != '-': # checks to see if the position we are trying to access is empty
            return False
        if n in self.lst[row]: # checks row to see if the element the user is trying to place is already in
            return False
        for i in range(9): # checks column to see if the element the user is trying to place is already in
            if self.lst[i][column] == n:
                return False
        # this piece of code checks to see if the element the user is trying to place is in the 3x3 box or not
        rr = row - (row%3)
        cc = column - (column%3)
        for i in range(3):
            for j in range(3):
                if self.lst[i+rr][j+cc] == n:
                    return False
        # this entire funtion returns False if either of the sudoku rules are not met else it returns True
        return True

    def checkArrows(self,n,r,c): # this function checks if the arrow conditions are met
        for i in self.arrowLst:
            if (r,c) not in i:
                return True
            else:
                if n == self.d[self.dChoose][r][c]:
                    return True
        return False

    def insert(self,n,r,c): # this function takes the user input values to the user input grid location and places it there if the parameters satisfy sudoku rules
        if r>=0 and c>=0 and r<9 and c<9 and self.check(n,r,c) and self.checkArrows(n,r,c):
            self.lst[r][c] = n
            self.remaining -= 1
        else:
            print("The move you are trying to make is invalid!")
        if self.remaining == 0: # after insertion, if there are no available spaces on the grid, the screen is cleared and the entire grid is redisplyed and the winning message is displayed
            os.system('cls || clear')
            self.display()
            print('Congratulations! You win')
            os.system('exit')
        
    def remove(self,r,c): # this funtion checks to see if the input row and column number are between 1-9 and the element the user is trying to remove is not '-'
        if r>=0 and c>=0 and r<9 and c<9 and self.lst[r][c] != '-':
            self.remaining-=1
            a = self.lst[r][c]
            self.lst[r][c] = '-'
            return [a,r,c]

    def solve(self): # this function takes the elements from the solveLst attribute of the sudoku class which has in itself the elements and their row and column numbers that were removed in the populate function. This allows the code to replace the same elements back into the array and solve the sudoku
        for i in range(len(self.solveLst)):
            n = self.solveLst[i][0]
            r = self.solveLst[i][1]
            c = self.solveLst[i][2]
            self.lst[r][c] = n
            self.remaining -= 1
        os.system('cls || clear')
        self.display()
        print('Congratulations! The computer solved the game!')
        os.system('exit')

    def display(self): # this function creates a grid layout and uses python string formating to place the values of the entire row into the grid in between the {} {} {} braces for a total of 3 times per row
        print('Arrow List')
        for i in self.arrowLst:
            print(i)
        print("_" * 37)
        for column, row in enumerate(self.lst):
            print(("|" + " {}   {}   {} |" * 3).format(*[node for node in row]))
            if column == 8:
                print("-" * 37)
            elif column % 3 == 2:
                print("|" + "---+" * 8 + "---|")
            else:
                print("|" + "   +" * 8 + "   |")

def main():
    diff = int(input('Enter difficulty: '))
    b = board(diff)
    b.display()
    ccnt = 0
    while ccnt<b.remain(): # The main runs until there are no free spaces in the grid
        x = int(input('Enter number to input (1-9, -1:Quit, 100:Solve, 200:Remove): '))
        if x == -1: break # Game terminating condition
        elif x == 100: # Game automatically solving condition
            b.solve()
            ccnt = b.remain()
            b.display()
        elif x == 200: # Removing condition
            r = int(input('Enter row to remove: '))
            c = int(input('Enter column to remove: '))
            b.solveLst.append(b.remove(r,c))
            b.display()
        else: # Any number between 1-9 and a valid row and ccolumn number will be accepted by this function
            r = int(input('Enter row to insert: '))
            c = int(input('Enter column to insert: '))
            b.insert(x,r,c)
            b.display()
        ccnt+=1
if __name__=='__main__':
    main()

    
