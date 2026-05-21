import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0) {
            long x = sc.nextLong();
            long a = sc.nextLong();  // blue pen price
            long b = sc.nextLong();  // black pen price
            long c = sc.nextLong();  // pencil price
            
            long pens = 0;  // number of each type of pen
            long pencils = 0;
            
            // If either pen is not available (price 0), we can't buy any pens
            if(a == 0 || b == 0) {
                pens = 0;
            } else {
                // Find maximum number of pairs (one blue + one black) we can buy
                // Each pair costs (a + b)
                pens = x / (a + b);
            }
            
            // Calculate money spent on pens
            long spentOnPens = pens * (a + b);
            
            // Remaining money
            long remaining = x - spentOnPens;
            
            // Buy pencils if available and if there's money left
            if(c > 0 && remaining > 0) {
                pencils = remaining / c;
            } else {
                pencils = 0;
            }
            
            // Output: blue pens, black pens (same), pencils
            System.out.println(pens + " " + pens + " " + pencils);
        }
        sc.close();
    }
}