class Solution {

    public static boolean isInteger(String s) {
        if(s == null || s.isEmpty()) return false;
        try {
            Integer.parseInt(s);
            return true;
        } catch(Exception e) {
            return false;
        }
    }
    public String decodeString(String s) {
        Stack<String> stk = new Stack<>();

        for(char c: s.toCharArray()) {
            if(c!=']') {
                stk.push(String.valueOf(c));
            } else {
                StringBuilder currStr = new StringBuilder();

                while(!stk.isEmpty() && !stk.peek().equals("[")) {
                    currStr.append(stk.pop());
                }
                if(!stk.isEmpty()){
                    stk.pop();
                }

                StringBuilder mutilplier = new StringBuilder();

                while(!stk.isEmpty() && isInteger(stk.peek())) {
                    mutilplier.append(stk.pop());
                }

                int value = 1;

                
                if(mutilplier.length() > 0) {
                    mutilplier.reverse();
                    value = Integer.parseInt(mutilplier.toString());
                }

                // currStr.reverse();
                stk.push(currStr.toString().repeat(value));


            }
        }
        Collections.reverse(stk);
        String result =  stk.stream().collect(Collectors.joining());
        return new StringBuilder(result).reverse().toString();
       
    }
}