import java.util.Scanner;

public class Star7 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		for (int i = 0; i < a; i++) {
			for (int j = i + 1; j < a; j++) {
				System.out.print(" ");
			}
			for (int k = 0; k <= 2*i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		for (int i = 1; i < a; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print(" ");
			}
			for (int k = 1; k < 2*(a - i); k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}