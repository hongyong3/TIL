import java.util.Scanner;

public class Test03 {

	public static void main(String[] args) {
		 Scanner keyboard = new Scanner(System.in);
		 int n = keyboard.nextInt();
		 int [] data = new int [n];
		 
		 for (int i = 0; i < n; i++)
			 data[i] = keyboard.nextInt();
		 keyboard.close();
		 
		 for (int i = 0; i < n; i++) {
			 for (int j = 0; j < n; j++) {
				 // data[i] data[j]
			 }
		 }
	}

}
