package StepByStep_Solving_4;

import java.util.Scanner;

public class Lev4_04 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int N = keyboard.nextInt();
		double total = 0;
		double max = 0;
		double score;

		for (int i = 0; i < N; i++) {
			score = keyboard.nextInt();
			total += score;
			if (score > max) {
				max = score;
			}
		}
		keyboard.close();

		double avg = 0;
		avg = total * 100 / max / N;
		System.out.println(avg);
	}
}