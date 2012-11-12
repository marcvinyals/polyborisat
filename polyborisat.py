#!/usr/bin/env python
import time
# get cnf2ideal from ${POLYBORI_ROOT}/gui/cnf2ideal.py
from cnf2ideal import *
from polybori import *
start_time = time.time()
# cnf2ideal converts a dimacs cnf into polynomials readable by PyPolyBoRi
inp=process_input(sys.stdin)
clauses=gen_clauses(inp)
pbdata=gen_PB(clauses)
# pbdata is a python script that creates a variable `ideal`
exec(pbdata)
print "Loaded input in ",time.time()-start_time," seconds"
# cnf satisfiable iff 1 not in the ideal. owns_one_constant only works for groebner basis
gb=groebner_basis(ideal, selection_size=1000000)
print "Satisfiable:",not gbcore.owns_one_constant(gb)
print "Found an answer in ",time.time()-start_time," seconds"
