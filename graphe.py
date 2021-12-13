import pandas as pd
import numpy as np
import math
import networkx as nx

df=pd.read_csv("coord_gps.csv")

prix_df=pd.read_csv("Data_prix.csv")
prix_df=prix_df.fillna(1000)
mat_prix=prix_df.to_numpy()
mat_prix1 = np.delete(mat_prix, 0, 1)
def path_weight_demoi(G, path):
    
    cost = 0

    if not nx.is_path(G, path):
        raise nx.NetworkXNoPath("path does not exist")
    for node, nbr in nx.utils.pairwise(path):
            cost += G[node][nbr][weight]
    return cost
G0=nx.Graph()
G0.add_nodes_from([ 0 , 1 , 2 , 3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42])
G0.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42),(11,20),(25,31)])
def chemin(i,j):
    return(nx.shortest_path(G0, source=i, target=j))

def grapheduchemin(i,j):
    Gij=nx.Graph()
    Gij.add_nodes_from(chemin(i,j))
    n=len(chemin(i,j))
    for k in range(n-1):
        for l in range (k+1,n):
            val1=chemin(i,j)[k]
            val2=chemin(i,j)[l]
            if Gij.has_edge(val1,val2)=='False':
                Gij.add_edges_from([(val1,val2,mat_prix1[val1,val2])])
    return(Gij)

def chemin_prix_min(i,j,k):
    G=grapheduchemin(i,j)
    L=[]
    for pa in nx.all_simple_paths(G, source=i, target=j, cutoff=k+1):
        L.append(path_weight_demoi(G,pa))
    m=min(L)
    for path1 in nx.all_simple_paths(G, source=i, target=j, cutoff=k+1):
        va=1000000
        p=0
        while va!=m:
            va=path_weight_demoi(G,path1)
            p=path1
    return(p,m)
        

    
   