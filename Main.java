import java.util.*;
class Main{
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int nv = sc.nextInt();
        int ne = sc.nextInt();
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int u=0; u<nv; u++){
            graph.put(u, new ArrayList<>());
        }
        for(int i=0; i<ne; i++){
            int u = sc.nextInt();
            int v = sc.nextInt();
            System.out.println(u + " " + v);
            graph.get(u).add(v);//dir+undir graph
            graph.get(v).add(u);// undir graph


        }
        int [] inv = new int[nv];
        for(int u=0; u<nv; u++){
            System.out.print(u + ":");
            for(int v: graph.get(u)){
                System.out.print(v + " ");
                inv[v]++;
            }
            System.out.println();
        }
    }
}