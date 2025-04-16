class Solution {
    public int reverse(int x) {
        int n=Math.abs(x);
        int reverse=0;
        while(n>0){
            int a=n%10;
            if (reverse > (Integer.MAX_VALUE - a) / 10) {
                return 0; // Return 0 if overflow would occur
            }
            reverse=(reverse*10)+a;
            n=n/10;
        }
        return (x<0)?-reverse:reverse;
    }
}