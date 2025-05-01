class Solution {
    public int compress(char[] chars) {
        int out = 0;
        if(chars.length == 0){
            return out;
        }

        char last = chars[0];
        int count = 1;
        
        int index = 0;
        for(int i =1;i<chars.length;i++) {
            char curr = chars[i];
            
            if(last!=curr) {
                chars[index++] = last;
                if(count > 1) {
                    for(char c: (count+"").toCharArray()) {
                        chars[index++] = c;
                    }
                    count = 1;
                }
                last = curr;
                
            } else {
                count++;
            }
        }

        chars[index++] = last;
        if(count > 1) {
            for(char c: (count+"").toCharArray()) {
                chars[index++] = c;
            }
        }

        return index;


        
    }
}