package StepByStep_Solving_2;

import java.util.Scanner;

public class Lev2_11 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);

		int a = keyboard.nextInt();
		int b = keyboard.nextInt();

		keyboard.close();

		b -= 45;

		if ( b < 0) {
			if ( a != 0) {
				a -= 1;
				b += 60;
			} else {
				a = 23;
				b += 60;
			}
		}
		System.out.println(a + " " + b);
	}
}