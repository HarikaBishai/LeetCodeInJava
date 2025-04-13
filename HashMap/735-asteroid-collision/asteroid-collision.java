class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stk= new Stack<>();

        for(int num: asteroids) {
            
            if (stk.isEmpty() || !(stk.peek() > 0 && num < 0)) {
                stk.push(num);
            } else {
                
                while(!stk.isEmpty() && (stk.peek() > 0 && num < 0)  ) {
                    int top = stk.pop();

                    if(Math.abs(num) < Math.abs(top) ) {
                        num = top;
                    } else if(Math.abs(num) == Math.abs(top)) {
                        num = 0;
                    }
                }
                if(num!=0) {
                    stk.push(num);
                }
            }
        }

        int[] result = stk.stream().mapToInt(Integer::intValue).toArray();
        return result;
    }
}