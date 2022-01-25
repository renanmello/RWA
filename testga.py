import random
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
G = nx.Graph()

# criação da rede NFS
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14])
G.add_edges_from(
    [(1, 2), (1, 3), (1, 8), (2, 1), (2, 3), (2, 4), (3, 2), (3, 1), (3, 6), (4, 2), (4, 5), (4, 11), (5, 4)
        , (5, 6), (5, 7), (6, 3), (6, 5), (6, 10), (6, 13), (7, 5), (7, 8), (8, 1), (8, 7), (8, 9), (9, 8), (9, 10),
     (9, 12), (9, 14), (10, 6),(10, 9), (11, 4), (11, 12), (11, 14), (12, 9), (12, 11), (12, 13), (13, 6), (13, 12)
        , (13, 14), (14, 9),(14, 11),(14, 13)])

#requisições
request = [(1, 11), (1, 12), (1, 14), (2, 13)]

#primeira ilha criada
pop1 = random.sample(request, len(request))

paths = []
populacao = []
tampop = 50
countp = 0

#melhores rotas da fila de requisição da 1 ilha
for j in range(4):
    paths.append(list(nx.shortest_simple_paths(G, pop1[j][0], pop1[j][1])))

#seleciona os 4 melhores caminhos de cada requisicao
pathb=[paths[0][0:4],paths[1][0:4],paths[2][0:4],paths[3][0:4]]


#laco para criar a população inicial. 50 individuos criados
while(countp<tampop):
    cromossomo = []
    #criando cromossomos com 4 espaços de indices com valores aleatorios
    for x in range(4):
        test=[]
        for y in range(4):
            test.append(random.randrange(4))
    cromossomo.append(test)
    #adicionando os cromossomos criados na população
    for x in range(len(cromossomo)):
        populacao.append(cromossomo[x])
    countp=countp+1

#criando uma classe de matriz que irá guardar os comprimentos de onda e o tempo delas

class matrix:


    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0]*self.vertices for i in range(self.vertices)]
        self.time=3
        self.block=0
        self.desaloca=[]
    def adiciona_aresta(self, u, v):
        if(self.matrix[u-1][v-1]==0 and self.matrix[v-1][u-1]==0):
            self.matrix[u-1][v-1] = 1
            self.matrix[v-1][u-1] = 1
        else:
            return False
    def zera_aresta(self, u, v):
        self.matrix[u - 1][v - 1] = 0
        self.matrix[v - 1][u - 1] = 0

    #funcao para verificar se existe comprimento de onda disponivel por todo caminho
    def verifica_caminho(self, lista):
        walking=True

        for x in range(len(lista)):
            if(walking==False):
                return walking
            else:
                if (x < len(lista) - 1):

                    inicio = lista[x]
                    fim = lista[x + 1]

                    if (self.get_aresta(inicio, fim) == 0):
                        walking = True
                    else:
                        walking = False
            if (x == len(lista) - 1):
                if(walking==False):
                    return walking
                else:
                    inicio = lista[x - 1]
                    fim = lista[x]
                    if (self.get_aresta(inicio, fim) == 0):
                        return walking
                    else:
                        walking=False
                        return walking


    def mostra_matriz(self):
        print()
        for i in range(self.vertices):
            print(self.matrix[i])

    def remove_aresta(self, u, v):

        self.matrix[u-1][v-1] = 0
        self.matrix[v-1][u-v] = 0

    def get_aresta(self, u , v):
        return self.matrix[u-1][v-1]

    def add_time(self, u , v):
        if(self.matrix[u - 1][v - 1]==0 and self.matrix[v - 1][u - 1]==0):
            self.matrix[u - 1][v - 1] = self.matrix[u - 1][v - 1] + 3
            self.matrix[v - 1][u - 1] = self.matrix[v - 1][u - 1] + 3




     #funcao que irá diminuir o tempo
    def sub_time(self):

        for x in range(len(self.matrix)):
            for y in range(len(self.matrix)):

                if (self.matrix[x][y] == 1):
                    self.matrix[x][y] = 0
                    self.desaloca.append((x + 1, y + 1))
                    continue
                if (self.matrix[x][y] == 2):
                    self.matrix[x][y] = 1
                    continue
                if (self.matrix[x][y] == 3):
                    self.matrix[x][y] = 2
                    continue


    def timeout(self):
        if(self.time<0):
            return True
        if(self.time>=0):
            return False

class Individuo:
    def __init__(self, caminhos, id , cromossomo , fog , lambida):
        self.caminhos=caminhos
        self.id=id
        self.cromossomo=cromossomo
        self.fog=fog
        self.lambida=lambida


#criando matrizes de adjacencias com os comprimentos de onda e o tempo
nlist=G.nodes
w1=matrix(len(nlist))
w1t=matrix(len(nlist))
w2=matrix(len(nlist))
w2t=matrix(len(nlist))
w3=matrix(len(nlist))
w3t=matrix(len(nlist))
w4=matrix(len(nlist))
w4t=matrix(len(nlist))

#alocado primeiro cromossomo
nota=0
ranking=[]
std=[]
wave=0
block=[]
count1=0
count2=0
count3=0
count4=0

#laço para pegar os caminhos conformo o indice do gene do cromossomo
for x in range(len(populacao)):
    for y in range(4):
        std.append(pathb[y][populacao[x][y]])
print(std)

ciclo=0
wave=random.randrange(4)

for x in range(len(std)):

    if (ciclo == 4):
        ciclo = 0
        wave = random.randrange(4)
        w1t.sub_time()
        w2t.sub_time()
        w3t.sub_time()
        w4t.sub_time()

    if (ciclo < 4):
        ciclo = ciclo + 1

    if(len(w1t.desaloca) > 0):
        for q in range(len(w1t.desaloca)):
            w1.remove_aresta(w1t.desaloca[q][0], w1t.desaloca[q][1])

    if(len(w2t.desaloca) > 0):

        for q in range(len(w2t.desaloca)):
            w2.remove_aresta(w2t.desaloca[q][0], w2t.desaloca[q][1])

    if (len(w3t.desaloca) > 0):

        for q in range(len(w3t.desaloca)):
            w3.remove_aresta(w3t.desaloca[q][0], w3t.desaloca[q][1])

    if (len(w4t.desaloca) > 0):

        for q in range(len(w4t.desaloca)):
            w4.remove_aresta(w4t.desaloca[q][0], w4t.desaloca[q][1])

        w1t.desaloca = []
        w2t.desaloca = []
        w3t.desaloca = []
        w4t.desaloca = []
    for y in range(len(std[x])):

        if(wave==0):
            count1=count1+1
            if(w1.verifica_caminho(std[x])==False):
                w1.block=w1.block+1
                ranking.append(0)
                break

            else:

                ranking.append(1)
                for j in range(len(std[x])):

                    if (j < len(std[x]) - 1):
                        inicio = std[x][j]
                        fim = std[x][j + 1]

                        w1.adiciona_aresta(inicio, fim)
                        w1t.add_time(inicio,fim)

                break


                    #if (j == len(std[y]) - 1):
                    #    inicio = std[y][j-1]
                    #    fim = std[y][j]
                    #    w1.adiciona_aresta(inicio, fim)
                    #    w1t.add_time(inicio, fim)


        if (wave == 1):
            count2 = count2 + 1
            if (w2.verifica_caminho(std[x]) == False):
                w2.block = w2.block + 1
                ranking.append(0)
                break

            else:

                ranking.append(2)
                for j in range(len(std[x])):

                    if (j < len(std[x]) - 1):
                        inicio = std[x][j]
                        fim = std[x][j + 1]

                        w2.adiciona_aresta(inicio, fim)
                        w2t.add_time(inicio, fim)
                break



        if (wave == 2):
            count3 = count3 + 1
            if (w3.verifica_caminho(std[x]) == False):
                w3.block = w3.block + 1
                ranking.append(0)
                break

            else:
                ranking.append(3)
                for j in range(len(std[x])):

                    if (j < len(std[x]) - 1):
                        inicio = std[x][j]
                        fim = std[x][j + 1]

                        w3.adiciona_aresta(inicio, fim)
                        w3t.add_time(inicio, fim)
                break


        if (wave == 3):
            count4 = count4 + 1
            if (w4.verifica_caminho(std[x]) == False):
                w4.block = w4.block + 1
                ranking.append(0)
                break

            else:
                ranking.append(4)
                for j in range(len(std[x])):

                    if (j < len(std[x]) - 1):
                        inicio = std[x][j]
                        fim = std[x][j + 1]

                        w4.adiciona_aresta(inicio, fim)
                        w4t.add_time(inicio, fim)
                break

print("matriz w1 final")
w1.mostra_matriz()
print("matriz tempo1 final")
w1t.mostra_matriz()

print("matriz w2 final")
w2.mostra_matriz()
print("matriz tempo2 final")
w2t.mostra_matriz()

print("matriz w3 final")
w3.mostra_matriz()
print("matriz tempo3 final")
w3t.mostra_matriz()

print("matriz w4 final")
w4.mostra_matriz()
print("matriz tempo4 final")
w4t.mostra_matriz()



mediat=(w1.block+w2.block+w3.block+w4.block)/(count1+count2+count3+count4)
media1=w1.block/count1
media2=w2.block/count2
media3=w3.block/count3
media4=w4.block/count4
print("media total de bloqueio: ",mediat)
print("total de bloqueio w1:",w1.block)
print("media de bloqueio w1: ",media1)


print("total de bloqueio w2:",w2.block)
print("media de bloqueio w2: ",media2)

print("total de bloqueio w3:",w3.block)
print("media de bloqueio w3: ",media3)

print("total de bloqueio w4:",w4.block)
print("media de bloqueio w4: ",media4)

#nx.draw(G, with_labels=True)
#plt.show()

aux=[]
testr=[]
add=0
lambidas=[]
for x in range(len(ranking)):
    if(add<4):
        aux.append(ranking[x])
        add=add+1

    if(add==4):

        testr.append(aux)
        add=0
        aux=[]

aux2=0
aux3=0
mediar=[]

for x in range(len(testr)):
    maior=0
    for y in range(len(testr[x])):

        if(testr[x][y]>maior):
            maior=testr[x][y]

        else:
            maior=maior
    for y in range(len(testr[x])):
        aux2=aux2+testr[x][y]
    if(maior==0):
        mediar.append(0)
    else:
        mediar.append(aux2 / (maior * 4))
    aux2=0
    lambidas.append(maior)


