package StepByStep_Solving_2;

import java.util.Scanner;

public class Lev2_09 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		int b = keyboard.nextInt();
		keyboard.close();

		if (a > b) {
			System.out.println(">");
		} else if (a < b) {
			System.out.println("<");
		} else {
			System.out.println("==");
		}
	}
}