# Python 101 
INDEX
> special thx to Taki

[01. Python Intro](https://github.com/djpy2/python101/blob/master/slides/Slide_01_Python_intro.ipynb)

[02. Control Flow](https://github.com/djpy2/python101/blob/master/slides/Slide_02_Control_of_flow.ipynb)

[03. Control Flow_Function](https://github.com/djpy2/python101/blob/master/slides/Slide_03_Control_of_flow_function.ipynb)

[04. Recursive Function](https://github.com/djpy2/python101/blob/master/slides/Slide_04_Recursive_function.ipynb)

[05_1. Data Structure](https://github.com/djpy2/python101/blob/master/slides/Slide_05_01_Data_structure.ipynb)

[05_2. Data Structure Dictionary](https://github.com/djpy2/python101/blob/master/slides/Slide_05_02_Dictionary_data_structure.ipynb)

[06. Module](https://github.com/djpy2/python101/blob/master/slides/Slide_06_Module.ipynb)

[07. Errors and Exceptions](https://github.com/djpy2/python101/blob/master/slides/Slide_07_Errors_and_exceptions.ipynb)

[08. OOP Intro](https://github.com/djpy2/python101/blob/master/slides/Slide_08_OOP_intro.ipynb)

[09. OOP](https://github.com/djpy2/python101/blob/master/slides/Slide_09_OOP.ipynb)

## 개요

본 Python 강의자료는 [HPHK](https://hphk.io)의 강의를 위해 작성되었으며, 외부 유출을 금합니다. 

## Python 환경설정

python version 3.6.7을 기준으로 작성되었음. 

* 윈도우 환경설정 
  1) [공식 홈페이지](https://www.python.org/downloads/release/python-367/) 설치

  * Chocolatey의 경우 다수의 인원이 동시에 접속시 문제가 생기며, 버전 관리는 차후에 진행함.
  * 설치 과정에서 **반드시 Path 설정**을 진행할 것!

  2) Git bash 적용시 아래의 명령어를 통해 python 인터프리터를 실행 할 수 있도록 설정.

  ```powershell
  $ echo "alias python='winpty python.exe'" >> ~/.bash_profile
  $ source ~/.bash_profile
  ```

* C9 환경설정 :  `pyenv`

  1) 아래의 스크립트 실행(복붙) : [gist 링크](https://zzu.li/c9)

  ```powershell
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  
  source ~/.bashrc
  pyenv install 3.6.7
  pyenv global 3.6.7
  python -V
  pip install --upgrade pip
  ```

* MAC 환경설정 : `pyenv` + `homebrew` 

  1) 아래의 스크립트 실행

  ```powershell
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew update
  brew install pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> 
  exec "$SHELL"
  pyenv install 3.6.7
  pyenv global 3.6.7
  python -V
  pip install --upgrade pip
  source ~/.bashrc
  ```
## Jupyter notebook 환경설정
본 주피터 노트북은 슬라이드 쇼로 활용할 수 있도록 구성하였음. 
### 0) Jupyter notebook 설치
```powershell
$ pip install jupyter
```

### 1) Jupyter notebook 실행
```powershell
$ jupyter notebook
```

## License

[Python 라이선스 정책](https://docs.python.org/3/license.html)을 따라 GPL-3.0을 따릅니다. 

본 강의자료는 [Python Tutorial](https://docs.python.org/3.6/tutorial/index.html)를 참조하여 만들어졌습니다.
