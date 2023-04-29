import sys

def main():
    if len(sys.argv) != 5:
        raise Exception('Run file in command line as ==>\npython3 sirs.py [Lattice size] [p1] [p2] [p3]')
    
    N= int(sys.argv[1])
    p1= float(sys.argv[2])
    p2= float(sys.argv[3])
    p3= float(sys.argv[4])


