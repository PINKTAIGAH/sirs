import sys
from simulate import Simulate

def main():
    if len(sys.argv) != 6:
        raise Exception('Run file in command line as ==>\npython3 sirs.py [Lattice size] [p1] [p2] [p3] [Immunity]')
    
    N= int(sys.argv[1])
    p1= float(sys.argv[2])
    p2= float(sys.argv[3])
    p3= float(sys.argv[4])
    immunityBool= str(sys.argv[5])
    
    simulation= Simulate(N, p1, p2, p3, immunityBool)
    simulation.runSimulation()

if __name__ == '__main__':
    main()


