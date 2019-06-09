package Section1;
import java.util.Scanner;

public class Code11 {

	public static void main(String[] args) {
		Scanner keyboard = new Scanner(System.in);
		int n = keyboard.nextInt();
		int [] data = new int [n];
		
		for (int i = 0; i < n; i++)
			data[i] = keyboard.nextInt();
		keyboard.close();
		
		int count = 0;
		for(int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {	// i < j 경우만
				if (data[i] == data[j])
					count++;
			}
		}
		System.out.println("중복된 숫자쌍은 " + count + "개입니다.");
	}

}
