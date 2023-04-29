import numpy as np

class InitialLattcie(object):
#==============================================================
# Class to generate initial lattice for sirs simulation

    def __init__(self, N, pImmunity= 0.5):
        #======================================================
        # Constructor to define inital parameters for class

        self.N= N
        self.pImmunity= pImmunity
    
    def generateRegularLattice(self):
        #======================================================
        # Return array with each state of SIRS model distributed with equal
        # probability

        lattice= np.random.choice(np.array([0, 1, 2]), size=(self.N, self.N))
        return lattice

    def generateImmunityLattice(self):
        #======================================================
        # Return array with each state of SIRS model and elements with immunity 
        # distributed with equal probability

        self.pOther= (1-self.pImmunity)/3
        lattice= np.random.choice(np.array([0,1,2,3]), size=(self.N ,self.N),\
                            p= np.array([self.pOther, self.pOther, self.pOther, self.pImmunity])) 
        return lattice    

if __name__ == '__main__':
    initialLattcie= InitialLattcie(10, 0.2)
    print(initialLattcie.generateImmunityLattice())
