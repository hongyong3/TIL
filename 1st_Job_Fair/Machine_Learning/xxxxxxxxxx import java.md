```java
import java.util.Scanner;

public class Star2 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 int a = keyboard.nextInt();
		 for (int i = 1; i <= a; i++) {
			 for (int j = 1; j <= a - i; j++) {
				 System.out.print(" ");
			 }
			 for (int j = 1; j <= a; j++) {
				 System.out.print("*");
			 }
			 System.out.println();
		 }
		 keyboard.close();

	}

}

```

5

*****

*****
*****
*****
*****