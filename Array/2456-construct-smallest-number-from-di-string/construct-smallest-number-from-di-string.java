class Solution {
    public String smallestNumber(String pattern) {

        StringBuilder out = new StringBuilder();
        Stack<Integer> stk = new Stack<>();
        int counter = 1;
        stk.push(counter);
        for(char c: pattern.toCharArray()) {
            if(c == 'I') {
                while(!stk.isEmpty()) {
                    out.append(stk.pop());
                } 
            }
          
            stk.push(++counter);
           
        }

        while(!stk.isEmpty()) {
            out.append(stk.pop());
        }
        return new String(out);
    }
}