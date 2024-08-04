import java.util.Scanner;

class Solution{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int test_case = 1; test_case <= 10; test_case++){
            int tc = sc.nextInt();
            int [][] matrix = new int[100][100];
            for(int i = 0; i < 100; i++){
                for(int j = 0; j < 100; j++){
                    matrix[i][j] = sc.nextInt();
                }
            }
            int maximum = 0; int temp = 0;

            for(int i1 = 0; i1 < 100; i1++){    //가로합
                temp = 0;
                for(int j1 = 0; j1 < 100; j1++){
                    temp += matrix[i1][j1];
                }
                if (maximum < temp){
                    maximum = temp;
                }
            }

            for(int j2 = 0; j2 < 100; j2++){    //세로합
                temp = 0;
                for(int i2 = 0; i2 < 100; i2++){
                    temp += matrix[i2][j2];
                }
                if (maximum < temp){
                    maximum = temp;
                }
            }

            temp = 0;                       //초기화 for문 전에
            for(int i3 = 0; i3 < 100; i3++){    //대각합
                temp += matrix[i3][i3];
            }
            if (maximum < temp){
                maximum = temp;
            }
            
            temp = 0;
            for(int i4 = 0; i4 < 100; i4++){
                temp += matrix[i4][99-i4];
            }
            if (maximum < temp){
                maximum = temp;
            }

            System.out.printf("#%d %d\n", tc, maximum);
        }      
    }
}