import java.io.*;
import java.util.*;
public class Main {
    static int[][] arr = new int[5][5]; //빙고판
    static int result = 0; //체크
    public static void main(String[] args) throws IOException {

        /**
         * N -> 관찰 횟수
         * 소의 번호 & 위치
         */

        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        StringTokenizer st;

        //빙고판 입력받기
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        for(int x=0; x<25; x++){
            int num = sc.nextInt();

            //부른 값은 0으로 체크하기
            for(int i=0; i<5; i++){
                for(int j=0; j<5; j++) {
                    if(arr[i][j] == num)  arr[i][j] = 0;
                }
            }

            //빙고 체크하기
            rowCheck();
            colCheck();
            diagonalL();
            diagonalR();

            //빙고 3개 이상일 시 불린 숫자 출력
            if(result >= 3) {
                System.out.println(x+1);
                break;
            }
            //빙고 체크 후 다시 리셋해주어야함
            result = 0;
        }
    }

    public static void rowCheck() {
        for(int i=0; i<5; i++){
            int count = 0;
            for(int j=0; j<5; j++){
                if(arr[i][j] == 0) count++;
            }
            if(count == 5) result++;
        }
    }

    public static void colCheck() {
        for(int i=0; i<5; i++){
            int count = 0;
            for(int j=0; j<5; j++){
                if(arr[j][i] == 0) count++;
            }
            if(count == 5) result++;
        }
    }

    public static void diagonalL() {
        int count = 0;
        for(int i=0; i<5; i++) {
            if(arr[i][i] == 0) count++;
        }
        if(count == 5) result++;
    }
    public static void diagonalR() {
        int count = 0;
        for(int i=0; i<5; i++) {
            if(arr[i][4-i] == 0) count++;
        }
        if(count == 5) result++;
    }
}