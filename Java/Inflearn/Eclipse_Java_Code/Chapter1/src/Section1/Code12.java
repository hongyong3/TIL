package Section1;
import java.util.Scanner;

public class Code12 {

	public static void main(String[] args) {
		
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		int [] data = new int [n];
		
		for (int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();

		int maxSum = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i; j < n; j++) {
				int sum = 0;
				for (int k = i; k <=j; k++)
					sum += data[k];
				if (sum > maxSum)
					maxSum = sum;
			}
		}
		System.out.println("The max sum is " + maxSum);
	}

}
