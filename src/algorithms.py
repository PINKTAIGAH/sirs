import numpy as np

class Algorithms(object):
#==============================================================
#  Class comtainiing algorithms for SIRS model simulation

    def __init__(self, N, p1, p2, p3):
        #======================================================
        # Constructor to define all inital parameters of the class

        self.N= N
        self.p1= p1
        self.p2= p2
        self.p3= p3

    