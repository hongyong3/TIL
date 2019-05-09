# HTML

Hyper Text Markup Language

### 닫는 태그가 없는 태그 : a, img

### Semantic tag

개발자 및 사용자 뿐만 아니라 검색엔진(구글, 네이버)등에 의미 있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 태그들을 활용하기 위한 노력.

> non semantic : div, span 등

#### header

헤더(문서 전체나 섹션의 헤더)

#### nav

내비게이션

#### aside

사이드에 위치한 공간으로, 메인 콘텐츠와 관련성이 적은 콘텐츠에 사용

#### section

문서의 일반적인 구분으로 컨텐츠의 그룹을 표현하며, 일반적으로 **h1**~**h6** 요소를 가짐.

#### article

문서, 페에지, 사이트 안에서 독립적으로 구분되는 영역(포럼/신문 등의 글 또는 기사)

#### footer

푸터(문서 전체나 섹션의 푸터)

### 기타 태그

#### b, strong : 볼드

#### i, em : 이탤릭

#### mark : 마크

#### del : 취소선

#### ins : 밑줄

#### sup : 윗첨자

#### sub : 아랫첨자

#### pre : 입력한 그대로 보여줌.

#### q: 큰따옴표

#### blockqoute : 인용구 표현시

#### ol : ordered list

#### ul : unordered list

​	안의 요소들은 li

# Css

상대단위 :

​	사이즈 기준 : font-size

​	em: 상속된 사이즈나 디폴트 사이즈에 상대적인 사이즈

```
<style>
      html { font-size: 16px; }
      body { font-size: 1.5em; }
      .a { font-size: 2.0em; }
</style>
</head>
<body>
    <p class="a">Lorem Ipsum Dolor</p>
</body>
```

> 16 * 1.5 * 2.0 = 48px

rem: 루트 사이즈의 배수

```
<style>
      html { font-size: 16px; }
      body { font-size: 1.5rem; }
      .a { font-size: 2.0rem; }
</style>
</head>
<body>
    <p class="a">Lorem Ipsum Dolor</p>
</body>
```

> 16 * 2 = 32px

선택자 우선순위 : 인라인>ID>Class, : >Tag>*

- 그룹으로 표현시 그룹이 가진 갯수에 따라서.
- 중복된 경우 가장 css에서 마지막에 선언된 설정이 적용

| 선택자                                                       | 예         | 예 설명                             | CSS  |
| ------------------------------------------------------------ | ---------- | ----------------------------------- | ---- |
| [.*class*](http://www.w3schools.com/css/sel_class.asp)       | .intro     | class="intro"인 모든 요소를 선택    | 1    |
| [#*id*](http://www.w3schools.com/css/sel_id.asp)             | #firstname | id="firstname"인 모든 요소를 선택   | 1    |
| [*](http://www.w3schools.com/css/sel_all.asp.asp)            | *          | 모든 요소를 선택                    | 2    |
| *element*                                                    | p          | 요소를 모두 선택                    | 1    |
| *element,element*                                            | div,p      | 모든요소와요소를 선택               | 1    |
| [*element* *element*](http://www.w3schools.com/css/sel_element_element.asp) | div p      | 요소 안에 있는 모든요소를 선택      | 1    |
| [*element*>*element*](http://www.w3schools.com/css/sel_element_gt.asp) | div>p      | 부모(상위) 요소가인 모든요소를 선택 | 2    |
| [*element*+*element*](http://www.w3schools.com/css/sel_element_pluss.asp) | div+p      | 요소 바로 뒤에 있는 모든요소를 선택 | 2    |

# Bootstrap

1-0.25rem, 브라우저 기본 : 16px

mt-2 : 0.5rem : 8px

mt-3 : 1rem : 16px

mt-4 : 1.5rem : 24px

mt-5 : 3 : 48px