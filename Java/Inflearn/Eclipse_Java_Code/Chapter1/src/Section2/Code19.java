package Section2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Code19 {

	public static void main(String[] args) {

		String [] name = new String [1000];
		String [] number = new String [1000];
		int a = 0;

		try {
			Scanner inFile = new Scanner(new File("input.txt"));

			while (inFile.hasNext()) {	// hasNext() �޼���� ������ ���� �����ߴ��� �˻��Ѵ�. detect End of File
				name[a] = inFile.next();
				number[a] = inFile.next();
				a++;
			}

			inFile.close();
		} catch (FileNotFoundException e) {
			System.out.println("No File");
			//			return;
			//			System.exit(0);	// �������� ����
			//			System.exit(1);	// ���������� ����
			System.exit(9);
		}

		for (int i = 0; i < a; i++) {
			System.out.println(name[i] + " : " + number[i]);
		}
	}
}