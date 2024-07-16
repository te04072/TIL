이 문서는 nested list를 deep copy하면서 찾은 방법들을 정리하였다.

## 1. 모듈 사용
>import copy  
>backup_catalog = copy.deepcopy(catalog)  


## 2. for문 사용
>backup_catalog = [item[:] for item in catalog]  


## 3. map 함수 사용
>nestedList = list(map(list,List))  
