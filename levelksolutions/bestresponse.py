# -*- coding: utf-8 -*-
"""
Implements Best Response Level-K calculations for SemiNFG and iterSemiNFG

Part of: PyNFG - a Python package for modeling and solving Network Form Games

Created on Fri May 24 07:01:05 2013

Copyright (C) 2013 James Bono (jwbono@gmail.com)

GNU Affero General Public License

"""


import copy
import numpy as np
from pynfg.utilities.utilities import convert_2_pureCPT, mceu

def bestresponse_node(Game, dn, N, delta=1, tol=30, verbose=False):
    """Compute level-k best response at the DN given Game
    
    :arg Game: the Network Form Game of interest
    :type Game: SemiNFG or iterSemiNFG
    :arg dn: the name of the decision node where MCEUs are estimated
    :type dn: str
    :arg N: the max number of iterations for the estimation
    :type N: int
    :arg tol: the minimum number of samples per parent value
    :type tol: int 
    
    """
    G = copy.deepcopy(Game)
    EUtable = mceu(G, dn, N, tol, delta, verbose)
    G.node_dict[dn].CPT = convert_2_pureCPT(EUtable)
    return G    