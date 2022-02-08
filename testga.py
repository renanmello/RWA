import random
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

G = nx.Graph()

# criação da rede NFS
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
G.add_edges_from(
    [(1, 2), (1, 3), (1, 8), (2, 1), (2, 3), (2, 4), (3, 2), (3, 1), (3, 6), (4, 2), (4, 5), (4, 11), (5, 4)
        , (5, 6), (5, 7), (6, 3), (6, 5), (6, 10), (6, 13), (7, 5), (7, 8), (8, 1), (8, 7), (8, 9), (9, 8), (9, 10),
     (9, 12), (9, 14), (10, 6), (10, 9), (11, 4), (11, 12), (11, 14), (12, 9), (12, 11), (12, 13), (13, 6), (13, 12)
        , (13, 14), (14, 9), (14, 11), (14, 13)])

# requisições
#randomica
request = [(1, 11), (1, 12), (1, 14), (2, 13)]


# primeira ilha criada
pop1 = random.sample(request, len(request))

paths = []
populacao = []
tampop = 50
countp = 0

# melhores rotas da fila de requisição da 1 ilha
for j in range(4):
    paths.append(list(nx.shortest_simple_paths(G, pop1[j][0], pop1[j][1])))

# seleciona os 4 melhores caminhos de cada requisicao
pathb = [paths[0][0:4], paths[1][0:4], paths[2][0:4], paths[3][0:4]]

# laco para criar a população inicial. 50 individuos criados
while (countp < tampop):
    cromossomo = []
    # criando cromossomos com 4 espaços de indices com valores aleatorios
    for x in range(4):
        test = []
        for y in range(4):
            test.append(random.randrange(4))
    cromossomo.append(test)
    # adicionando os cromossomos criados na população
    for x in range(len(cromossomo)):
        populacao.append(cromossomo[x])
    countp = countp + 1


# criando uma classe de matriz que irá guardar os comprimentos de onda e o tempo delas

class matrix:

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * self.vertices for i in range(self.vertices)]
        self.time = 3
        self.block = 0
        self.desaloca = []

    def adiciona_aresta(self, u, v):
        if (self.matrix[u - 1][v - 1] == 0 and self.matrix[v - 1][u - 1] == 0):
            self.matrix[u - 1][v - 1] = 1
            self.matrix[v - 1][u - 1] = 1
        else:
            return False

    def zera_aresta(self, u, v):
        self.matrix[u - 1][v - 1] = 0
        self.matrix[v - 1][u - 1] = 0

    # funcao para verificar se existe comprimento de onda disponivel por todo caminho
    def verifica_caminho(self, lista):
        walking = True

        for x in range(len(lista)):
            if (walking == False):
                return walking
                break
            else:
                if (x < len(lista) - 1):

                    inicio = lista[x]
                    fim = lista[x + 1]

                    if (self.get_aresta(inicio, fim) == 0):
                        walking = True
                    else:
                        walking = False
                        return walking
                        break
                if (x == len(lista) - 1):
                    if (walking == False):
                        return walking
                        break
                else:
                    inicio = lista[x - 1]
                    fim = lista[x]
                    if (self.get_aresta(inicio, fim) == 0):
                        walking=True
                        return walking
                        break
                    else:
                        walking = False
                        return walking
                        break

    def mostra_matriz(self):
        print()
        for i in range(self.vertices):
            print(self.matrix[i])

    def remove_aresta(self, u, v):

        self.matrix[u - 1][v - 1] = 0
        self.matrix[v - 1][u - v] = 0

    def get_aresta(self, u, v):
        return self.matrix[u - 1][v - 1]

    def add_time(self, u, v):
        if (self.matrix[u - 1][v - 1] == 0 and self.matrix[v - 1][u - 1] == 0):
            self.matrix[u - 1][v - 1] = self.matrix[u - 1][v - 1] + 3
            self.matrix[v - 1][u - 1] = self.matrix[v - 1][u - 1] + 3

    # funcao que irá diminuir o tempo
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
        if (self.time < 0):
            return True
        if (self.time >= 0):
            return False


class Individuo:
    def __init__(self, requisicoes, caminhos, id, cromossomo, fog, lambida, n_saltos):
        self.caminhos = caminhos
        self.id = id
        self.cromossomo = cromossomo
        self.fog = fog
        self.lambida = lambida
        self.requisicoes = requisicoes
        self.n_saltos = n_saltos


# criando matrizes de adjacencias com os comprimentos de onda e o tempo
nlist = G.nodes
w1 = matrix(len(nlist))
w1t = matrix(len(nlist))
w2 = matrix(len(nlist))
w2t = matrix(len(nlist))
w3 = matrix(len(nlist))
w3t = matrix(len(nlist))
w4 = matrix(len(nlist))
w4t = matrix(len(nlist))

# alocado primeiro cromossomo
ranking = []
std = []
wave = 0
block = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

# laço para pegar os caminhos conformo o indice do gene do cromossomo
for x in range(len(populacao)):
    for y in range(4):
        std.append(pathb[y][populacao[x][y]])
# print(std)

ciclo = 0
wave = random.randrange(4)




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

    if (len(w1t.desaloca) > 0):
        for q in range(len(w1t.desaloca)):
            w1.remove_aresta(w1t.desaloca[q][0], w1t.desaloca[q][1])



    if (len(w2t.desaloca) > 0):

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

        if (wave == 0):
            count1 = count1 + 1
            if (w1.verifica_caminho(std[x]) == False):
                w1.block = w1.block + 1
                ranking.append(0)
                break

            else:

                ranking.append(1)

                for j in range(len(std[x])):

                    if (j < len(std[x]) - 1):
                        inicio = std[x][j]
                        fim = std[x][j + 1]

                        w1.adiciona_aresta(inicio, fim)

                        w1t.add_time(inicio, fim)

                break

                # if (j == len(std[y]) - 1):
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

# print("matriz w1 final")
# w1.mostra_matriz()
# print("matriz tempo1 final")
# w1t.mostra_matriz()

# print("matriz w2 final")
# w2.mostra_matriz()
# print("matriz tempo2 final")
# w2t.mostra_matriz()

# print("matriz w3 final")
# w3.mostra_matriz()
# print("matriz tempo3 final")
# w3t.mostra_matriz()

# print("matriz w4 final")
# w4.mostra_matriz()
# print("matriz tempo4 final")
# w4t.mostra_matriz()


mediat = (w1.block + w2.block + w3.block + w4.block) / (count1 + count2 + count3 + count4)
media1 = w1.block / count1
media2 = w2.block / count2
media3 = w3.block / count3
media4 = w4.block / count4

# print("media total de bloqueio: ",mediat)
# print("total de bloqueio w1:",w1.block)
# print("media de bloqueio w1: ",media1)


# print("total de bloqueio w2:",w2.block)
# print("media de bloqueio w2: ",media2)

# print("total de bloqueio w3:",w3.block)
# print("media de bloqueio w3: ",media3)

# print("total de bloqueio w4:",w4.block)
# print("media de bloqueio w4: ",media4)

# nx.draw(G, with_labels=True)
# plt.show()

aux = []
testr = []
add = 0
lambidas = []

for x in range(len(ranking)):
    if (add < 4):
        aux.append(ranking[x])
        add = add + 1

    if (add == 4):
        testr.append(aux)
        add = 0
        aux = []
#print("tester",testr)
aux2 = 0

mediar = []

for x in range(len(testr)):
    maior = 0
    for y in range(len(testr[x])):

        if (testr[x][y] > maior):
            maior = testr[x][y]

        else:
            maior = maior
    for y in range(len(testr[x])):
        aux2 = aux2 + testr[x][y]
    if (maior == 0):
        mediar.append(0)
    else:
        mediar.append(aux2 / (maior * 4))
    aux2 = 0
    lambidas.append(maior)

print("std",std)
print("tester:", testr)
#print("lambidas:",lambidas)
print("populacao: ", populacao)

# variavel que ira guardar todos os individuos agrupados
popi = []

caminhos = []
caminhosauxi = []
aux3 = 0
saltosauxi = []
saltos = []
soma_s = 0
for i in range(len(std)):

    caminhosauxi.append(std[i])
    saltosauxi.append(len(std[i]))
    aux3 = aux3 + 1

    if (aux3 == 4):
        caminhos.append(caminhosauxi)
        caminhosauxi = []
        for x in range(len(saltosauxi)):
            soma_s = saltosauxi[x] + soma_s
        saltos.append(soma_s)
        aux3 = 0
        soma_s = 0
        saltosauxi = []

#print("saltos", saltos)

# requisicoes, caminhos, id , cromossomo , fog , lambida
for i in range(len(populacao)):
    popi.append(Individuo(pop1, caminhos[i], i, populacao[i], mediar[i], lambidas[i], saltos[i]))

# teste de individuos geral
'''''
for x in range(len(popi)):
    print("Individuo "+str(x)+":")
    print("requisicoes:",popi[x].requisicoes)
    print("caminhos: ", popi[x].caminhos)
    print("id", popi[x].id)
    print("cromossomo:",popi[x].cromossomo )
    print("fog", popi[x].fog)
    print("lambida", popi[x].lambida)
'''''
# variavel que ira guardar os individuos com fog 1
popr = []
for i in range(len(popi)):
    if (popi[i].fog == 1):
        popr.append(popi[i])

# testando os individuos com fog 1
'''''
for x in range(len(popr)):
    print("Individuo " + str(x) + ":")
    print("requisicoes:", popr[x].requisicoes)
    print("caminhos: ", popr[x].caminhos)
    print("id :", popr[x].id)
    print("cromossomo:", popr[x].cromossomo)
    print("fog :", popr[x].fog)
    print("lambida :", popr[x].lambida)
    print("numero de saltos :", popr[x].n_saltos)
'''''
sum_rota_max=len(pathb[0][3])+len(pathb[1][3])+len(pathb[2][3])+len(pathb[3][3])
#print("rota maxima",sum_rota_max)
sum_rota_min=len(pathb[0][0])+len(pathb[1][0])+len(pathb[2][0])+len(pathb[3][0])
#print("rota minima",sum_rota_min)
#print(pathb)

popw1=[]
popw2=[]
popw3=[]
popw4=[]

for x in range(len(popr)):
   if(popr[x].lambida==1):
       popw1.append(popr[x])
   elif(popr[x].lambida==2):
       popw2.append(popr[x])
   elif(popr[x].lambida==3):
       popw3.append(popr[x])
   elif(popr[x].lambida==4):
       popw4.append(popr[x])

pop_w_r=popw1+popw2+popw3+popw4

#teste rankeamento por onda
''''
for x in range(len(pop_w_r)):
    print("lista rankeadas por lambidas 1:")
    print("Id: ",pop_w_r[x].id)
    print("Fog: ",pop_w_r[x].fog)
    print("lambida",pop_w_r[x].lambida)
    print("cromossomo: ",pop_w_r[x].cromossomo)
    print("caminho: ",pop_w_r[x].caminhos)
    print("numero saltos: ",pop_w_r[x].n_saltos)
'''''


def roullet(pop):
    pesos = []
    for x in range(len(pop)):
        if (pop[x].lambida == 1):
            pesos.append(40)
        if (pop[x].lambida == 2):
            pesos.append(20)
        if (pop[x].lambida == 3):
            pesos.append(10)
        if (pop[x].lambida == 4):
            pesos.append(5)

    soma_pesos = 0

    for x in range(len(pesos)):
        soma_pesos = soma_pesos + pesos[x]

    porc = []

    for x in range(len(pesos)):
        porc.append((pesos[x] * 100) / soma_pesos)

    soma_regua = -1
    regua = []
    addp = soma_pesos

    while (addp > 0):
        soma_regua = soma_regua + 1
        addp = addp - pesos[soma_regua]
        regua.append(addp)

    escolha1 = random.randrange(soma_pesos)
    escolha2 = random.randrange(soma_pesos)

    #print("escolha 1", escolha1)
    #print("escolha 2", escolha2)
    posicao = -1
    posicao2 = -1
    while (escolha1 > 0):
        posicao = posicao + 1
        escolha1 = escolha1 - pesos[posicao]
    while (escolha2 > 0):
        posicao2 = posicao2 + 1
        escolha2 = escolha2 - pesos[posicao2]

    return pop[posicao].lambida, pop[posicao2].lambida


best_w1,best_w2=roullet(pop_w_r)


def choose_Parents(w1,w2):

    t_par1 = []
    t_par2 = []
    c_dad=False
    c_mon=False

    for x in range(len(pop_w_r)):
        if (pop_w_r[x].lambida == w1):
            t_par1.append(pop_w_r[x])
        if (pop_w_r[x].lambida == w2):
            t_par2.append(pop_w_r[x])

    melhorpai = t_par1[0]
    t_par1.pop(0)
    c_dad=True

    melhormae = t_par2[0]
    t_par2.pop(0)
    c_mon=True
    if(len(t_par1)==0):
        c_dad=True
    else:
        if(len(t_par1)==1):
            if(melhorpai.n_saltos>t_par1[0].n_saltos):
                melhorpai=t_par1[0]
                c_dad=True
            else:
                melhorpai=melhorpai
                c_dad=True
        else:
            for x in range(len(t_par1)):
                if(melhorpai.n_saltos>t_par1[x].n_saltos):
                    melhorpai=t_par1[x]
                    c_dad=True
                else:
                    melhorpai=melhorpai
                    c_dad=True

    if (len(t_par2) == 0):
        c_mon = True
    else:
        if (len(t_par2) == 1):
            if (melhormae.n_saltos > t_par2[0].n_saltos):
                melhormae = t_par2[0]
                c_mon = True
            else:
                melhormae = melhormae
                c_mon = True
        else:
            for x in range(len(t_par2)):
                if (melhormae.n_saltos > t_par2[x].n_saltos):
                    melhormae = t_par2[x]
                    c_mon = True
                else:
                    melhormae = melhormae
                    c_mon = True

    if(c_dad==True and c_mon==True):
        return melhorpai, melhormae

def choose_Parests2(w):
    t_par=[]
    c_dad=False
    c_mon=False

    for x in range(len(pop_w_r)):
        if(pop_w_r[x].lambida==w):
            t_par.append(pop_w_r[x])

    melhorpai = t_par[0]
    c_dad=True

    if (len(t_par) == 0):
        c_dad = True
    else:
        if (len(t_par) == 1):
            if (melhorpai.n_saltos > t_par[0].n_saltos):
                melhorpai = t_par[0]
                c_dad = True
            else:
                melhorpai = melhorpai
                c_dad = True
        else:
            for x in range(len(t_par)):
                if (melhorpai.n_saltos > t_par[x].n_saltos):
                    melhorpai = t_par[x]
                    c_dad = True
                else:
                    melhorpai = melhorpai
                    c_dad = True

    for x in range(len(pop_w_r)):
        if(melhorpai==pop_w_r[x]):
            pop_w_r.pop(x)
            break

    for x in range(len(t_par)):
        if(melhorpai==t_par[x]):
            t_par.pop(x)
            break

    if(len(t_par)==0):
        h_w=False
        while(h_w==False):
            new_wave1,new_wave2=roullet(pop_w_r)

            for x in range(len(pop_w_r)):
                if(new_wave1==pop_w_r[x].lambida):
                    h_w=True
                    t_par.append(pop_w_r[x])


        #for x in range(len(pop_w_r)):
        #    if(new_wave1==pop_w_r[x].lambida):
        #        t_par.append(pop_w_r[x])

        if(len(t_par)==0):
            for x in range(len(pop_w_r)):
                if (new_wave2 == pop_w_r[x]):
                    t_par.append(pop_w_r[x])
        if(len(t_par)==0):
            new_wave1 , new_wave2 = roullet(pop_w_r)
            for x in range(len(pop_w_r)):
                if (new_wave1==pop_w_r[x].lambida):
                    t_par.append(pop_w_r[x])


        melhormae = t_par[0]
        c_mon=True
        if (len(t_par) == 0):
            c_mon = True
        else:
            if (len(t_par) == 1):
                if (melhormae.n_saltos > t_par[0].n_saltos):
                    melhormae = t_par[0]
                    c_mon = True
                else:
                    melhormae = melhormae
                    c_mon = True
            else:
                for x in range(len(t_par)):
                    if (melhormae.n_saltos > t_par[x].n_saltos):
                        melhormae = t_par[x]
                        c_mon = True
                    else:
                        melhormae = melhormae
                        c_mon = True
    elif(len(t_par)==1):
        melhormae=t_par[0]
        c_mon=True

    if(c_mon==True):
     c_mon=True

    else:
        melhormae=t_par[0]
        c_mon = True
        if (len(t_par) == 0):
            c_mon = True
        else:
            if (len(t_par) == 1):
                if (melhormae.n_saltos > t_par[0].n_saltos):
                    melhormae = t_par[0]
                    c_mon = True
                else:
                    melhormae = melhormae
                    c_mon = True
            else:
                for x in range(len(t_par)):
                    if (melhormae.n_saltos > t_par[x].n_saltos):
                        melhormae = t_par[x]
                        c_mon = True
                    else:
                        melhormae = melhormae
                        c_mon = True

    if(c_dad==True and c_mon==True):
        return melhorpai, melhormae





best_dad=0
best_mon=0
if(best_w1!=best_w2):
    best_dad , best_mon=choose_Parents(best_w1, best_w2)

else:
    best_dad , best_mon=choose_Parests2(best_w1)
#testepais

print("melhor pai:")
print("Id: ",best_dad.id)
print("lambida: ",best_dad.lambida)
print("Saltos: ",best_dad.n_saltos)
print("cromossomo:",best_dad.cromossomo)
print("caminhos:",best_dad.caminhos)
print("\nmelhor mae:")
print("Id: ",best_mon.id)
print("lambida: ",best_mon.lambida)
print("Saltos: ",best_mon.n_saltos)
print("cromossomo:",best_mon.cromossomo)
print("caminhos:",best_mon.caminhos)


