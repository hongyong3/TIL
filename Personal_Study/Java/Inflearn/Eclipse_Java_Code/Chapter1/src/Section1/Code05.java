package Section1;

public class Code05 {

	public static void main(String[] args) {
		// declare the array
		int [] grades;		// �迭�� ����ϱ� ���ؼ��� ���� �̷��� �迭�� ����

		// allocate memory for 5 indices
		grades = new int[5];	// �迭�� ũ�⸦ �����ϸ鼭 �����Ѵ�.
        						// ���� �迭�� ��������� ������ ����
        						// �� �� ������ �� �������� ���� �� �ִ�.
        						// int[] grades = new int [5];
				
		// assign some values to the array
		grades[0] = 100;	// �迭�� �� ĭ�� �����͸� �����ϰ�,
		grades[1] = 76;		// ����� �����͸� �б� ���ؼ� []�� ���
		grades[2] = 92;		// �迭�� �ε����� 0���� �����Ѵ�.
		grades[3] = 95;
		grades[4] = 14;

		// print out each value
		System.out.println(grades[0]);
		System.out.println(grades[1]);
		System.out.println(grades[2]);
		System.out.println(grades[3]);
		System.out.println(grades[4]);

	}

}
