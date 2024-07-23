import java.util.Scanner;

public class Solution{
    public static int is369(int x){
        if (x != 0 && x % 3 == 0){
            return 1;
        }
        else {
            return 0;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a, b, c;
        for (int i = 1; i <= N; i++){
            a = i / 100; b = (i / 10) % 10; c = i % 10;
            int count = is369(a) + is369(b) + is369(c);
            if (count > 0){
                char dash = '-';
                String ans = Character.toString(dash);
                ans = ans.repeat(count);
                System.out.print(ans + " ");
            }
            else {
                String ans;
                ans = Integer.toString(i);
                System.out.print(ans + " ");
            }
        }
        sc.close();
    }
}