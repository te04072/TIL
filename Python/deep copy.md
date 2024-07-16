이 문서는 nested list를 deep copy하면서 찾은 방법들을 정리하였다.

## 1. 모듈 사용
>import copy  
>nestedList = copy.deepcopy(List)  


## 2. for문 사용
>nestedList = [item[:] for item in List]  


## 3. map 함수 사용
>nestedList = list(map(list,List))  
