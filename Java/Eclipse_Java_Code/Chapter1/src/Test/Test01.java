package Test;
import java.util.Scanner;

public class Test01 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		System.out.print("몇 개의 숫자를 입력받겠습니까?: ");
		int n = keyboard.nextInt();
		int [] data = new int[n];
		System.out.println(n +"개의 숫자를 입력하세요.");
		for ( int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();
		System.out.println("");
		int tmp = data[n-1];
		for (int i = n - 2; i >= 0; i--)
			data[i+1] = data[i];
		data[0] = tmp;
		
		for (int i = 0; i < n; i++)
			System.out.print(data[i] + " ");


	}

}
