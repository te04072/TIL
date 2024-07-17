# Lazy evaluation

map() 함수에 print를 사용한 함수를 넣어 list의 요소들에 적용하여 결과를 출력하게 하려 했으나  
map() 만으로는 출력이 나오지 않는 다는 것을 알았다. 이를 해결하기 위해서는 list()로 map()을 감싸야 했다.

## iterator 객체
이는 map() 함수가 반환하는 값이 iterator이기 때문인데, iterator은 메모리 효율성을 위해  
**lazy evaluation**을 수행하기 때문에 한 번에 하나의 값만 생성하며 필요한 시점에 연산을 수행한다.  
다시말해 실제 iteration이 이뤄지기 전까지는 입력된 함수를 호출하지 않고 map() 객체를 생성할 뿐이다.  
이 때 list()를 사용하면 iterator의 모든 항목을 순회하며 연산을 수행하여 map() 함수값을 리스트로 변환하게 되는데,
tuple()이나 set()을 사용해도 같은 효과를 취할 수 있다.  

## itertools 모듈
count() : 무한한 iterator 생성  
cycle() : 반복 가능한 객체 무한히 반복  
islice() : 반복 가능한 객체 일부를 slice

## generator
generator은 함수 안에서  yield 키워드로 값을 하나씩 반환한다. 이는 호출될 때마다 이전 상태를 기억하고 다음 값을 생성한다.

## generator expression
list comprehension과 유사한 방식으로 소괄호를 사용하여 generator을 생성하는데, 이는 값을 한번에 하나씩 생성한다.

## functools 모듈의 lru_cache
반복된 함수호출의 결과를 캐시, 동일한 입력에 대해 계산을 새로 수행하는 대신 저장된 값을 반환
