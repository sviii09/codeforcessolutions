import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // declare matrix 
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] m = new int[r][c];
        
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                m[i][j] = sc.nextInt();
            }
        }

        // start and end coordinates
        int st = sc.nextInt(), sj = sc.nextInt();
        int et = sc.nextInt(), ej = sc.nextInt();
        
        boolean[][] visited = new boolean[r][c];
        int[][] dis = new int[r][c];
        
        // Initialize all distances to -1 (unreachable)
        for (int i = 0; i < r; i++) {
            Arrays.fill(dis[i], -1);
        }
        
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(st, sj));
        visited[st][sj] = true;
        dis[st][sj] = 0;
        
        while (!q.isEmpty()) {
            Pair f = q.poll();
            int i = f.i;
            int j = f.j;
            
            // up
            int newi = i - 1;
            int newj = j;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // right
            newi = i;
            newj = j + 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // down - FIXED: was j-1, should be j
            newi = i + 1;
            newj = j;  // Fixed this line
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // left
            newi = i;
            newj = j - 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // up-right
            newi = i - 1;
            newj = j + 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // up-left
            newi = i - 1;
            newj = j - 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // down-right
            newi = i + 1;
            newj = j + 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
            
            // down-left
            newi = i + 1;
            newj = j - 1;
            if (newi >= 0 && newi < r && newj >= 0 && newj < c 
                && m[newi][newj] == 1 && !visited[newi][newj]) {
                visited[newi][newj] = true;
                dis[newi][newj] = dis[i][j] + 1;
                q.add(new Pair(newi, newj));
            }
        }
        
        // Print the distance to the destination - MOVED OUTSIDE THE LOOP
        System.out.println(dis[et][ej]);
    }
    
    static class Pair {
        int i;
        int j;
        
        Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}