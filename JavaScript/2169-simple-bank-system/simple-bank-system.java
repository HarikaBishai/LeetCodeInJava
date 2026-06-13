class Bank {

    private Map<Integer, Long> accounts;
    public Bank(long[] balance) {
        this.accounts = new HashMap<>();
        for (int i=0;i<balance.length;i++) {
            this.accounts.put(i+1, balance[i]);
        }
    }

    public boolean validAccount(int account) {
        return accounts.containsKey(account);
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if(!validAccount(account1) || !validAccount(account2)) {
            return false;
        }
        if(withdraw(account1, money) && deposit(account2, money)) {
            return true;
        }
        return false;
    }
    
    public boolean deposit(int account, long money) {
        if(!validAccount(account)){
            return false;
        }

        long balance = getBalance(account);
        accounts.put(account, balance+money);
        return true;
    }

    public long getBalance(int account) {
        if(!validAccount(account)){
            return -1;
        }

        return accounts.get(account);
    }
    
    public boolean withdraw(int account, long money) {
        if(!validAccount(account)){
            return false;
        }
        long balance = getBalance(account);
        if(balance < money) {
            return false;
        }
        accounts.put(account, balance-money);
        return true;


    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */