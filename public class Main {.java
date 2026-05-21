public class Main {
    static dp[][]=new int[1001][1001]; // stores answer for each i and j

public static void main(String[] args) 
{
    Scanner sc = new Scanner(System.in);
    String s1=sc.nextLine();
    String s2=sc.nextLine();
    // use array.fill
        for(int i=0;i<1001;i++) {
            Arrays.fill(dp[i],-1);
        }
/*   for(int i=0;i<1001;i++) {
        for(int j=0;j<1001;j++) {
            dp[i][j]=-1;
        }
    }*/

    int ans=lcs(s1,s2,0,0);
    System.out.println(ans);
}
//top-down dp approach
int lcs(String s1,String s2, int i,int j) {
    if(i>=s1.length() || j>=s2.length()) {
    return 0;}
    if(dp[i][j]!=-1) {
        return dp[i][j];
    }
    if(s1.charAt(i)==s2.charAt(j)){
    return dp[i][j]=1+lcs(s1,s2,i+1,j+1);}
    else{
    return dp[i][j]=Math.max(lcs(s1,s2,i+1,j),lcs(s1,s2,i,j+1));}

}

}

