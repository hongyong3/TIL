package StepByStep_Solving_4;

import java.util.Scanner;

public class Lev4_05 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int C = keyboard.nextInt();
		int N, total, count;
		double avg;
		int [] scores = new int[1000];

		for (int i = 0; i < C; ++i) {
			N = keyboard.nextInt();
			total = 0;
			count = 0;

			for (int j = 0; j < N; ++j) {
				scores[j] = keyboard.nextInt();
				total += scores[j];
			}

			avg = (double)total / N;

			for (int j = 0; j < N; ++j) {
				if (scores[j] > avg) {
					count++;
				}
			}

			System.out.printf("%.3f", 100.0 * count / N);
			System.out.println("%");
		}
		keyboard.close();
	}
}