package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_13 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		for (int i = 0; i < a; i++) {
			int x = keyboard.nextInt();
			int y = keyboard.nextInt();
			System.out.println(x + y);
		}
		keyboard.close();
	}
}