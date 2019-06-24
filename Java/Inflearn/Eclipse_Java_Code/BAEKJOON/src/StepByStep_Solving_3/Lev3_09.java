package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_09 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		keyboard.close();
		
		int b = 0;
		for (int i = 1; i <= a; i++) {
			b += i;
		}
		System.out.println(b);

	}

}
