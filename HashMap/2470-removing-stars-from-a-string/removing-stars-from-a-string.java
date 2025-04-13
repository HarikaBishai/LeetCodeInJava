class Solution {
    public String removeStars(String s) {
        // Stack<Character> stk = new Stack<>();

        // for(char c: s.toCharArray()) {

        //     if(c == '*') {
        //         if (!stk.isEmpty()) stk.pop();
        //     } else {
        //         stk.push(c);
        //     }
        // }

        // String result = stk.stream().map(String::valueOf).collect(Collectors.joining());

        // return result;

        StringBuilder sb = new StringBuilder();
        for(char c: s.toCharArray()) {
            if(c == '*') {
                if(sb.length() > 0) {
                    sb.deleteCharAt(sb.length()-1);
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}