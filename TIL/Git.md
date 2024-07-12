# How to use git

## git log --oneline
로그를 한 줄로 간편하게 볼 때 사용

## git push origin master
local master branch를 github의 master branch로 push
이 때 origin은 별칭으로 원하는대로 명명 가능

## git push -u origin master
-u는 --set-upstream으로 이후로는 git push만 입력해도 해당 master branch로 push 가능
## git pull origin master
github에서 pull

## git clone <url>

## git remote add origin <url>
>git remote add origin <url>  
>git branch -M master  
>git push -u origin master

github remote repository에 작업 소스 추가

## git remote set-url origin --push --add <url>
이와 같이 설정하면 origin이라는 이름 하에 여러 repository에 동시에 push 가능

## gitignore
*touch .gitignore*로 파일 생성
여기에 추가한 파일이나 디렉토리는 commit 대상이 되지 않는다.
gitignore.io에서 손쉽게 생성 가능
단 한번이라도 **git 관리대상이 된 적이 있다면 적용되지 않으니 gitignore은 작업 전에 미리 생성**해야 한다.

### 여담
>error: src refspec master does not match any  
error: failed to push some refs to 'https://github.com/te04072/TIL.git'

commit을 깜박하고 업로드를 시도하니 위와 같은 에러가 발생한다. 잘하자
