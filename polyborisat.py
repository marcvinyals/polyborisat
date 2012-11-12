#!/usr/bin/env python
import argparse
import time

# get cnf2ideal from ${POLYBORI_ROOT}/gui/cnf2ideal.py
from cnf2ideal import *
from polybori import *

def solvecnf(file,args) :
    start_time = time.time()

    # cnf2ideal converts a dimacs cnf into polynomials readable by PyPolyBoRi
    inp=process_input(file)
    clauses=gen_clauses(inp)
    pbdata=gen_PB(clauses)

    # pbdata is a python script that creates a variable `ideal`
    exec(pbdata)
    print "Loaded input in {} seconds".format(time.time()-start_time)

    # cnf satisfiable iff 1 not in the ideal. owns_one_constant only works for groebner basis
    gb=groebner_basis(ideal, **args)
    print "Satisfiable: {}".format(not gbcore.owns_one_constant(gb))
    print "Found an answer in {} seconds".format(time.time()-start_time)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("cnf",type=argparse.FileType('r'),help="File with a CNF formula, - for stdin")
    parser.add_argument("polyboriargs",nargs='*',help="Arguments to pass to groebner_basis(), in a key=value format")
    args=parser.parse_args()
    polyboriargs=dict((key,eval(value)) for key,value in [arg.split('=') for arg in args.polyboriargs])
    solvecnf(args.cnf,polyboriargs)

#TODO: add defaults (eg: selection_size=1000000)
