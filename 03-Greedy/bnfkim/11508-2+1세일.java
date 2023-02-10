import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        Integer[] goods = new Integer[N];

        for(int i=0;i<N;i++) goods[i] = scan.nextInt();
        Arrays.sort(goods, Comparator.reverseOrder());

        int sum = 0;
        for(int i=0;i<N;i++){
            if(i%3==2) continue;
            sum += goods[i];
        }
        System.out.println(sum);
    }
}