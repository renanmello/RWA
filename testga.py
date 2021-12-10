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

#plt.show()


class masternode:
    # lista de requisições
    request = [(1, 11), (1, 12), (1, 8), (2, 13)]

    # faz o yen e guarda os caminhos
    # 5 melhores melhores caminhos sem precisar embaralhar
    paths0 = list(nx.shortest_simple_paths(G, 1, 11))
    paths1 = list(nx.shortest_simple_paths(G, 1, 12))
    paths2 = list(nx.shortest_simple_paths(G, 1, 8))
    paths3 = list(nx.shortest_simple_paths(G, 2, 13))

    # tabela de menores caminhos
    luk = [paths0[0], paths1[0], paths2[0], paths3[0]]

    # embaralhando e criando as populações de requisicoes
    master = request
    lukmaster = [paths0[0:4], paths1[0:4], paths2[0:4], paths3[0:4]]

    pop1 = random.sample(request, len(request))
    pop2 = random.sample(request, len(request))
    pop3 = random.sample(request, len(request))
    pop4 = random.sample(request, len(request))

    print("pop", pop1)
    print("luk master", lukmaster)
    # criando os individuos e populacao de individuos

    individuo = []
    individuo2= []
    individuo3=[]
    individuo4=[]
    populacao = []
    pathi=[]


    for j in range(4):
        pathi.append(list(nx.shortest_simple_paths(G, pop1[j][0], pop1[j][1])))


    print("pathi>>",pathi)
    pathi0 = list(nx.shortest_simple_paths(G, pop1[0][0], pop1[0][1]))
    pathi1 = list(nx.shortest_simple_paths(G, pop1[1][0], pop1[1][1]))
    pathi2 = list(nx.shortest_simple_paths(G, pop1[2][0], pop1[2][1]))
    pathi3 = list(nx.shortest_simple_paths(G, pop1[3][0], pop1[3][1]))

    individuo.append(pathi0[random.randrange(len(pathi0))])
    individuo.append(pathi1[random.randrange(len(pathi1))])
    individuo.append(pathi2[random.randrange(len(pathi2))])
    individuo.append(pathi3[random.randrange(len(pathi3))])

    for j in range(4):
        individuo2.append(pathi[j][random.randrange(len(pathi[j]))])
        individuo3.append(pathi[j][random.randrange(len(pathi[j]))])
        individuo4.append(pathi[j][random.randrange(len(pathi[j]))])



    #individuo2.append((pathi[0][random.randrange(len(pathi[0]))]))


    print("path0", pathi0)
    print("individuos",individuo)
    print("individuo teste", individuo2)
    populacao.append(individuo)
    populacao.append(individuo2)
    populacao.append(individuo3)
    populacao.append(individuo4)


    print("População :",populacao)



    # testes
    # print("pop11", pop11)
    # print("quantidade de caminhos:")
    # quantidade_de_caminhos = len(paths0)
    # print(quantidade_de_caminhos)
    # print("Dados do grafo:")
    # print(G)
    # print("lista dos caminhos:")
    # print(paths0)
    # print("LUK: ", luk)
    # print("pop1: ", pop1)
    # print("pop2: ", pop2)
    # print("quantidade do primeiro elemento", len(paths0[0]))
    # print("arestas",G.edges())
    # print(paths0)
    # criando um dicionario para alocação de onda
    #pop11 = list(nx.shortest_simple_paths(G, pop1[0][0], pop1[0][1]))
    #luk11 = pop11[0]
    #count11 = len(luk11)
    # print("luk11", luk11)
    #pop11 = random.sample(pop11, len(pop11))

    list = G.edges
    dict = {}

    # print("lista", list)
    for x in range(len(list)):
        dict[x] = [0, 0, 0, 0, 0, 0, 0, 0]
        # dict[x]=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),
        #               random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]

    # print(dict.values())
    # print(dict.keys())
    # print('pop11', pop11)
    # print('luk11', luk11)
    # print(count11)

    CHANCE_MUT = .20
    CHANCE_CO = .25
    NUM_INDIVIDUOS = len(pop11)
    NUM_MELHORES = 4
    TIME_SPEND = 3
    bests = []
    fbests = []

    ''''
    for x in range(NUM_INDIVIDUOS):
        wave=random.randint(0,7)
        print("wave",wave)
        for y in range(len(pop11[x])):
            for z in dict.values():
                print("zwave",z[wave])
                z[wave]=0
                #print("z>>>", z)
                dict[wave]=z
                print("Dict",dict)

    for x in range(NUM_INDIVIDUOS):
        function=count11-len(pop11[x])
        if function==0:
            bests.append(pop11[x])
    '''''
