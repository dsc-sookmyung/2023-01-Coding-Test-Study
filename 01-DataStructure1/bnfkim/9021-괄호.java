import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();

            for(int j=0; j<str.length(); j++){
                char ch = str.charAt(j);

                if (ch == '(') {
                    stack.push(ch);
                } else {
                    if (stack.empty()){
                        stack.push(ch);
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }
            if(stack.empty()) {
                sb.append("YES").append("\n");
            }
            else {
                sb.append("NO").append("\n");
            }
        }
        System.out.println(sb);
    }
}