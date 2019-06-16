package StepByStep_Solving_1;

import java.util.Scanner;

public class Lev1_7 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 while (keyboard.hasNextLine()) {
			 String a = keyboard.nextLine();
			 
			 if (a.isEmpty() || a.length() > 100) {
				break; 
			 }
			 else {
				 System.out.println(a);
			 }
		 }
		 keyboard.close();
	}
}
