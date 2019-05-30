import java.util.Scanner;

public class Code02 {

	public static void main(String[] args) {

		int number = 123;

		Scanner keyboard = new Scanner(System.in);	// import 필요 	keyboard라는 이름의 Scanner를 만든다.

		System.out.print("please enter an integer: ");
		int input = keyboard.nextInt();
		if(input == number) {
			System.out.println("Numbers match! :-)");
		}
		else {
			System.out.println("Numbers do not mathch! :-(");
		}

		keyboard.close();
	}

}
