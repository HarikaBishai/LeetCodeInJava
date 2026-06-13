class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> out = new ArrayList<>();

        int i = 0;

        while (i<words.length) {
            int j = i;
            List<String> line = new ArrayList<>();
            line.add(words[j]);
            int len = words[j].length();
            
            while(j+1<words.length && len+words[j+1].length() + line.size()<=maxWidth) {
                j++;
                line.add(words[j]);
                len += words[j].length();
            }

            StringBuilder sb = new StringBuilder();
            int spaces = maxWidth - len;
            int lineSize = line.size();

            if( j == words.length-1 || lineSize == 1) {
                sb.append(line.get(0));
                for(int k = 1; k< lineSize; k++) {
                    sb.append(" ");
                    sb.append(line.get(k));
                }
                int rem = maxWidth - sb.length();
                sb.append(" ".repeat(rem));
            } else {
                int gaps = lineSize - 1;
                int base = spaces / gaps;
                int extra = spaces % gaps;
                sb.append(line.get(0));
                for(int k = 1;k<lineSize; k++){
                    int gap_space = base;
                    if(k-1<extra) {
                        gap_space++;
                    }
                    sb.append(" ".repeat(gap_space));
                    sb.append(line.get(k));

                }
            }

            out.add(sb.toString());

            i = j+1;
            

        }
        return out;
    }
}