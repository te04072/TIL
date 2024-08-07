import java.util.Scanner;
    class Solution{
        public static main void(String args[]) throws Exception{
            Scanner sc = new Scanner(System.in);
            int T = sc.nextInt;
            int N;
            int [] target, output
            for(int test_case = 1; test_case <= T; test_case++){
                N = sc.nextInt();
                target = new int[N], output = new int[N];
                for(int i = 0; i < N; i++){
                    target[i] = sc.nextInt();
                }
                System.out.printf("#%d %d\n", test_case, output)
            }
        }
    }