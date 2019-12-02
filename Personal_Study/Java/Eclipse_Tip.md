

####  Eclipse Tip

- `자동완성기능을 제공`한다. 단축키는 `ctrl+space`

- 코드 블럭을 선택하고 `ctrl+i`를 누르면 자동으로 들여쓰기를 정리해준다. 습관들 들이자.

- 초보자의 경우 뭘 `import`해야 하는지 알기 어렵다. import문 없이 먼저 코드를 작성한 후

  Eclipse의 메뉴 `"Source > OrganizeImports"`를 실행하면 자동으로 필요한 import문을 생성해 준다.

  단축키는 `ctrl+Shift+O`

---

```java
package arabiannight.tistory.com.java.test;
 
public class TestFor {
    public static void main(String[] args) {
         
        int i = 1;
         
        System.out.println(++i); // 먼저 +
        System.out.println(i++); // 나중 +
         
        System.out.println(i--); // 나중 -
        System.out.println(--i); // 먼저 -
         
    }
}

---
결과
++i = 2
++i = 2
i-- = 3
--i = 1
```

