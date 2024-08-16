import java.util.Scanner;
    class Solution{
        public static void main(String args[]) throws Exception{
            Scanner sc = new Scanner(System.in);
            int T = sc.nextInt();
            int K, N, M;
            for(int test_case = 1; test_case <= T; test_case++){
                int output = 0, cur = 0; 
                int [] station_list, charge_list;
                K = sc.nextInt(); N = sc.nextInt(); M = sc.nextInt();
                charge_list = new int[M];
                station_list = new int[N];
                for (int x = 0; x < M; x++){
                    charge_list[x] = sc.nextInt();
                }
                for (int i = 0; i < M; i++){
                    station_list[charge_list[i]] = 1;
                    }
                while (cur < N-K){
                    
                    for (int j = 3; j >= 1; j--) {
                        if (station_list[cur+j] == 1){
                            cur += j;
                            output += 1;
                            break;
                            }
                        }
                    if (output == 0){
                            break;
                        }
                }    
                System.out.printf("#%d %d\n", test_case, output);
                }
            }
        }
    
