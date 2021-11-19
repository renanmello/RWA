import networkx as nx
import random
import numpy as np
G = nx.Graph()

#rede NFS
G.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11,12,13])
G.add_edges_from([(0,1),(0,2),(0,7),(1,0),(1,3),(1,2),(2,1),(2,0),(2,5),(3,1),(3,4),(3,10),(4,3)
,(4,5),(4,6),(5,2),(5,4),(5,9),(5,13),(6,4),(6,7),(7,0),(7,6),(7,8),(8,7),(8,9),(8,11),(9,5),(9,8),
(10,3),(10,11),(10,12),(11,8),(11,10),(11,13),(12,10),(12,13),(13,5),(13,11),(13,12)])





class masternode:
    #lista de requisições
    request=[(1,11),(1,12),(1,8),(2,13)]
    luk=request

    #faz o yen e guarda os caminhos
    paths0=list(nx.shortest_simple_paths(G, 1, 11))
    paths1=list(nx.shortest_simple_paths(G, 1, 12))
    paths2=list(nx.shortest_simple_paths(G, 1, 8))
    paths3=list(nx.shortest_simple_paths(G, 2, 13))
    
    #embaralhando e criando as populações
    pop1 = random.sample(request, len(request))


    pop2 = random.sample(request, len(request))



        
    #testes
    print("quantidade de caminhos:")
    quantidade_de_caminhos=len(paths0)
    print(quantidade_de_caminhos)
    print("Dados do grafo:")
    print(G)
    print("lista dos caminhos:")
    print(paths0)
    print("LUK: ", luk)
    print("pop1: ",pop1)
    print("pop2: ", pop2)

