class BeingZero {
public ArrayList<Integer> CourseScheduleII(int numCourses, int[][] prerequisites) {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    for(int u=0; u<numCourses; u++){
        graph.put(u, new ArrayList<>());
    }
    for(int[] edge: prerequisites){
        int u = edge[0];
        int v = edge[1];
        graph.get(v).add(u);
    }
    List<Integer> ans = new ArrayList<>();
    boolean[] visited = new boolean[numCourses];
    boolean[] recStack = new boolean[numCourses];
    for(int u=0; u<numCourses; u++){
        if(!visited[u]){
            if(dfs(u, graph, visited, recStack, ans)){
                return new ArrayList<>();
            }
        }
    }
    Collections.reverse(ans);
    return new ArrayList<>(ans);

}