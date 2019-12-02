package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_10 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int a = keyboard.nextInt();
		int sum = 0;		
		String str = keyboard.next();
		keyboard.close();
		
		for(int i = 0; i < a; i++) {            
			sum += str.charAt(i) - '0';            
		}
		System.out.println(sum);
	}
}