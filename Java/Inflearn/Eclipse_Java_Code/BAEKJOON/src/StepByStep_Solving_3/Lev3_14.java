package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_14 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		for (int i = 1; i <= a; i++) {
			int x = keyboard.nextInt();
			int y = keyboard.nextInt();
			System.out.print("Case #" + i + ": ");
			System.out.println(x + y);
		}
		keyboard.close();
	}
}