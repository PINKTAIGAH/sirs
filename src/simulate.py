import numpy as np
from time import time 
from animate import Animate
from algorithms import Algorithms
from initialLattices import InitialLattcie

class Simulate(object):
#==============================================================
# Class to initialise and run SIRS simulation

    def __init__(self, N, p1, p2, p3, immuneBool):
        #======================================================
        # Constructor to define initial parameters for SIRS simulation

        self.N= N
        self.p1= p1
        self.p2= p2
        self.p3= p3
        
        self.sweep=0
        self.timestep=0
        self.timestepLimit= self.N**2
        self.visPeriod= 10
        self.immuneBool= immuneBool

    def createArray(self):
        #=======================================================
        # Create inital array dependant on immunity criteria

        if self.immuneBool == str('true'):
            self.array= self.initialLattcie.generateImmunityLattice()
        else:
            self.array= self.initialLattcie.generateRegularLattice()
    
    def updateVisualisation(self):
        #+======================================================
        # Update visualisation every 10 sweeps

        if self.timestep % self.timestepLimit*self.visPeriod == 0:
            self.animation.drawImage(self.array)

    def writeOutData(self):
        #========================================================
        # Write relevant data to file

        with open('../data/visualisationData.csv', 'ab') as f:
            #f.write(b'\n')
            np.savetxt(f, np.array([[1]]), delimiter= ',', fmt= '%d')

    def runSimulation(self):
        #=======================================================
        # Run SIRS simulation with visualisation

        self.initialLattcie= InitialLattcie(self.N)
        self.algorithms= Algorithms(self.N, self.p1, self.p2, self.p3)
        self.createArray()
        self.animation= Animate(self.array, colourmap= 'seismic')

        while True:
            self.array= self.algorithms.updateArray(self.array)
            self.timestep +=1
            if self.timestep % self.timestepLimit == 0:
                self.sweep+= 1
            self.updateVisualisation()



    


    

