package StepByStep_Solving_1;

import java.util.Scanner;

public class Lev1_10 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);

		int a = keyboard.nextInt();
		int b = keyboard.nextInt();
						
		keyboard.close();

		int ans1 = a * (b % 10);
		int ans2 = a * (b % 100 - (b % 10)) / 10;
		int ans3 = a * (b / 100);
		System.out.println(ans1);
		System.out.println(ans2);
		System.out.println(ans3);
		System.out.println(ans1 + (ans2 * 10) + (ans3 * 100));
	}
}