import java.util.Scanner;

public class Star9 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		for (int i = 0; i < a; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print(" ");
			}
			for (int k = 0; k < 2*(a - i) - 1; k++) {
				System.out.print("*");
			}
			for (int l = 0; l < i; l++) {
				System.out.print(" ");
			}
			System.out.println();
		}

		for (int i = 1; i < a; i++) {
			for (int j = 1; j < a - i; j ++) {
				System.out.print(" ");
			}
			for (int k = 0; k <= 2 * i; k++) {
				System.out.print("*");
			}
			for (int l = 1; l < a - i; l++) {
				System.out.print(" ");
			}
			System.out.println();
		}
	}

}
