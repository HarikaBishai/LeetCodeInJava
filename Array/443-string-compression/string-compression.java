class Solution {
    public int compress(char[] chars) {
        int out = 0;

        int n = chars.length;
        if(n==0) return out;

        char lastChar = chars[0];
        int count = 1;
        out = 1;
        int index = 1;
        for(int i=1;i<n;i++) {
            char c = chars[i];
            if (c == lastChar) {
                count++;
            } else {

                if(count != 1) {
                    char[] strCount = Integer.toString(count).toCharArray();
                    for (char sc: strCount) {
                    
                        chars[index++] = sc;
                       
                    }
                    

                }

                lastChar = c;
                chars[index++] = c;
                count = 1;
            }
        }

        if (count!=1) {
            char[] strCount = Integer.toString(count).toCharArray();
                    for (char sc: strCount) {
                    
                        chars[index++] = sc;
                       
                    }
        } 
        return index;
    }
}