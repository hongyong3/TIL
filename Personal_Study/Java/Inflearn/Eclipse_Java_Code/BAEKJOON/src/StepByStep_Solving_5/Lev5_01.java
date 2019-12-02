package StepByStep_Solving_5;

import java.util.Scanner;

public class Lev5_01 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		while(keyboard.hasNextInt()){
			int a = keyboard.nextInt();
			int b = keyboard.nextInt();
			if(a > 0 && b > 0) {
				System.out.println(a + b);
			}
		}
		keyboard.close();
	}
}