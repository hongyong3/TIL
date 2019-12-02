package StepByStep_Solving_5;

import java.util.Scanner;

public class Lev5_03 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		int ans = a;
		int count = 0;

		do {
			ans = ans % 10 * 10 + (ans / 10 + ans % 10) % 10;
			count++;
		} while (a != ans);

		System.out.println(count);
	}
}