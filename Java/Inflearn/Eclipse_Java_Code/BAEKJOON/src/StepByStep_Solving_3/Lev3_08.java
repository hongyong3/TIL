package StepByStep_Solving_3;

import java.util.Scanner;

public class Lev3_08 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int month = keyboard.nextInt();
		int day = keyboard.nextInt();
		keyboard.close();

		int [] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		String [] daysOfTheWeeks = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

		int totalDays = day;
		for (int i = 0; i < month - 1; ++i) {
			totalDays += daysInMonth[i];
		}
		System.out.println(daysOfTheWeeks[totalDays % 7]);
	}
}