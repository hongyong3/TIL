package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_11 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		String str = keyboard.next();
		keyboard.close();

		for (int i = 0; i < str.length(); i++) {
			System.out.print(str.charAt(i));
			if (i % 10 == 9) {
				System.out.println();
			}
		}
	}
}