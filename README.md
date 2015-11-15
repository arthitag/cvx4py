# cvx4py
cvx like wrapper for cvxpy, to describe convex problems in english


example.py is the file the user writes, where he/she calls cvx4py to solve convex problems

cvx4py.py is the entry point. It calls cvxParser, which in turn calls cvxLexer



TODO:
1) implement cvxParser class
2) implement some useful functions in cvx4py like: checkConvex (that uses DCP rules to check if a problem is convex)
