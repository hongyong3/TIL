package Section1;
import java.util.Scanner;

public class Code04 {

	public static void main(String[] args) {
		 String name = null;	// ����� �̸��� ���� �Է¹��� �ʾƼ� null ��
		 int age;
		 String gender;
		 
		 Scanner keyboard = new Scanner(System.in);
		 System.out.print("Please type your name and your age and your gender: ");
		 
		 name = keyboard.next();
		 age = keyboard.nextInt();
		 gender = keyboard.next();
		 keyboard.close();
		 
		 if(gender.equals("male"))	// string literal
			 System.out.println(name + ", you're " + age + " years old man.");
		 else if (gender.equals("female"))
			 System.out.println(name + ", you're " + age + "years old woman.");
		 else
			 System.out.println("Hmm... interesting.");

	}

}