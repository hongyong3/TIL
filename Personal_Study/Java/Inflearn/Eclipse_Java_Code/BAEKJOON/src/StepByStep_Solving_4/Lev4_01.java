package StepByStep_Solving_4;

import java.util.Scanner;

public class Lev4_01 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();

		if (a >= 90) {
			System.out.println("A");
		} else if (a >= 80) {
			System.out.println("B");
		} else if (a >= 70) {
			System.out.println("C");
		} else if (a >= 60) {
			System.out.println("D");
		} else {
			System.out.println("F");
		}
	}
}