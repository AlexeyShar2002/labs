int minOperations(int n){
    int k = 0, cnt = 0;
    while(k <= n/2) {
        for (int i = 0; i < (n - 1 - 2 * k); i++) {
            cnt++;
        }
        k++;
    }
    return cnt;
}