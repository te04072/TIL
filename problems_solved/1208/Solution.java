import java.util.Scanner;  // 미완
import java.util.Arrays;

class Solution{
    public static void main(String args[]) throws Exception{
        Scanner sc = new Scanner(System.in);
        for(int test_case = 1; test_case <= 10; test_case++){
            int T;
            T = sc.nextInt();
            int [] boxes = new int[100];    // 박스 100개 입력  int의 wrapper class인 Integer 사용
            for(int x = 0; x < 100; x++){
                boxes[x] = sc.nextInt();
            }
            for(int times = 1; times <= T ; times++){
                Arrays.sort(boxes);
                boxes[0] += 1; boxes[99] -= 1;
            }
            Arrays.sort(boxes);     // 마지막에 대소판정 한 번 더
            int output = boxes[99] - boxes[0];
            System.out.printf("#%d %d\n", test_case, output);
        }
        sc.close();
    }

}
