class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if(numerator == 0) return "0";
        StringBuilder s = new StringBuilder();

        if((numerator < 0) ^ (denominator < 0)) {
            s.append("-");
        }

        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);

        s.append(num/den);

        long rem = num % den;
        if(rem == 0) {
            return s.toString();
        }

        s.append(".");

        Map<Long, Integer> map = new HashMap<>();
        while(rem!=0) {
            if(map.containsKey(rem)) {
                int index = map.get(rem);
                s.insert(index, "(");
                s.append(")");
                break;
            }

            map.put(rem, s.length());
            rem = rem*10;

            s.append(rem/den);
            rem = rem%den;
        }

        return s.toString();



    }
}