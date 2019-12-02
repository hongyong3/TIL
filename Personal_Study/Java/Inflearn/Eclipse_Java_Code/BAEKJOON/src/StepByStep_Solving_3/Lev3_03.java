package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_03 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 int a = keyboard.nextInt();
		 keyboard.close();
		 for (int i = 1; i <= 9; i++)
			 System.out.println(a + " * " + i + " = " + a*i);

	}

}
