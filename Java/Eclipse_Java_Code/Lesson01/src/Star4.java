import java.util.Scanner;

public class Star4 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 int a = keyboard.nextInt();
		 keyboard.close();
		 
		 for (int i = 0; i < a; i++) {
			 for (int j = a-i; j < a; j++) {
				 System.out.print(" ");
			 }
			 for (int k = i; k < a; k++) {
				 System.out.print("*");
			 }
			 System.out.println();
		 }
	}
}