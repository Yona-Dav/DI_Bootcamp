import random

#Exercise 1 : Double Dice
def throw_dice():
    return random.randint(1,6)


def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            break
    return count

print(f'It took {throw_until_doubles()} tries to get doubles')

def results_avg(res_list):
    return sum(res_list)/len(res_list)

def main():
    results = []
    for num in range(0,100):
        results.append(throw_until_doubles())
    print(f'It took {sum(results)} tries to get 100 doubles')
    print(f'on average it took {results_avg(results)} throws to get a double')

main()

