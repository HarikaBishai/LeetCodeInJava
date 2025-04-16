class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> out = new ArrayList<>();

        int row = 0;

        while(row<numRows) {
            List<Integer> rowArray = new ArrayList<>();

            for(int i=0;i<=row;i++) {
                if(i==0) {
                    rowArray.add(1);
                } else if(i==row) {
                    rowArray.add(1);
                } else {
                    if(row-1>=0 && i-1>=0)
                        rowArray.add(out.get(row-1).get(i-1) + out.get(row-1).get(i) );
                }
            }
            out.add(rowArray);

            row++;
        }
        return out;

    }
}