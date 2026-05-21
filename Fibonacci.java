public class Fibonacci {
    static int[] dp = new int[1001];
    static int modAdd(long a , long b)
    {
        long mod = 1000000007;
        return (int)(( (a % mod) + (b % mod) ) % mod);
    }
    static {
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i < dp.length; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
    }

    
    // Recursive method to calculate fibonacci number at index n
    public static int fibonacci(int n) {

        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
    
    // Method to print fibonacci series up to n terms
    /*public static void printFibonacciSeries(int terms) {
        for (int i = 0; i < terms; i++) {
            System.out.print(fibonacci(i) + " ");
        }
        System.out.println();
    }*/
    
    public static void main(String[] args) {
       // int n = 10;
        //System.out.println("Fibonacci series up to " + n + " terms:");
        //printFibonacciSeries(n);
        long a= 1000000000;
        long b= 1000000000;
        System.out.println(modAdd(a,b));
        System.out.println(dp[14]);
    }
}