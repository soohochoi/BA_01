# BA_01_차원축소

<p align="center"><img src="https://user-images.githubusercontent.com/97882448/195100669-4eea03a4-42e9-47d1-815a-7786f3285caa.png" width="50%" height="50%"/>

## BA_01 차원축소 유전 알고리즘(Genetic Algorithm)_개념설명

먼저 이자료는 고려대학교 비니지스 애널리틱스 강필성교수님께 배운 유전 알고리즘을 바탕으로 만들어졌습니다.

먼저, GA의 기본적인 개념에대해서 설명하고 예시 파일을 통해 이해를 돕도록하겠습니다.
그리고 앞으로 설명할때 통일성을 위해 유전 알고리즘을 GA라고 명명하도록하겠습니다.

<p align="center"><img width="581" alt="image" src="https://user-images.githubusercontent.com/97882448/195105010-107d4b9d-a041-47f1-9dbf-d55f91550fe0.png">

일단 GA는 local search인 Foward Selection, Backward Elimination, Stepwise Selection보다 소요시간이 좀더 걸리고 성능이 좀더 좋아지는 Heuristic method입니다. 
<p align="center"><img width="759" alt="image" src="https://user-images.githubusercontent.com/97882448/195103063-5d058ba7-3fa7-4086-9573-68f55f5c0e7d.png">

일단 GA는 heuristic이기에 최적해는 아니고 최적해에 가까운 해입니다. 최적화 알고리즘 중에 자연적인 현상을 모티브로한 여러가지 알고리즘이 있는데요. 그 중 하나는 위에 그림을 참고하시면 인공신경망, 호르몬으로 최단거리를 찾아가는 개미군집방법 ,철새들이 최장거리를 가기위해서 에너지를 최소한 시키는 방법을 모티브로 한 PSD가 있습니다.

그리고 이번시간에 설명하려는 GA가 있습니다. 

<p align="center"><img width="433" alt="image" src="https://user-images.githubusercontent.com/97882448/195108105-d6457fc3-3252-484d-80c5-b14008335caa.png">

GA의 전반적인 시스템을 설명하겠습니다. 중요한 용어가 selection, crossover, mutation이 있습니다. selection은 Fitness function을 통해 solution의 quality을 높이는 일을 하고요 cross over는 다양한 염색체를 섞어주기 위함이며 mutation은 local optimm이 아니라 global optimum을 찾기 위함입니다.

<p align="center"><img width="500" alt="image" src="https://user-images.githubusercontent.com/97882448/195110535-1e29e02a-2b72-43dc-8224-c98772f76f41.png">

계속해서 강조하지만 GA는 세대가 지남에 따라 최선해를 찾는 heuristic method이고 전체적인 프레임워크는 위 그림과 같이 염색체 초기화 및 파라미터를 설정 후 모델을 학습하고 fitness function을 통해 평가를 진행하는것을 세대에 걸쳐 진행해서 성능이 높은 염색체를 선별합니다. 그리고 성능이 좋은 유전자들끼리 crossover와 mutation을 통해 새로운 염색체가 정의되고 이 순환 사이클을 generation이라고 합니다. 이렇게 계속 진행이 되면 결국 마지막세대에서 최종 변수 집합이 선택됩니다.

<p align="center"><img width="810" alt="image" src="https://user-images.githubusercontent.com/97882448/195241575-9826054c-b43c-4644-9243-4943305452fd.png">

좀더 자세히 순서별로 알아보도록 하겠습니다. 첫번째는 Iinitializng입니다. 

#### Step.01 Iinitializng을 통해 초기 염색체의 개수 그리고 fitness function, 교배 방식, 돌연변이율 종료조건을 설정함

* 종료조건은 보통 향상이 더이상 되지 않거나 반복을 최대로 했을 때 둘 중 하나가 만족하면 종료함 
<p align="center"><img width="808" alt="image" src="https://user-images.githubusercontent.com/97882448/195242232-c64100c2-6dc6-4a40-ac53-97c11423f201.png">

* 벡터들을 일단 chrobosome(염색체)라고 부르고 그 안에있는 유전자를 gene이라고 부릅니다. 위에 그림은 차원축소의 예시로 변수를 사용하면 1 아니면 0이라고 설정함

<p align="center"><img width="810" alt="image" src="https://user-images.githubusercontent.com/97882448/195243740-8dc33a23-ed34-421a-8aa8-59fc5e2d9016.png">

#### Step.02,03 파라미터 설정이 완료되었으면 선택된 변수별로 모델을 훈련시키고 훈련된 변수 모델들이 얼마나 모델을 잘 표현하는지에 대한 적합도를 평가함

* 염색체의 수만큼 모델을 만들고 fitness function을 통해 모델을 평가하는 과정임
  
 <p align="center"> <img width="810" alt="image" src="https://user-images.githubusercontent.com/97882448/195245282-312b2035-82bf-4f8b-ba6d-090adbee6d29.png">

#### Step.04 Selection을 통해 우수한 염색체를 선택하며 선택방식은 2가지가 있음
   
* Deterministic selection: 살릴 염색체와 버릴 염색체를 구분 지어 살릴 염색체만 채택하고 나머지는 버림
    * EX) 100개의 염색체중 30%만 살릴 염색체면 70%인 70개는 버림
* Probabilistic selection: 적합도 평가를 기준으로 모든 염색체에게 기회를 줌 대신 1등부터 꼴등까지 가중치(selection weight)를 정의 후 확률적으로 염색체를 선택하도록 함
    * EX) 100개의 염색체를 적합도 평가가 우수한기준으로 순서를 매긴후 1등에게 가장 많은 가중치를 꼴등에겐 가장 적은 가중치를 주어 selection함
   
 <p align="center"><img width="810" alt="image" src="https://user-images.githubusercontent.com/97882448/195246971-9d6c5705-891d-4da3-97f2-02cc7f9e0397.png">
   
#### Step.05 다음세대에 더 좋은 염색체를 crossover하고 mutation을 진행시키는 과정임
   
 <p align="center"><img width="461" alt="image" src="https://user-images.githubusercontent.com/97882448/195247717-9d894e6c-cfe7-4d21-a6a5-6e418863cdb1.png">

* 남녀의 염색체를 통해 남아 여아가 생성되는 것에 착안하여 다음세대 염색체를 생성함 1 cross over이면 위 그림처럼 한포인트를 바꿔 주고 2cross over이면 2개의 포인트를 바꿔 줌
   
<p align="center"><img width="459" alt="image" src="https://user-images.githubusercontent.com/97882448/195247835-01937ec1-1e61-47c3-bfff-e78ca79aab09.png">

* mutation의 목적은 돌연변이를 통해 local optimal -> Global optimal로 바꿔 줌

<p align="center"><img width="810" alt="image" src="https://user-images.githubusercontent.com/97882448/195248105-c73b1ebd-2697-4d8d-8bac-da5d280050fd.png">

#### Step.06 최선해가 나올 때 Step.02부터 Step.05까지를 반복함

<p align="center"><img width="495" alt="image" src="https://user-images.githubusercontent.com/97882448/195249507-1995a512-004d-4aa6-a227-ede63ed0e714.png">

* 위 그림처럼 GA의 성능은 초반에  fitness value가 급격하게 감소하다 완만해짐 
* 안전장치로서, 이전 세대의 best 염색체들을 다음 세대에 그대로 가져와서 성능이 감소되지 않도록 이용하기도 함 
* 학습 종료 조건은 다음과 같음
  * 더이상 성능 향상이 일어나지 않을 때
  * 초기에 설정해 둔 반복 횟수에 도달되었을 때

---
  
## BA_01 차원축소 유전 알고리즘(Genetic Algorithm)_코드설명
  
```python
#만약에 numpy와 datatime이 없다면 install 해주도록한다  
import numpy as np
import datetime  
```
유전 알고리즘을 실행할때 필요한 package들이다.

```python
  # 아스키코드를 통해 새로운 염색체를 만드는 과정임
def create_gen(num_target):
    random_number = np.random.randint(32, 126, size=num_target)
    #['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
    gen = ''.join([chr(i) for i in random_number])
    print(gen)
    return gen
``` 
#### 아스키 코드란?
  
<p align="center"><img width="792" alt="image" src="https://user-images.githubusercontent.com/97882448/195253671-ffa0bb1c-6251-4bf7-8053-9cea2554a68a.png">

* 숫자를 문자로 표현하는 방식임
  * chr(숫자)-> 숫자에 맞는 아스키 코드를 반환함 
  * 반대로 ord(문자)-> 문자에 맞는 숫자를 반환함 

```python
#염색체의 적합도를 계산함
def calculate_fitness(gen, target, num_target):
    fitness = 0
    for i in range (num_target):
        if gen[i:i+1] == target[i:i+1]:
            fitness += 1
    fitness = fitness / num_target * 100
    return fitness
``` 
* fitness 함수를 계산하는 함수를 만들어줌 염색체와 num_target의 위치와 문자가 같을 때 적합도가 올라감
  
```python
#인구수생성을 통해 dictionary에 넣어서 염색체를 만들고 적합도를 계산하는 과정
def create_population(target, max_population, num_target):
    population_set = {}
    for i in range(max_population):
        gen = create_gen(num_target)
        genfitness = calculate_fitness(gen, target, num_target)
        population_set[gen] = genfitness
        #print(population_set)
    return population_set
``` 
* max_population을 통해 최대 인구수를 설정하고 population set이라는 dictionary을 만들었는데 1개씩 한염색체가 fitness가 얼마인지 계산해서 넣는 과정임 
  * EX) i가 2번 돌았을때 {'E,r9..Jfq;$9(HNP\\': 0.0, '7yi/?B&XUx\\5hF6t#': 0.0} 

``` python  
  # 염색체에서 우수한 염색체를 선별하는 함수임
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
``` 
* population_set에서 우수한 염색체가 선별되는 과정임 fitness가 높은 염색체가 생선된 parent dictionary에 저장해줌
  
``` python 
  # 교차를 할수 있도록 만드는 함수임
def crossover(parent, target, num_target):
    child = {}
    #dic을 list로 바꾸어서 가운데로 잘라서 1crossover를 할수 있도록 만들어줌->cp
    cp = round(len(list(parent)[0])/2)
    #print(list(parent))
    for i in range(2):
        gen = list(parent)[i][:cp] + list(parent)[1-i][cp:]
        #print(gen)
        genfitness = calculate_fitness(gen, target, num_target)
        child[gen] = genfitness
        #print(len(child))
    return child
```
  
* cp를 통해 문자의 길이의 반을 나눈다음에 gen을 통해 부모세대에서 성능이 좋았던 염색체를 교차시켜줌 그리고 child dictionary로 저장해주는 과정임

``` python 
# mutation을 일으키는 함수
def mutation(child, target, mutation_rate, num_target):
    mutant = {}
    for i in range(len(child)):
        data = list(list(child)[i])
        #print(len(data))
        for j in range(len(data)):
            #랜덤이 0에서 1사이 나오는 점수에서 넘나 안넘나를 보면 됨
            if np.random.rand(1) <= mutation_rate:
                ch = chr(np.random.randint(32, 126))
                #print(ch)
                data[j] = ch
                #print(data)
        gen = ''.join(data)
        genfitness = calculate_fitness(gen, target, num_target)
        mutant[gen] = genfitness
    return mutant
```                                                
* 돌연변이 함수를 통해 일단 child세대에서 dictionary를 ['K', 'O', 'R', 'E', 'u', ' ', 'U', 'N', 'I', 'V', 'R', 'R', 'S', 'I', 'T', 'Y', '!']이런 식으로 만들어줌                                                
* mutaion rate을 0.1로 설정하였고  각 유전자의 갯수만큼 random(0~1)사이에서 난수를 생성하는데 0.1보다 작은 값이 나오면 ['K', 'O', 'R', 'E', 'u', ' ', 'Z', 'N', 'I', 'V', 'R', 'R', 'S', 'I', 'T', 'Y', '!']가 7번째에서 발생하여 바뀐것을 알수있음 
* 나중에 나오겠지만 답이 KOREA UNIVERSITY! 인데 이같은 경우는 잘찾아가던 답이 바뀐것으로 좋은 mutation은 아니였음

``` python 
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
```
* mutant와 population_set를 통해 성능이 좋지 않은 염색체는 지우고 mutant를 시켰던 염색체를 update시켜줌

``` python 
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
    print('{}\t{}%\t{}'.format(bestgen(parent), round(bestfitness(parent), 2), timeDiff))
```
* 마지막 함수에대해서 추가설명을 하자면 맨앞에서 불러온 datatime을 통해 최고의 parent을 추출하는데 걸린 시간과  fitness값을 가시성 좋게 소수 3번째에서 반올림한것을 알수있음

``` python 
# 하이퍼파라미터처럼 무엇을 맞출것인지? 염색체 생성갯수, mutation(돌연변이)율도 설정가능함 
target = 'KOREA UNIVERSITY!'
max_population = 100
mutation_rate = 0.1
```
* 위 코드보다시피 target은 KOREA UNIVERSITY!로 설정하였고 염색체 생성갯수는 100 돌연변이율은 0.1로 설정하였음

``` python 
print('Target Word :', target)
print('Max Population :', max_population)
print('Mutation Rate :', mutation_rate)

#target의 길이
num_target = len(target)
startTime=datetime.datetime.now()
print('################################################')
print('\t{}\t\t\t{}\t\t{}'.format('The Best','Fitness','Time'))
print('################################################')
population_set = create_population(target, int(max_population), num_target)
parent = selection(population_set)
display(parent)
``` 
* 정의 하였던 함수를 연결시켜주는 과정임 그리고 print 해줌 

``` python
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
```

* crossover를 통해 자식세대의 과정 다음 돌연변이 과정이 진행되는데 그 때 적합도가 100%이면 대상 단어와 추측이 동일하다고 판단이 되어져 과정이 중지됨
  
* 파일을 실행하면 아래와 같은 화면이 나옴
<p align="center"><img width="398" alt="image" src="https://user-images.githubusercontent.com/97882448/195274508-cbc61432-6ce9-4fd0-9578-d7ea1c1add74.png">

---
## BA_01 차원축소 유전 알고리즘(Genetic Algorithm)_성능평가
* Target은 KOREA UNIVERSITY!로 설정후 Mutation을 변경
  * Mutaion rate를 0.1 ,0.2 0.3 로 바꾸어 5번씩 반복실험을 진행함
  * Meantime은 소수점 3번째 자리에서 반올림 하였음
  
 <p align="center"><img width="393" alt="image" src="https://user-images.githubusercontent.com/97882448/195283265-8565a943-ea3a-4e2e-a7b5-d56a3eaee800.png">
   
  1. mutation율이 올라갈수록 Target을 잘 찾지 못함
  2. 초반에 fitness function이 성능이 많이 올라오지만 mutaion율이 올라갈수록 Target값을 찾는데 방해를 하는것을 볼수 있음 

* Target은 KOREA UNIVERSITY!로 설정후 Max population을 변경   
  * population수를 를 10 , 100 , 1000 로 바꾸어 5번씩 반복실험을 진행함
  * Meantime은 소수점 3번째 자리에서 반올림 하였음  
 
 <p align="center"><img width="390" alt="image" src="https://user-images.githubusercontent.com/97882448/195286453-9f46d800-0190-4688-addb-cd22038833c3.png">

   1. 염색채수가 10개는 너무 작은것같고 1000개는 너무 많았던것 같음 100개가 제일 성능이 좋게나옴
   2. Meantime은 소수점 3번째 자리에서 반올림 하였음  
---
 ### Reference
 1. https://sustaining-starflower-aff.notion.site/2022-2-0e068bff3023401fa9fa13e96c0269d7 <강필성교수님 자료>
 2. https://github.com/2black0/ <GA코드 참조>
