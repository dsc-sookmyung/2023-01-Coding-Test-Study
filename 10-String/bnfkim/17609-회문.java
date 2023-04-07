import java.io.*;

public class Main {
    static char[] word;
    static class Position {
        int left;
        int right;
        public Position(int left, int right){
            this.left = left;
            this.right = right;
        }
    }
    public static void main(String[] args) throws IOException {
        /**
         * T : 주어지는 문자열의 개수
         * 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            word = br.readLine().toCharArray();
            Position position = new Position(0, word.length-1);

            if(isPalindrome(position)){
                System.out.println(0);
            } else {
                if(isPalindrome(new Position(position.left+1, position.right))
                        || isPalindrome(new Position(position.left, position.right-1))) {
                    System.out.println(1);
                } else {
                    System.out.println(2);
                }
            }
        }
    }
    static boolean isPalindrome(Position position){
        while (position.left <= position.right) {
            if (word[position.left] == word[position.right]) {
                position.left++;
                position.right--;
            } else {
                return false;
            }
        }
        return true;
    }
}