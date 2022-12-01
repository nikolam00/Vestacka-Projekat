import re
import time
import sys

class Player:
    def __init__(self, Name , Znak):
        self.Name = Name
        self.Znak = Znak

class Board:
    def __init__(self, n : int, m : int):
        
        self.m = m
        self.n = n
        self.Tabla = {}

        for i in range(0,n):
            self.Tabla[i] = [None] * m 
    
class Game:
    
    def __init__(self):
        self.NaPotezu = 1   # 1,2 Kao koji od igraca je na potezu
        self.Player1 = None
        self.Player2 = None
        self.board = None
       
    def getStartState(self):

        sys.stdout.write("Unesite broj igraca: (1 ili 2) ")
        sys.stdout.flush()
        if(int(sys.stdin.readline(),10)==2):
            sys.stdout.write("Unesite ime igraca koji igra prvi: ")
            sys.stdout.flush()
            self.Player1=Player(sys.stdin.readline(),"X")

            sys.stdout.write("Unesite ime drugog igraca: ")
            sys.stdout.flush()
            self.Player2=Player(sys.stdin.readline(),"O")
        else:
            sys.stdout.write("Da li zelite da igrate prvi? Da/Ne ")
            sys.stdout.flush()
            if(sys.stdin.readline().lower()=="da"):
                sys.stdout.write("Unesite ime igraca: ")
                sys.stdout.flush()
                self.Player1=Player(sys.stdin.readline(),"X")
                self.Player2=Player("Racunar","Y")
            else:
                sys.stdout.write("Unesite ime igraca: ")
                sys.stdout.flush()
                self.Player1=Player("Racunar","X")
                self.Player2=Player(sys.stdin.readline(),"O")
                

        sys.stdout.write("Unesite broj vrsta table :")
        sys.stdout.flush()
        m = int(sys.stdin.readline())
        
        sys.stdout.write("Unesite broj kolona table :")
        sys.stdout.flush()
        n = int(sys.stdin.readline())

        self.board=Board(n,m)

    def PrintBoard(self):
        labVer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        labHor = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        
        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write(labHor[i]+ "   ")

        sys.stdout.write("\n")

        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write("=   ")   

        sys.stdout.write("\n")    
        
        for i in range(0,self.board.n):
            if(int(labVer[self.board.n-i])<=10):
                 sys.stdout.write(" ")
                
            sys.stdout.write(labVer[self.board.n-i - 1]+ " ǁ ")

            for j in range(0, self.board.m-1):
                if(self.board.Tabla[i][j]!=None):
                    sys.stdout.write(self.board.Tabla[i][j] + " | ")
                else:
                    sys.stdout.write("_ | ")
            j+=1
            if(self.board.Tabla[i][j]!=None):
                sys.stdout.write(self.board.Tabla[i][j] + " ǁ " + labVer[self.board.n-i - 1])
            else:
                sys.stdout.write("_ ǁ " + labVer[self.board.n-i - 1])
            
            sys.stdout.write("\n")
        
        
        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write("=   ") 
        sys.stdout.write("\n")
        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write(labHor[i]+ "   ")

        sys.stdout.flush()

    def IsValid(self,PozX,PozY):
        
        Polje=(self.board.n-PozX,ord(PozY)-ord("A"))

        if(self.NaPotezu==2):
            if(Polje[0]<0 or Polje[0]>self.board.n or Polje[1]<0 or Polje[1]>self.board.m-2):
                return False
            if(self.board.Tabla[Polje[0]][Polje[1]] != None or self.board.Tabla[Polje[0]][Polje[1]+1]!=None):
                return False
        else:
            if(Polje[0]<1 or Polje[0]>self.board.n or Polje[1]<0 or Polje[1]>self.board.m):
                return False
            if(self.board.Tabla[Polje[0]][Polje[1]] != None or self.board.Tabla[Polje[0]-1][Polje[1]]!=None):
                return False

        return True
    
    def PlayMove(self):

        sys.stdout.write("\n")
        sys.stdout.flush()
        sys.stdout.write("Unesite Vas potez:")
        sys.stdout.flush()
        
        PozX,PozY = sys.stdin.readline().split()
        PozX = int(PozX,10)

        if(self.IsValid(PozX,PozY)==True):
            Polje=(self.board.n-PozX,ord(PozY)-ord("A"))
            if(self.NaPotezu==1):
                self.board.Tabla[Polje[0]][Polje[1]]="X"
                self.board.Tabla[Polje[0]-1][Polje[1]]="X"
                self.NaPotezu=2
            else:
                self.board.Tabla[Polje[0]][Polje[1]]="O"
                self.board.Tabla[Polje[0]][Polje[1]+1]="O"
                self.NaPotezu=1
            
            return True
        else:
            sys.stdout.write("Uneli ste nevalidan potez, pokusajte ponovo!\n")
            sys.stdout.flush()
            return False

Igra=Game()
Igra.getStartState()
Igra.PrintBoard()

while(True):
    if(Igra.PlayMove()==True):
        Igra.PrintBoard()


Igra.PrintBoard()


                





        

        
    

        

        