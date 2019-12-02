package StepByStep_Solving_6;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Lev6_02 {

	public static void main(String[] args) throws Exception {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder ans = new StringBuilder();
		int max = 0;
		int index = 0;

		for (int i = 0; i < 9; i++) {
			int a = Integer.parseInt(keyboard.readLine());
			if (max < a) {
				max = a;
				index = i + 1;
			}
		}
		ans.append(max).append('\n').append(index);
		System.out.println(ans);
	}
}