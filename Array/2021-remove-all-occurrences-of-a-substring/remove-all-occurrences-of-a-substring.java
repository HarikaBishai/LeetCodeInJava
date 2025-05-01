class Solution {

    public String removeOccurrences(String s, String part) {

        Deque<Character> dq = new ArrayDeque<>();

        StringBuilder sb= new StringBuilder();
        int partLen = part.length();

        for(char c: s.toCharArray()) {
            dq.push(c);

            while(dq.size()>=partLen) {
                StringBuilder temp= new StringBuilder();
                Iterator<Character> it = dq.iterator();
                for(int i = partLen-1; i>=0;i--) {
                    char curr = it.next();
                    if(curr!= part.charAt(i)) {
                        break;
                    }
                    temp.append(curr);
                }

                if(temp.length() < partLen) {
                    break;
                }
                int i=0;
                while(i< partLen) {
                    dq.pop();
                    i++;
                }
            }
        }

        while(!dq.isEmpty()) {
            sb.append(dq.pop());
        }

        sb.reverse();
        return sb.toString();

        
    }
}