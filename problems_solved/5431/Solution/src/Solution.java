import java.util.Scanner;

public class Solution {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int test_case = 1; test_case <= T; test_case++) {
            int total = sc.nextInt();
            int passed_number = sc.nextInt();
            int[] result_list = new int[total];
            for (int x = 1; x <= total; x++) {
                result_list[x-1] = x;                   // 전체 학생 번호 배열
            }
            for (int i = 0; i < passed_number; i++) {
                int temp = sc.nextInt();                // 제출한 번호 입력 받을 때마다 배열의 해당 요소 0으로 교체
                result_list[temp - 1] = 0;
            }
            System.out.printf("#%d ", test_case);
            for (int j = 0; j < total; j++) {           // 0이 아닌 요소만 출력
                if (result_list[j] != 0) {
                    System.out.printf("%d ", result_list[j]);
                }
            }
            System.out.println("");
        }
    }
}