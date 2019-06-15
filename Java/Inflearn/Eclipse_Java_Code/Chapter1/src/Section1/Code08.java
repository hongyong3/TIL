package Section1;
import java.util.Scanner;

public class Code08 {

	public static void main(String[] args) {

		Scanner keyboard = new Scanner(System.in);
		System.out.print("몇 개의 숫자를 입력하시겠습니까? :");
		int n = keyboard.nextInt();
		System.out.println("숫자를 입력하세요.");
		int [] data = new int [n];
		for (int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();

		int sum = 0;
        // int max = 0; 만약 입력받는 숫자가 모두 양수라면 이렇게 써도 문제가 없지만 
		int max = data[0];	// 입력받은 숫자가 음수라면 문제가 있기 때문에 이렇게 쓴다.
		for ( int i = 0; i < n; i++) {
			sum += data[i];	// sum = sum + data[i];
			if (data[i] > max)
				max = data[i];
		}
		System.out.println("The sum is " + sum);
		System.out.println("The max is " + max);

	}

}