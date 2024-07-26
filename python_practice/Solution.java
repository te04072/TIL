import java.util.Scanner;
// import java.util.Arrays;
// import java.util.Collections;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int test_case = 1; test_case <= 10; test_case++){
            int T = sc.nextInt(); int ans = 0;
            int [] Building;
            Building = new int[T];
            for(int i = 0; i < T; i++){
                Building[i] = sc.nextInt();
            }
            for(int t = 2; t < T-2; t++){
                int [] Sample;
                Sample = new int[5];
                // Sample = Arrays.copyOfRange(Building, t-2, t+3);
                for(int j = 0; j < 5; j++){
                    Sample[j] = Building[t+j-2];
                }
                // Arrays.sort(Sample);
                // Arrays.sort(Sample, Collections.reverseOrder());
                for(int x = 0; x < 5-1; x++){
                    for(int y = 0; y < 5-x-1; y++){
                        if (Sample[y] < Sample[y+1]){
                            int temp = Sample[y];
                            Sample[y] = Sample[y+1];
                            Sample[y+1] = temp;
                        }
                    }
                }
                if(Sample[0] == Building[t]){
                    ans += (Sample[0] - Sample[1]);
                }
            }
            System.out.printf("#%d %d\n", test_case, ans);
        }
        sc.close();
    }
}
