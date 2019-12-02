package StepByStep_Solving_4;

import java.util.Scanner;

public class Lev4_03 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int N = keyboard.nextInt();
		int X = keyboard.nextInt();
		int [] nums = new int[N];

		for (int i = 0; i < nums.length; i++) {
			nums[i] = keyboard.nextInt();
		}

		keyboard.close();
		for (int i = 0; i < nums.length; i ++) {
			if (X > nums[i]) {
				System.out.print(nums[i] + " ");
			}
		}
	}

}
