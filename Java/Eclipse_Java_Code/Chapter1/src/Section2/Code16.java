package Section2;

import java.util.Scanner;

public class Code16 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Please enter two integers and press Enter.");
		
		int a = keyboard.nextInt();
		int b = keyboard.nextInt();

		int result = power(a, b);

		System.out.println("The result is " + result);
		keyboard.close();
	}

	public static int power( int m, int n )	// return type
	{
		int prod = 1;
		for (int i = 0; i < n; i++)
//			prod = prod * m;
			 prod *= m;	// ���� �ǹ�

		return prod;

	}
}