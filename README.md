# BA_01_차원축소

<p align="center"><img src="https://user-images.githubusercontent.com/97882448/195100669-4eea03a4-42e9-47d1-815a-7786f3285caa.png" width="50%" height="50%"/>

## BA_01 차원축소 유전 알고리즘(Genetic Algorithm)

고려대학교 비니지스 애널리틱스에서 배운 유전 알고리즘을 구현하려고합니다.
그리고 앞으로 설명할때 GA라고 명명하도록하겠습니다.
먼저, GA의 기본적인 개념에대해서 설명하고 예시 파일을 통해 이해를 돕도록하겠습니다.

<p align="center"><img width="581" alt="image" src="https://user-images.githubusercontent.com/97882448/195105010-107d4b9d-a041-47f1-9dbf-d55f91550fe0.png">

일단 GA는 local search인 Foward Selection, Backward Elimination, Stepwise Selection보다 소요시간이 좀더 걸리고 성능이 좀더 좋아지는 Heuristic method입니다. 
<p align="center"><img width="759" alt="image" src="https://user-images.githubusercontent.com/97882448/195103063-5d058ba7-3fa7-4086-9573-68f55f5c0e7d.png">

일단 GA는 heuristic이기에 최적해는 아니고 최적해에 가까운 해입니다. 최적화 알고리즘 중에 자연적인 현상을 모티브로한 여러가지 알고리즘이 있는데요. 그 중 하나는 위에 그림을 참고하시면 인공신경망, 호르몬으로 최단거리를 찾아가는 개미군집방법 ,철새들이 최장거리를 가기위해서 에너지를 최소한 시키는 방법을 모티브로 한 PSD가 있습니다.

그리고 이번시간에 설명하려는 GA가 있습니다. 

<p align="center"><img width="433" alt="image" src="https://user-images.githubusercontent.com/97882448/195108105-d6457fc3-3252-484d-80c5-b14008335caa.png">

GA의 전반적인 시스템을 설명하겠습니다. 중요한 용어가 selection, crossover, mutation이 있습니다. selection은 Fitness function을 통해 solution의 quality을 높이는 일을 하고요 cross over는 다양한 gene를 섞어주기 위함이며 mutation은 local optimm이 아니라 global optimum을 찾기 위함입니다.

<p align="center"><img width="500" alt="image" src="https://user-images.githubusercontent.com/97882448/195110535-1e29e02a-2b72-43dc-8224-c98772f76f41.png">

계속해서 강조하지만 GA는 세대가 지남에 따라 최선해를 찾는 heuristic method이고 전체적인 프레임워크는 위 그림과 같이 염색체 초기화 및 파라미터를 설정 후 모델을 학습하고 피트니스 펑션을 통해 평가를 진행하고 성능이 높은 염색체를 선별합니다. 그리고 성능이 좋은 애들끼리 크로스오버와 뮤테이션을 통해 새로운 염색체가 정의되고 이 순환 사이클을 generation이라고 합니다.

이렇게 계속 진행이 되면 결국 마지막세대에서 최종 변수 집합이 선택됩니다.
