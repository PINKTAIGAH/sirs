import numpy as np

class Algorithms(object):
#==============================================================
# Class comtainiing algorithms for SIRS model simulation
# Keys for SIRS array:
# 0 ==> (S)ucceptable
# 1 ==> (I)nfected
# 2 ==> (R)ecovered
# 3 ==> (Im)mune

    def __init__(self, N, p1, p2, p3):
        #======================================================
        # Constructor to define all inital parameters of the class

        self.N= N
        self.p1= p1
        self.p2= p2
        self.p3= p3
        self.sirsey= {  0:'S', 1:'I', 2:'R', 3:'V'}

    def generateRandomIndex(self):
        #======================================================
        # Generate a random index within the bounds of an array

        self.index= tuple(np.random.randint(0, high= self.N, size= 2))

    def periodic_boundaries(self):
        #=======================================================
        # Apply periodic boundaries to neighbour indices if necesary
        self.neighbourList= [self.iU, self.iD, self.iL, self.iR]
        
        for i in range(len(self.neighbourList)):
            if (self.neighbourList[i][0]) >= self.N:
                self.neighbourList[i][0]= 0
            if (self.neighbourList[i][1]) >= self.N:
                self.neighbourList[i][1]= 0    
        self.neighbourList= tuple(self.neighbourList) 

    def findNearestNeighbours(self):
        #=======================================================
        # Return indices of nearest neighbours of a lattice points
        
        self.iD, self.iU= [self.index[0]+1, self.index[1]], [self.index[0]-1, self.index[1]]
        self.iL, self.iR= [self.index[0], self.index[1]-1], [self.index[0], self.index[1]+1]
        self.periodic_boundaries()

    def findNeigbourStates(self):
        #=======================================================
        # Return list containing state of neighbour cells
        self.findNearestNeighbours()
        self.neigbourVals= [self.array[i[0]][i[1]] for i in [self.iU, self.iD, self.iL, self.iR]]
        self.neigbourStates= [self.sirsKey[i] for i in tuple(self.neigbourVals)]

#    def findNeighbourStates(self):
        #======================================================
        # Find the state of neighbours for randomly selected array element

        self.U= np.roll(self.array, -1, axis=0)[self.index]
        self.D= np.roll(self.array, +1, axis=0)[self.index]
        self.R= np.roll(self.array, +1, axis=1)[self.index]
        self.L= np.roll(self.array, -1, axis=1)[self.index]

    def isInfected(self):
        #======================================================
        # Return boolean stating if neighbour of state is infected

        self.infectedNeighbour= False
        if str('I') in self.neigbourStates:
            self.infectedNeighbour= True

    def isSucceptable(self):
        #======================================================
        # Return boolean stating if neighbour of state is succeptable

        self.succeptableNeighbour= self.U == 0 & self.D == 0 & self.R == 0 & self.L == 0

    def isRecovered(self):
        #======================================================
        # Return boolean stating if neighbour of state is succeptable

        self.recoveredNeighbour= self.U == 2 & self.D == 2 & self.R == 2 & self.L == 2

    def applySirsRuleS(self):
        #======================================================
        # Apply dedicated SIRS rule for a succeptable element

        if self.infectedNeighbour and np.random.rand() <= self.p1:
            self.array[self.index] = 1
        
    def applySirsRuleI(self):
        #======================================================
        # Apply dedicated SIRS rule for a succeptable element

        if np.random.rand() <= self.p2:
            self.array[self.index] = 2

    def applySirsRuleR(self):
        #======================================================
        # Apply dedicated SIRS rule for a succeptable element

        if np.random.rand() <= self.p3:
            self.array[self.index] = 1

    def updateArray(self, array):
        # =====================================================
        # Update array according to SIRS model rules.

        self.array= array
        self.generateRandomIndex()
        self.findNeigbourStates()

        if self.array[self.index] == 0:
            self.isInfected()
            self.applySirsRuleS()
        
        elif self.array[self.index] == 1:
            self.applySirsRuleI()

        elif self.array[self.index] == 2:
            self.applySirsRuleR()

        return self.array


