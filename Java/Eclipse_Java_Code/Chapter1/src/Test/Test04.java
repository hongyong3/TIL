package Test;
import java.util.Scanner;

public class Test04 {

	public static void main(String[] args) {
		
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		int [] data = new int [n];
		
		for (int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();

		int maxSum = 0;
		for (int i = 0; i < n; i++) {
			int sum = 0;
			for (int j = i; j < n; j++) {
				sum += data[j];
				if (sum > maxSum)
					maxSum = sum;
			}
		}
		System.out.println("The max sum is " + maxSum);
	}

}
