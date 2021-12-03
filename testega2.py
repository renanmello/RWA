import random
import networkx
import matplotlib

class AlgoritmoGenetico2:

    def __init__(self, req=[1,2,3,4,5], tamPopulacao=5, limGeracoes=50, probMutacao=5, funcaoFitness=None, maiorFitness=True):
        # Atributos
        self.req = req
        self.tamPopulacao = tamPopulacao
        self.limGeracoes = limGeracoes
        self.funcaoFitness = funcaoFitness
        self.maiorFitness = maiorFitness
        self.probMutacao = probMutacao
        self.populacao = []
        self.geracao = 1

        # Funções que podem ser alteradas
        self.funMutacao = self.mutacao
        self.funSelecao = self.selecao
        self.funCrossover = self.crossover
        self.funCriaIndividuo = self.criaIndividuo


    def criaPopulacaoInicial(self):
        """ Cria a primeira população """

        for i in range(self.tamPopulacao):
            individual = []  # C = [ idx, idx, idx, ..., idx, fit ]
            for j in range(len(self.Req)):
                individual.append(random.randrange(5))
            # individual.append(random.randrange(info.K_MIN))
            self.population.append(individual + [0])

        return self.population
p=AlgoritmoGenetico2.criaPopulacaoInicial()
print(p)
