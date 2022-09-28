import random

# Tamanho da população em cada geração

populationSize = 100

# Todos os genes possíveis em um indivíduo

genes = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

target = "testando o algoritmo"

'''
classe que representa um indivíduo, que vai possuir
cromossomo e uma taxa de aptidão
'''

class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.fitnessFunction()

        # criando genes aleatórios com mutação

    @classmethod
    def mutatedGenes(self):
        global genes
        gene = random.choice(genes)
        return gene

        # criando um cromossomo (cadeia de genes)

    @classmethod
    def createChromosome(self):
        global target
        chromosomeLength = len(target)
        return [self.mutatedGenes() for _ in range(chromosomeLength)]

    # Realizando cruzamentos e criando novos indivíduos para a geração seguinte
    
    def match(self, pair):
        child = []

        # Separando grupos de indivíduos escolhidos

        for firstGroup, secondGroup in zip(self.chromosome, pair.chromosome):
            probability = random.random()
            
            '''
            Se a cálculo de aptidão obtiver menos de 0.45 de precisão, o indivíduo
            é inserido no primeiro grupo
            '''

            if probability < 0.45:
                child.append(firstGroup)

            # Caso contrário, é inserido no segundo grupo

            elif probability < 0.90:
                child.append(secondGroup)

            # Aplicação da mutação para manter a diversidade

            else:
                child.append(self.mutatedGenes())

        # Criando novo indivíduo

        return Individual(child)

    '''
    Calculando a taxa de aptidão, que é o quão determinado
    indivíduo de aproxima da solução
    '''

    def fitnessFunction(self):
        global target
        fitness = 0

        for firstGene, secondGene in zip(self.chromosome, target):
            if firstGene != secondGene: fitness += 1
        return fitness

def main():
    global populationSize

    # geração atual

    generation = 1

    found = False
    population = []

    # Criando a população incial

    for _ in range(populationSize):
        chromosome = Individual.createChromosome()
        population.append(Individual(chromosome))

    while not found:

        # Ordenando a população de acordo com a taxa de aptidão

        population = sorted(population, key = lambda x:x.fitness)

        '''
          Se o indivíduo possuir uma taxa de aptidão igual a 0,
          Significa que a solução foi encontrada, então o
          programa termina
        '''

        if population[0].fitness <= 0:
            found = True
            break

        # Caso contrário, é gerada uma nova geração

        newGeneration = []

        '''
        A seleção natural, onde 10% dos melhores classificados
        vão para a próxima geração
        '''

        naturalSelection = int((10*populationSize)/100)
        newGeneration.extend(population[:naturalSelection])

        
        # 50% dos melhores classificados irão fazer parte do cruzamento

        naturalSelection = int((90*populationSize)/100)

        for _ in range(naturalSelection):
            firstParent = random.choice(population[:50])
            secondParent = random.choice(population[:50])
            child = firstParent.match(secondParent)
            newGeneration.append(child)

        population = newGeneration

        print("Geração: {}\tSolução: {}\tAptidão: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))

        generation += 1

    print("Geração: {}\tSolução: {}\tAptidão: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))

if __name__ == '__main__':
    main()