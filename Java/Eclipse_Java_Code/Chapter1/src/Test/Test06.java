package Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Test06 {

	public static void main(String[] args) {
		
		String [] name = new String[1000];
		String [] number = new String[1000];
		int a = 0;
		
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
			System.exit(9);
		}
		
		for (int i = 0; i < a; i++) {
			System.out.println(name[i] + " : "+ number[i]);
		}
	}
}
