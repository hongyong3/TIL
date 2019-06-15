package Section2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Code20 {

	static String [] name;
	static String [] number;
	static int a = 0;

	public static void main(String[] args) {

		name = new String[1000];
		number = new String[1000];

		try {
			Scanner inFile = new Scanner(new File("input.txt"));

			while (inFile.hasNext()) {
				name[a] = inFile.next();
				number[a] = inFile.next();
				a++;
			}
			inFile.close();

		} catch (FileNotFoundException e) {
			System.out.println("Not File");
			System.exit(1);
		}

		bubbleSort();

		for (int i = 0; i < a; i++) {
			System.out.println(name[i] + " : " + number[i]);
		}
	}

	public static void bubbleSort() {
		for (int i = a - 1; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				if (name[j].compareTo( name[j + 1] ) > 0 ) {	// Str1.equals(str2) // str1 == str2´Â ¾ÈµÊ.
					// swap name[j] and name[j + 1]
					String tmp = name[j];
					name[j] = name[j + 1];
					name[j + 1] = tmp;

					tmp = number[j];
					number[j] = number[j + 1];
					number[j + 1] = tmp;
				}
			}
		}
	}
}
