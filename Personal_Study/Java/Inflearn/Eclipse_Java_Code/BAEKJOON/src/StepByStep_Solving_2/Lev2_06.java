package StepByStep_Solving_2;

import java.util.Scanner;

public class Lev2_06 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		int b = keyboard.nextInt();
		int c = keyboard.nextInt();
		System.out.println((a + b) % c);
		System.out.println((a % c + b % c) % c);
		System.out.println((a * b) % c);
		System.out.println((a % c * b % c) % c);
		keyboard.close();
	}
}