import numpy

class Observable(object):
#================================================================
# Class to claculate observables of SIRS model

    def findInfectedFraction(array):
        #========================================================
        # Find the infection fraction of a SIRS array for a given timestep

        return array[array == 1].size/array.size