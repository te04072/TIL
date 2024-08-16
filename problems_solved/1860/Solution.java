import java.util.Scanner;
class Solution{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int tc = 0;
        for (int test_case = 1; test_case <= T; test_case++){
            tc += 1;
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();                   // 각각 손님수, 소요시간, 시간당 붕어빵수                   
            int [] customers = new int[N];
            String ans = "Possible";
            for (int i = 0; i < N; i++){        // 손님 방문 시간 배열       
                customers[i] = sc.nextInt();
            }
            int size = 11112;                    // 카운팅 정렬을 위한 최댓값                    
            int [] count = new int[size];
            for (int i = 0; i < N; i++){
                count[customers[i]]++;
            }
            for (int j = 1; j < size; j++){  // 각 초마다 방문한 손님의 누적합 배열 생성  
                count[j] += count[j-1];
            }
            for (int j = 0; j < size; j++){
                int time = j / M;
                int item = time * K;                 // 누적 붕어빵 수 초마다 계산
                if (count[j] > item){               // 누적 손님수가 붕어빵보다 많은 시점에 break       
                    ans = "Impossible";
                    break;
                }
                if (count[j] == N){             // 손님 N명을 모두 받았으면 break            
                    break;
                }
            }
            System.out.printf("#%d %s \n", tc, ans);
        }
    }
}   