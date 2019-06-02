import java.util.Scanner;

public class Code09 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 System.out.print("숫자를 입력하세요.");
		 int n = keyboard.nextInt();
		 int [] data = new int [n];
		 for (int i = 0; i < n; i++)
			 data[i] = keyboard.nextInt();
		 keyboard.close();
		 
		 int tmp = data[n-1];
		 for (int i = n-2; i >= 0; i--)
			 data[i+1] = data[i];
		 data[0] = tmp;
		 
		 for (int i = 0; i < n; i++)
			 System.out.println(data[i]);
	}

}
