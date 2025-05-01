class Solution {

    private Stack<Character> stk;

    public boolean checkEqual(String part) {
        Stack<Character> temp = new Stack<>();
        temp.addAll(stk);
        for(int i = part.length()-1; i>=0;i--) {
            if(temp.peek()!=part.charAt(i)) {

                return false;
            }
            temp.pop();
        }
        return true;
    }

    public String removeOccurrences(String s, String part) {

        stk = new Stack<>();

        StringBuilder sb= new StringBuilder();

        for(char c: s.toCharArray()) {
            stk.push(c);

            while(stk.size()>=part.length() && checkEqual(part)) {
                for(int i = 0; i<part.length();i++) {
                    stk.pop();
                }
            }
        }

        while(!stk.isEmpty()) {
            sb.append(stk.pop());
        }

        sb.reverse();
        return sb.toString();

        
    }
}