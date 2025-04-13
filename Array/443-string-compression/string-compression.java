class Solution {
    public int compress(char[] chars) {

        int n = chars.length;
        if(n==0) return 0;

        char lastChar = chars[0];
        int count = 1;
        int index = 1;
        for(int i=1;i<n;i++) {
            char c = chars[i];
            if (c == lastChar) {
                count++;
            } 
            
            if (i == n-1 || c != lastChar) {
                if(count != 1) {
                    char[] strCount = Integer.toString(count).toCharArray();
                    for (char sc: strCount) {
                        chars[index++] = sc;
                    }
                }
                if (c != lastChar) {
                    lastChar = c;
                    chars[index++] = c;
                    count = 1;
                }
               
            }
        }

        // if (count!=1) {
        //     char[] strCount = Integer.toString(count).toCharArray();
        //     for (char sc: strCount) {
            
        //         chars[index++] = sc;
                
        //     }
        // } 
        return index;
    }
}