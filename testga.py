import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()

# rede NFS
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
G.add_edges_from(
    [(0, 1), (0, 2), (0, 7), (1, 0), (1, 3), (1, 2), (2, 1), (2, 0), (2, 5), (3, 1), (3, 4), (3, 10), (4, 3)
        , (4, 5), (4, 6), (5, 2), (5, 4), (5, 9), (5, 13), (6, 4), (6, 7), (7, 0), (7, 6), (7, 8), (8, 7), (8, 9),
     (8, 11), (9, 5), (9, 8),
     (10, 3), (10, 11), (10, 12), (11, 8), (11, 10), (11, 13), (12, 10), (12, 13), (13, 5), (13, 11), (13, 12)])
nx.draw(G, with_labels=True)
plt.show()


class masternode:
    # lista de requisições
    request = [(1, 11), (1, 12), (1, 8), (2, 13)]

    # faz o yen e guarda os caminhos
    paths0 = list(nx.shortest_simple_paths(G, 1, 11))
    paths1 = list(nx.shortest_simple_paths(G, 1, 12))
    paths2 = list(nx.shortest_simple_paths(G, 1, 8))
    paths3 = list(nx.shortest_simple_paths(G, 2, 13))

    # tabela de menores caminhos
    luk = [paths0[0], paths1[0], paths2[0]]

    # embaralhando e criando as populações
    pop1 = random.sample(request, len(request))
    pop2 = random.sample(request, len(request))
    pop3 = random.sample(request, len(request))


    pop11=list(nx.shortest_simple_paths(G, pop1[0][0], pop1[0][1]))
    pop11= random.sample(pop11, len(pop11))


    # testes
    print("pop11", pop11)
    print("quantidade de caminhos:")
    quantidade_de_caminhos = len(paths0)
    print(quantidade_de_caminhos)
    print("Dados do grafo:")
    print(G)
    print("lista dos caminhos:")
    print(paths0)
    print("LUK: ", luk)
    print("pop1: ", pop1)
    print("pop2: ", pop2)
    print("quantidade do primeiro elemento", len(paths0[0]))
    print("arestas",G.edges())


    #criando um dicionario para alocação de onda
    list=G.edges
    dict={}
    for x in range(len(list)):
        dict[x]=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),
                       random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]

    print(dict.values())
    print(dict.keys())

    CHANCE_MUT = .20
    CHANCE_CO = .25
    NUM_INDIVIDUOS = len(pop11)
    NUM_MELHORES = 4

    for x in NUM_INDIVIDUOS:

