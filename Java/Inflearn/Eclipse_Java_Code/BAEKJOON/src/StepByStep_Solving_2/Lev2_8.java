package StepByStep_Solving_2;

import java.util.Scanner;

public class Lev2_8 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		if (a % 5 == 0) {
			System.out.println(a / 5);
			return;
		}
		else {
			int resultA = a / 5;

			for (int i = resultA; i > 0; i--) {
				int ans = a - (i * 5);

				if ( ans % 3 == 0) {
					System.out.println(i + (ans / 3));
					return;
				}
			}
		}

		if (a % 3 == 0) {
			System.out.println(a / 3);
		}
		else {
			System.out.println(-1);
		}
		return;
	}
}