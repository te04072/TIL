import java.util.Scanner;
//import java.io.FileInputStream;

public class Solution{
   public static void main(String args[]) throws Exception{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int [] moneyKey = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
        int [] output = new int[8];
        for(int test_case = 1; test_case <= T; test_case++){
            int price = sc.nextInt();
            for(int i = 0; i < 8; i++){
                int division = price / moneyKey[i];
                output[i] = division;
                price %= moneyKey[i];
            }
            System.out.printf("#%d %d\n", test_case, output);
        }
        sc.close();
        }
    }