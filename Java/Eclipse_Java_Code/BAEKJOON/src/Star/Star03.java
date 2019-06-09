package Star;
import java.util.Scanner;

public class Star03 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		for (int i = 0; i < a; i++) {
			for (int j = a - i; j >= 1; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}
