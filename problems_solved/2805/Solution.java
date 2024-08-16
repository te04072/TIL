import java.util.Scanner;
class Solution{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++){
            int size = sc.nextInt();
            int [][] target = new int[size][size];
            for (int i = 0; i < size*size; i++){
                String[] strInput = sc.next().split("");
                for (int j = 0; j < size; j++){
                    target[i][j] = Integer.parseInt(strInput[j]);
                }
            }
            // for (int i = 0; i < size; i++){             // 농작물 정보 입력
            //     for (int j = 0; j < size; j++){
            //         target[i][j] = sc.nextInt();
            //     }
            // }
            int output = 0;
            int mid = size/2;
            for (int i = 0; i < size; i++){
                for (int j = 0; j < size; j++){
                    if ((i <= mid) && (mid-i <= j) && (j <= mid + i)){
                        output += target[i][j];
                    }
                    else if ((i > mid) && (i-mid <= j) && (j <= 3*mid - i)){
                        output += target[i][j];
                    }
                }
            }
            System.out.printf("#%d %d\n", tc, output);
        }
    }
}

                // if (i <= mid){
                //     f
                //     for (int m = mid - i; m <= mid + i; m++){   // mid 중심, 양쪽으로 i만큼
                //         output += target[i][m];
                //     }
                // }
                // else{
                //     for (int n = i - mid; n <= 3*mid - i; n++){     // mid 중심, 양쪽으로 2mid-i(=size-i-1) 만큼
                //         output += target[i][n];
                //     }
                // }