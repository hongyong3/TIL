##### Self-Check List(1 / 2)

* Voter 구조체와 Proposal 구조체의 쓰임에 대해 설명할 수 있는가?

  > 각 구조체는 어떠한 정보를 담기 위함인가?

  * 구조체를 구성하는 각 변수

  > 구조체와 구조체의 리스트를 선언하고 사용할 수 있는가?



* msg.sender는 무엇을 뜻하는가?

  > msg.sender와 같은 특성을 갖는 변수를 무엇이라 지칭하는가?



* 조건문, 반복문을 사용할 수 있는가?



* 생성자 및 함수의 선언을 이해할 수 있는가?



##### Self-Check List (2 / 2)

* 생성자 및 함수의 동작을 설명할 수 있는가?

  > constructor
  >
  > givRightToVote(address toVoter)
  >
  > delegate(address to)
  >
  > vote(unit8 toProposal)
  >
  > winningProposal() returns (unit8 _winningProposal)

* givRightToVote 함수의 if문을 require문으로 변경할 수 있는가?

* 함수 내 storage 변수를 설명할 수 있는가?

* Openzeppelin SafeMath 라이브러리를 사용하여 코드를 변경할 수 있는가?



* Ballot.sol은 모든 참가자에게 투표권을 부여할 수 있는 형태인가?

  여러 투표에 투표할 수 있는 컨트랙트로 확장할 수 있는 방법은 무엇인가?



#### 솔리디티 개발 과제 3

##### 스마트 컨트랙트 요구사항 명세

* 솔리디티 컴파일러는 0.4.18 버전 이상을 사용한다.

  > 주요차이

  * view -> constant
  * 생성자 -> function ContractName() ~



* ERC20을 준수하는 토큰의 특징은 다음과 같다.

  > Token name = MyCustomToken
  >
  > Token symbol = "MCT"
  >
  > Token total supply = 1000000000 (10억개)
  >
  > Token decimals = 18
  >
  > Token per ETH = 10(1 eth 당 10 MCT)



* 필수적으로 구현해야 할 컨트랙트 및 함수는 다음과 같다.

  > contract ERC20TokenInterface{}

  * ERC20 표준에서 요구하는 인터페이스 정의
  * 참고 : https://theethereum.wiki/w/index.php.ERC20_Token_Standard

  > contract ERC20Token is ERC20TokenInterface{}

  * ERC20TokenInterface 컨트랙트를 상속하는 컨트랙트
  * ERC20Token 인터페이스를 구현

  > contract MyCustomToken is ERC20Token{}

  * ERC20Token 컨트랙트를 상속하는 컨트랙트
  * 컨트랙트 생성자
  * function balanceOf(address) : 해당 주소의 잔액을 반환하는 함수
  * function transfer() : 컨트랙트 혹은 주소로 토큰을 전송하는 함수



#### 솔리디티 개발 과제 4

##### 스마트 컨트랙트 요구사항 명세

* 스마트 컨트랙트 이름 : contract SafeMathTest{...}

* 이더리움 솔리디티 오픈소스 라이브러리 openzeppelin 사용

  > import"<openzeppelin directory or url>" // 위치에 맞게 변경 혹은 remix 전용 import 구문(하단) 사용

  * import "https://github.com/OpenZeppelin/openzeppelin-solidity/con"



#### 솔리디티 개발 과제 5