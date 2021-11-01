import random


class DNA:
    def __init__(self):
        self.dna_list =[]
        for i in range(10):
            self.dna_list.append(Chromosome().chromosome_list)
        print(self.dna_list)

class Chromosome(DNA):
    def __init__(self):
        self.chromosome_list = []
        for i in range(10):
            self.chromosome_list.append(Gene().value)
        #print(self.chromosome_list)

class Gene(Chromosome):
    def __init__(self):
        self.value = random.choice([0,1])
    
    def mutate(self):
        self.value = 1 if self.value==0 else 0
        print(self.value)

class Organism(DNA):
    def __init__(self, environment):
        super().__init__()
        self.env = environment
        self.number_generation = 0

    def mutate(self):   
        for chromosome in self.dna_list:
            count = 0
            while count < random.randint(0,len(chromosome)-1):
                i = random.randint(0,len(chromosome)-1)
                chromosome[i]= 1 if chromosome==0 else 0
                count+=1
        print(self.dna_list)
    
    def only_one(self):
        self.mutate()
        self.number_generation +=1
        for chromosome in self.dna_list:
            if chromosome != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                return self.only_one()
        print(self.number_generation)
        print(self.dna_list)



# chromosome1 = Chromosome()
# dna1 = DNA()
organism1 = Organism('land')
#organism1.mutate()
organism1.only_one()