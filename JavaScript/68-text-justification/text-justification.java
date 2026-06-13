class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        

        List<String> out = new ArrayList<>();
        int i = 0;
        while(i < words.length){
            List<String> line = new ArrayList<>();
            int j = i;
            
            line.add(words[j]);
            int len = words[j].length();
            while (j+1 <words.length && len + words[j+1].length() + line.size() <= maxWidth ) {
                line.add(words[j+1]);
                len += words[j+1].length();
                j+=1;
            }
            
            int spaces = maxWidth - len;
            boolean last_line = (j == words.length -1);
            int line_size = line.size();
            if(last_line || line_size == 1) {
                
                int base = spaces / line_size;

                StringBuilder sb = new StringBuilder();
                sb.append(line.get(0));
                for (int k=1;k<line_size;k++){
                    sb.append(" ");
                    sb.append(line.get(k));
                    
                }

                int rem = maxWidth - sb.length();
                if(rem > 0) {
                     sb.append(" ".repeat(rem));
                    
                }
                out.add(sb.toString());
               
            } else {
            
                int gaps = line.size()-1;
            
                int base = spaces / gaps;
                int extra = spaces % gaps;


                StringBuilder sb = new StringBuilder();
                sb.append(line.get(0));
                for (int k =1;k<line.size();k++){
                    int space_gap = base;
                    if (k-1 < extra) {
                        space_gap+=1;
                    }
                    sb.append(" ".repeat(space_gap));
                    sb.append(line.get(k));
                }
                out.add(sb.toString());
            }
            i = j+1;
        }
        return out;
    }
}