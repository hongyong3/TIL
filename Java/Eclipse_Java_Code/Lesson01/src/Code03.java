import java.util.Scanner;

public class Code03 {

	public static void main(String[] args) {
		String str = "Hello";
		String input = null;	// String input;이라고 해도 된다. String input;과 String input = null;은 같은 의미
		
		Scanner keyboard = new Scanner(System.in);
		System.out.print("Please type a string: ");

		input = keyboard.next();

		if(str == input) {
			System.out.println("Strings match! :-)");
		} else {
			System.out.println("Strings do not match! :-(");
		}
		keyboard.close();
	}

}
