import java.util.Random;

public class LargestIsland {
    int rows = 10;
    int cols = 10;
    int[][] grid = new int[rows][cols];
    boolean[][] visited = new boolean[rows][cols];
    Random random = new Random();

    public LargestIsland() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (random.nextDouble() > 0.5) {
                    grid[i][j] = 1;
                }
            }
        }
    }

    int calculate() {
        int largestIsland = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (visited[i][j]) {
                    continue;
                }

                int islandSize = 0;
                if (grid[i][j] == 1) {
                    islandSize = dfs(grid, i, j);
                    if (islandSize > largestIsland) {
                        largestIsland = islandSize;
                    }
                    System.out.printf("SIZE: %d, STARTING INDEX: (%d, %d)\n", islandSize, i, j);
                }
            }
        }

        return largestIsland;
    }

    int dfs(int[][] grid, int row, int col) {
        boolean invalidRow = row < 0 || row >= rows;
        boolean invalidCol = col < 0 || col >= cols;
        if (invalidRow || invalidCol) {
            return 0;
        }

        if (visited[row][col] || grid[row][col] == 0) {
            return 0;
        }

        visited[row][col] = true;

        int count = 1;
        count += dfs(grid, row + 1, col);
        count += dfs(grid, row - 1, col);
        count += dfs(grid, row, col + 1);
        count += dfs(grid, row, col - 1);
        return count;
    }

    void print() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                System.out.printf(" %d ", grid[i][j]);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        LargestIsland li = new LargestIsland();
        li.print();
        System.out.println(li.calculate());
    }
}
