import numpy as np
import datetime

#아스키 코드를 통해 새로운 염색체를 만드는 과정
def create_gen(num_target):
    random_number = np.random.randint(32, 126, size=num_target)
    #['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
    gen = ''.join([chr(i) for i in random_number])
    #print(gen)
    return gen

#염색체의 적합도를 계산함
def calculate_fitness(gen, target, num_target):
    fitness = 0
    for i in range (num_target):
        if gen[i:i+1] == target[i:i+1]:
            fitness += 1
    fitness = fitness / num_target * 100
    return fitness

#인구수 생성을 통해  dictionary에 넣어서 유전자만들고 적합도를 계산하는 과정
def create_population(target, max_population, num_target):
    population_set = {}
    for i in range(max_population):
        gen = create_gen(num_target)
        genfitness = calculate_fitness(gen, target, num_target)
        population_set[gen] = genfitness
        #print(population_set)
        #print(population_set)
    return population_set

# selection process
def selection(population_set):
    pop = dict(population_set)
    #print(pop)
    parent = {}
    for i in range(2):
        #pop에서 max값을 가진 value를 뱉어줌
        gen = max(pop, key=pop.get)
        #print(gen)
        genfitness = pop[gen]
        #print(genfitness)
        parent[gen] = genfitness
        #2개를 넣어야하니깐 처음꺼는 if를 통해 지워줌
        if i == 0:
            del pop[gen]
    return parent

# 교차함수
def crossover(parent, target, num_target):
    child = {}
    #dic을 list로 바꾸어서 1crossover를 할수 있도록 만들어줌->cp
    cp = round(len(list(parent)[0])/2)
    #print(list(parent))
    for i in range(2):
        gen = list(parent)[i][:cp] + list(parent)[1-i][cp:]
        #print(gen)
        genfitness = calculate_fitness(gen, target, num_target)
        child[gen] = genfitness
        #print(len(child))
    return child

# 돌연변이 함수정의
def mutation(child, target, mutation_rate, num_target):
    mutant = {}
    for i in range(len(child)):
        data = list(list(child)[i])
        #print(data)
        #print(len(data))
        for j in range(len(data)):
            #랜덤이 0에서 1사이 나오는 점수에서 넘나 안넘나를 보면 됨
            #print(j)
            if np.random.rand(1) <= mutation_rate:
                ch = chr(np.random.randint(32, 126))
                #print(ch)
                data[j] = ch
                #print(data)
        gen = ''.join(data)
        genfitness = calculate_fitness(gen, target, num_target)
        mutant[gen] = genfitness
    return mutant

#최고의 염색체와 함께 새로운 generation을 만듬
def regeneration(mutant, population_set):
    #print(len(population_set))
    #print(len(mutant))
    for i in range(len(mutant)):
        bad_gen = min(population_set, key=population_set.get)
        del population_set[bad_gen]
    population_set.update(mutant)
    #print(type(population_set))
    return population_set

# 최고의 염색체를 추출하는 함수
def bestgen(parent):
    gen = max(parent, key=parent.get)
    return gen

# 최고의 염색체에서 좋은성능을 가진 fitness값을 추출하는 함수
def bestfitness(parent):
    fitness = parent[max(parent, key=parent.get)]
    return fitness

# 위에서 정의한 2개의 함수를 시간과 같이 추출함
def display(parent):
    timeDiff=datetime.datetime.now()-startTime
    print('\t{}\t{}%\t{}'.format(bestgen(parent), round(bestfitness(parent), 2), timeDiff))

# 하이퍼파라미터처럼 무엇을 맞출것인지? 염색체 생성갯수, mutation(돌연변이)율도 설정가능함
target = 'KOREA UNIVERSITY!'
max_population = 1000
mutation_rate = 0.1

print('\tTarget Word :', target)
print('\tMax Population :', max_population)
print('\tMutation Rate :', mutation_rate)

#target의 길이
num_target = len(target)
startTime=datetime.datetime.now()
print('################################################')
print('\t{}\t\t\t{}\t\t{}'.format('The Best','Fitness','Time'))
print('################################################')
population_set = create_population(target, int(max_population), num_target)
parent = selection(population_set)
display(parent)

#while 1 : 항상실행하라는 뜻임
while 1:
    child = crossover(parent, target, num_target)
    mutant = mutation(child, target, float(mutation_rate), num_target)
    if bestfitness(parent) >= bestfitness(mutant):
        continue
    population_set = regeneration(mutant, population_set)
    parent = selection(population_set)
    display(parent)
    if bestfitness(mutant) == 100:
        break