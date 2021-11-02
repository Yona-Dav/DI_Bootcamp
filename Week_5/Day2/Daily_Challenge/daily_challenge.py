import random


class DNA:
    def __init__(self):
        self.dna_list =[]
        for i in range(10):
            self.dna_list.append(Chromosome().chromosome_list)
        print(self.dna_list)

    def mutate(self):
        selected_chromosomes = random.sample(self.dna_list, random.randint(0, len(self.dna_list)))
        for chromo in selected_chromosomes:
            if random.randint(0,1):
                chromo.mutate()  
                print('i mutated', chromo)
            else:
                print('i didnt mutated')

    

class Chromosome(DNA):
    def __init__(self):
        self.chromosome_list = []
        for i in range(10):
            self.chromosome_list.append(Gene().value)
        #print(self.chromosome_list)
        
    def mutate(self):
        # selected_genes = random.sample(self.chromosome_list, random.randint(0,len(self.chromosome_list)))
        # for gene in selected_genes:
        #     if random.randint(0,1):
        #         gene.flip()
        indexs = list(range(0,len(self.chromosome_list)))
        random.shuffle(indexs)
        for idx in indexs[0:random.choice(indexs)]:
            if random.randint(0,1):
                self.chromosome_list[idx].flip()


class Gene(Chromosome):
    def __init__(self):
        self.value = random.choice([0,1])
    
    def flip(self):
        self.value = 1 if self.value==0 else 0
        print(self.value)

class Organism(DNA):
    def __init__(self, dna, environment=50):
        # super().__init__()
        # self.env = environment
        # self.number_generation = 0
        self.dna = dna
        self.probability = environment

    def mutate(self):   
        # for chromosome in self.dna_list:
        #     count = 0
        #     while count < random.randint(0,len(chromosome)-1):
        #         i = random.randint(0,len(chromosome)-1)
        #         chromosome[i]= 1 if chromosome==0 else 0
        #         count+=1
        # print(self.dna_list)
        if self.probability <random.randint(0,100): 
            self.dna.mutate()

    def only_one(self):
        self.mutate()
        self.number_generation +=1
        for chromosome in self.dna:
            if chromosome != [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                return self.only_one()
        print(self.number_generation)
        print(self.dna)



# chromosome1 = Chromosome()
# dna1 = DNA()
organism1 = Organism()
#organism1.mutate()
organism1.only_one()