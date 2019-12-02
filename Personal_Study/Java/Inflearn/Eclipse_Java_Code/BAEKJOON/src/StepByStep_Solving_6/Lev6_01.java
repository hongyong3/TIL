package StepByStep_Solving_6;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Lev6_01 {
	public static StringTokenizer st;

	public static void main(String[] args) throws Exception {
		BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(keyboard.readLine());
		st = new StringTokenizer(keyboard.readLine(), " ");
		int[] num = new int[a];
		
		int i = 0;
		while (st.hasMoreTokens()) {
			num[i] = Integer.parseInt(st.nextToken());
			i++;
		}
		
		Arrays.sort(num);
		System.out.print(num[0] + " " + num[num.length - 1]);
	}
}