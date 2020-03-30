from itertools import product
import numpy as np

# --- Cell & Neighbors information Extaction ---
cellColor = lambda x, i, j: x[i, j]
# get the pattern that the neighbors draw in a list
neighPattern = lambda x, i, j: np.array([ x[i+ip, j+jp] for ip, jp in product([1, -1, 0], repeat=2) if 0 <= i+ip < x.shape[0] and 0 <= j+jp < x.shape[1] ])
# [upper_neigh_value, cell_value, lower_neigh_value]
verticalLine = lambda x, i, j: np.array(x[i-(1 if i>0 else 0):i+1+(0 if i==x.shape[1] else 1),j])
# [left_neigh_value, cell_value, right_neigh_value]
horizontalLine = lambda x, i, j: np.array(x[i,j-(1 if j>0 else 0):j+1+(0 if j==x.shape[0] else 1)])
# [bottom_left_neigh_value, cell_value, top_right_neigh_value]
bl_trDiagonal = lambda x, i, j: np.array([ x[i+ip,j+jp] for ip, jp in [(1,-1),(0,0),(-1,1)] if 0<=i+ip<x.shape[0] and 0<=j+jp<x.shape[1] ])
# [top_left_neigh_value, cell_value, bottom_right_neigh_value]
tl_brDiagonal = lambda x, i, j: np.array([ x[i+ip,j+jp] for ip, jp in [(-1,-1),(0,0),(1,1)] if 0<=i+ip<x.shape[0] and 0<=j+jp<x.shape[1] ])

# applications / modifications (lambda x: x)(A) =? B
