import java.util.Scanner;
//import java.io.FileInputStream;

public class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int lenM, lenN, output;
        int [] M, N;
        for(int test_case = 1; test_case <= T; test_case++)
        {
            lenM = sc.nextInt(); lenN = sc.nextInt(); output = 0;
            M = new int[lenM]; N = new int[lenN];
            for(int i = 0; i < lenM; i++){
                M[i] = sc.nextInt();
            }
            for(int i = 0; i < lenN; i++){
                N[i] = sc.nextInt();
            }
            if (lenM < lenN){
                int temp = lenM; lenM = lenN; lenN = temp;
                int [] tempM = M; M = N; N = tempM;
            }
            int lenDiff = lenM - lenN + 1;
            int [] sumlist = new int[lenDiff];
            for(int i = 0; i < lenDiff; i++){
                for (int j = 0; j < lenN; j++){
                    sumlist[i] += M[i+j] * N[j];
                }
                if (output < sumlist[i]){
                    output = sumlist[i];
                }
            }
            System.out.printf("#%d %d\n", test_case, output);
        }
       sc.close();
    }
}
