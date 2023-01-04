import re
import time
import sys
import copy

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
        self.finished=False
        self.Pobednik = None
       
    def GetStartState(self):

        sys.stdout.write("Broj igrača (1 ili 2): ")
        sys.stdout.flush()
        if(int(input(),10)==2):
            sys.stdout.write("Prvi igrač: ")
            sys.stdout.flush()
            self.Player1=Player(input(),"X")

            sys.stdout.write("Drugi igrač: ")
            sys.stdout.flush()
            self.Player2=Player(input(),"O")
        else:
            sys.stdout.write("Da li želite da igrate prvi? Da/Ne ")
            sys.stdout.flush()
            if(str(input().lower())=="da"):
                sys.stdout.write("Igrač: ")
                sys.stdout.flush()
                self.Player1=Player(input(),"X")
                self.Player2=Player("Računar","O")
            else:
                sys.stdout.write("Igrač: ")
                sys.stdout.flush()
                self.Player1=Player("Računar","X")
                self.Player2=Player(input(),"O")
                
                

        sys.stdout.write("Broj vrsta table: ")
        sys.stdout.flush()
        n = int(input())
        
        sys.stdout.write("Broj kolona table: ")
        sys.stdout.flush()
        m = int(input())

        self.board=Board(n,m)
        self.labVer = [str(i) for i in range(1,self.board.n+2)]
        self.labHor = [chr(i) for i in range(ord("A"),ord("A")+self.board.m+1)]
    
    def PrintBoard(self):

        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write(self.labHor[i]+ "   ")

        sys.stdout.write("\n")

        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write("=   ")   

        sys.stdout.write("\n")    
        
        for i in range(0,self.board.n):
            if(int(self.labVer[self.board.n-i])<=10):
                 sys.stdout.write(" ")
                
            sys.stdout.write(self.labVer[self.board.n-i - 1]+ " ǁ ")

            for j in range(0, self.board.m-1):
                if(self.board.Tabla[i][j]!=None):
                    sys.stdout.write(self.board.Tabla[i][j] + " | ")
                else:
                    sys.stdout.write("_ | ")
            j+=1
            if(self.board.Tabla[i][j]!=None):
                sys.stdout.write(self.board.Tabla[i][j] + " ǁ " + self.labVer[self.board.n-i - 1])
            else:
                sys.stdout.write("_ ǁ " + self.labVer[self.board.n-i - 1])
            
            sys.stdout.write("\n")
        
        
        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write("=   ") 
        sys.stdout.write("\n")
        sys.stdout.write("     ")
        for i in range(0,self.board.m):
            sys.stdout.write(self.labHor[i]+ "   ")

        sys.stdout.flush()

    def IsValid(self,PozX,PozY):

        if PozX not in self.labVer:
            return False
        if PozY not in self.labHor:
            return False
        PozX=int(PozX)
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
        
        igrac = self.Player1.Name if self.NaPotezu==1 else self.Player2.Name

        sys.stdout.write('Na potezu: {} Vaš potez:'.format(igrac))
        sys.stdout.flush()
        
        PozX,PozY = input().upper().split()

        if(self.IsValid(PozX,PozY)==True):
            PozX = int(PozX,10)
            Polje=(self.board.n-PozX,ord(PozY)-ord("A"))
            if(self.NaPotezu==1):
                self.board.Tabla[Polje[0]][Polje[1]]="X"
                self.board.Tabla[Polje[0]-1][Polje[1]]="X"
                self.NaPotezu=2
                if(self.CheckEndGame()):
                    self.EndOfGame()
            else:
                self.board.Tabla[Polje[0]][Polje[1]]="O"
                self.board.Tabla[Polje[0]][Polje[1]+1]="O"
                self.NaPotezu=1
                if(self.CheckEndGame()):
                    self.EndOfGame()
            
            return True
        else:
            sys.stdout.write("Nevalidan potez, pokušajte ponovo!\n")
            sys.stdout.flush()
            return False

    def CheckEndGame(self):
        
        if(self.NaPotezu==1):
            for j in range(0,self.board.m):
                i=1 #Krecemo od prve vrste
                while i<self.board.n:
                    if(self.board.Tabla[i][j]==None):
                        if(self.board.Tabla[i-1][j]==None):
                            return False   
                        else:
                            i+=1
                    else:
                        i+=2
        else:
            for i in range(0,self.board.n):
                j=0
                while j<self.board.m-1:
                    if(self.board.Tabla[i][j+1]==None):
                        if(self.board.Tabla[i][j]==None):
                            return False   
                        else:
                            j+=1
                    else:
                        j+=2
        return True

    def CheckEndGame(naPotezu,board):
        
        if(naPotezu==1):
            for j in range(0,board.m):
                i=1 #Krecemo od prve vrste
                while i<board.n:
                    if(board.Tabla[i][j]==None):
                        if(board.Tabla[i-1][j]==None):
                            return False   
                        else:
                            i+=1
                    else:
                        i+=2
        else:
            for i in range(0,board.n):
                j=0
                while j<board.m-1:
                    if(board.Tabla[i][j+1]==None):
                        if(board.Tabla[i][j]==None):
                            return False   
                        else:
                            j+=1
                    else:
                        j+=2
        return True

    def EndOfGame(self):
        self.finished=True
        if(self.NaPotezu==1):
            self.Pobednik=self.Player2
        else:
            self.Pobednik=self.Player1
    
    def PlayGame(self):
        while(not self.finished):
            
            

            if(self.PlayMove()==True):
                self.PrintBoard()

        if(self.Pobednik==self.Player1):
            sys.stdout.write('\nPobednik je igrač 1: {}\n'.format(self.Player1.Name))
        else:
            sys.stdout.write('\nPobednik je igrač 2: {}\n'.format(self.Player2.Name))
        
    def AvailableMoves(self)->set:
        Moves = set()
        if(self.NaPotezu==1):
            for j in range(0,self.board.m):
                i=1 #Krecemo od prve vrste
                while i<self.board.n:
                    if(self.board.Tabla[i][j]==None):
                        if(self.board.Tabla[i-1][j]==None):
                            Moves.add((self.labVer[self.board.n-1-i],self.labHor[j]))
                            i+=1
                        else:
                            i+=1
                    else:
                        i+=2
        else:
            for i in range(0,self.board.n):
                j=0
                while j<self.board.m-1:
                    if(self.board.Tabla[i][j+1]==None):
                        if(self.board.Tabla[i][j]==None):
                            Moves.add((self.labVer[self.board.n-1-i],self.labHor[j]));  
                            j+=1
                        else:
                            j+=1
                    else:
                        j+=2

        return Moves

    def AvailableStates(self)->dict:
        
        Moves = self.AvailableMoves()
        NewStates = dict()

        if(self.NaPotezu==1):
            for x in Moves:
                NovaTabla = copy.deepcopy(self.board.Tabla)

                PozX = self.board.n-int(x[0],10)
                PozY=ord(x[1])-ord("A")

                NovaTabla[PozX][PozY]="X"
                NovaTabla[PozX-1][PozY]="X"

                NewStates[x]=NovaTabla
        else:
            for x in Moves:
                NovaTabla = copy.deepcopy(self.board.Tabla)

                PozX = self.board.n-int(x[0],10)
                PozY=ord(x[1])-ord("A")

                NovaTabla[PozX][PozY]="O"
                NovaTabla[PozX][PozY+1]="O"

                NewStates[x]=NovaTabla

        return NewStates

Igra=Game()
Igra.GetStartState()
Igra.PrintBoard()
Igra.PlayGame()