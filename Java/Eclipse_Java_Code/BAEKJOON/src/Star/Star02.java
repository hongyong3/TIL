package Star;
import java.util.Scanner;

public class Star02 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 int a = keyboard.nextInt();
		 keyboard.close();
		 
		 for (int i = 0; i < a; i++) {
			 for (int j = i + 1; j < a; j++) {
				 System.out.print(" ");
			 }
			 for (int k = a - i; k <= a; k++) {
				 System.out.print("*");
			 }
			 System.out.println();
		 }
	}

}
