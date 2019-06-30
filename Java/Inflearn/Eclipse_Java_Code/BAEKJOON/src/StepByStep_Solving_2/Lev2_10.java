package StepByStep_Solving_2;

import java.util.Scanner;

public class Lev2_10 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		if (a % 4 == 0 && a % 100 != 0) {
			System.out.println("1");
		} else if (a % 400 == 0) {
			System.out.println("1");			
		} else {
			System.out.println("0");
		}

	}

}
