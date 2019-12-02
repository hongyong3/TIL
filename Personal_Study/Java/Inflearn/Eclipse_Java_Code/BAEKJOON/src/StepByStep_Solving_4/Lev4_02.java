package StepByStep_Solving_4;

import java.util.Arrays;
import java.util.Scanner;

public class Lev4_02 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int [] nums = new int[3];

		for (int i = 0; i < nums.length; i++) {
			nums[i] = keyboard.nextInt();
		}

		keyboard.close();

		Arrays.sort(nums);
		System.out.println(nums[1]);
	}
}