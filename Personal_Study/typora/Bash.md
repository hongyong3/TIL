# Bash

### alias 설정하기

```
vi ~/.bash_profile
vi ~/.zshrc

i

alias jp="jupyter notebook"    
 
esc + :wq

source ~/.bash_profile
source ~/.zshrc
```

-> jp하면 쥬피터 열림

### 단축키

`ctrl` + `l` : 화면 클리어

`ctrl` + `c` : 나가기

`ctrl` + `a` : 입력중인 줄 맨 앞으로 이동 ( Flask -> `Home`)

`ctrl` + `e` : 입력중인 줄 맨 뒤로 이동 ( Flask -> `End` )

`ctrl` + `u` : 입력중인 줄 전체 지우기

`ctrl` + `w` : 현재 커서 기준으로 단어로 지우기 ( C9에서는 X )

`ctrl` + `d` : 커맨드 종료

`alt` + `클릭` : 원하는 위치로 커서 이동

### man

매뉴얼 페이지 보기 (Git Bash 불가)

```
sshyeri:~/workspace $ man
What manual page do you want?
sshyeri:~/workspace $ man echo
sshyeri:~/workspace $ man sleep
```

### file, echo, diff

**adele.txt만들어서 그 안에 문자열 넣기( > ), 그 뒤에 붙여 써넣기( >> )**

```
sshyeri:~/workspace $ echo "Someone Like You" > adele.txt
sshyeri:~/workspace $ echo "Rolling In the Deep" >> adele.txt

#둘의 차이 출력
shyeri:~/workspace $ echo "Someone Like You" > adele_2.txt
sshyeri:~/workspace $ echo "rolling in the deep" >> adele_2.txt
sshyeri:~/workspace $ diff adele.txt adele_2.txt
2c2
< Rolling In the Deep
---
> rolling in the deep
```

### **cat **

**adele.txt 내용 CLI창에서 보기**

```
sshyeri:~/workspace $ cat adele.txt
Someone Like You
```

### head

**맨 앞 10줄**

```
$ head sonnets.txt
$ head -18 sonnets.txt  ---> 18줄
```

### tail

**맨 뒤 10줄**

```
$ tail sonnets.txt
$ tail -18 sonnets.txt  ---> 18줄
```

### **wc**

**파일 안에 줄, 단어 , 바이트(word count)**

```
sshyeri:~/workspace $ wc sonnets.txt
 2621 17671 95642 sonnets.txt
```

### **|**

**좌측의 출력을 오른쪽에 입력으로**

**좌측 작업의 결과물만 가지고 오른쪽 명령 실행**

```
sshyeri:~/workspace $ head sonnets.txt | wc
     10      46     294
     
$ head -18 sonnets.txt | tail -14 ---> ch1에서 뒤의 14줄 출력
```

less 파일 보는거?

u, d 빈페이지 앞, 뒤

f, b 한페이지 앞 뒤

/검색단어	n누르면 앞으로, shift+n 누르면 반대로

1G 첫 줄

100G 100번째 줄

G 막 줄

```
   -n, --line-number
          Prefix  each line of output with the 1-based line number within its input file.  (-n is specified by POSIX.)
sshyeri:~/workspace $ grep -n rose sonnets.txt

sshyeri:~/workspace $ grep -n rose sonnets.txt | head -1
```

루트 디렉토리

```
$ cd /
```

~ 홈 디렉토리

```
$ cd 
$ cd ~
```

현재 위치 확인

```
$ pwd
```

모든 텍스트파일 옮기기

```
sshyeri:~/workspace $ mv *.txt text_files/
sshyeri:~/workspace $ ls
README.md  cli_test/  google.log  text_files/
```

dir1안에 dir2 폴더 생성

```
$ mkdir -p dir1/dir2
```

cd - 이전 디렉토리

```
$ mv cd -
```

&& 명령어 결합

```
$ cd .. && git add . && git commit -m "asdf" && git push && cd -
```

foo폴더 이름을 bar로 변경

```
$ mv foo/ bar/
```

text_files 자체를 가져옴(복사)

```
$ cp -r ../text_files . 
```

text_files안의 내용물만 가져옴(복사)

```
$ cp -r ../text_files/ .
```

디렉토리 삭제

```
$ rm -rf second_dir/
```

sesquipedalian 문자열 있는 파일 검색

```
 $ grep -r sesquipedalian text_files 
 text_files/foo/long_word.txt:sesquipedalian
 $ grep -ir sesquipedalian text_files
 text_files/foo/long_word.txt:sesquipedalian
```

*i : 대소문자 구별 없이*