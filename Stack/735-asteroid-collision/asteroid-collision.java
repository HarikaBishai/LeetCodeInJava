class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stk= new Stack<>();

        for(int num: asteroids) {
            
           boolean alive = true;
           while(alive && num < 0 && !stk.isEmpty() && stk.peek() > 0) {
                int top = stk.peek();

                if(Math.abs(num) > top) {
                    stk.pop();
                } else if(Math.abs(num) == top) {
                    stk.pop();
                    alive = false;
                } else {
                    alive = false;
                }
           }
           if (alive) stk.push(num);
        }

        return stk.stream().mapToInt(Integer::intValue).toArray();


        
    }
}