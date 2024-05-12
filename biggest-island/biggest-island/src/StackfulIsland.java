import java.util.List;
import java.util.Random;
import java.util.Stack;

public class StackfulIsland {
    int rows = 5;
    int cols = 5;
    int[][] grid = new int[rows][cols];
    boolean[][] visited = new boolean[rows][cols];
    int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    StackfulIsland() {
        Random random = new Random();
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
        Stack<List<Integer>> stack = new Stack<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (visited[i][j]) {
                    continue;
                }

                int islandSize = 0;
                if (grid[i][j] == 1) {
                    stack.add(List.of(i, j));
                    islandSize = dfs(stack);
                    if (islandSize > largestIsland) {
                        largestIsland = islandSize;
                    }
                    System.out.printf("SIZE: %d, STARTING INDEX: (%d, %d)\n", islandSize, i, j);
                }
            }
        }

        return largestIsland;
    }

    int dfs(Stack<List<Integer>> stack) {
        int count = 0;
        while (!stack.empty()) {
            List<Integer> cell = stack.pop();
            int row = cell.get(0);
            int col = cell.get(1);
            visited[row][col] = true;
            for (int[] dir : directions) {
                if (row + dir[0] < 0 || row + dir[0] >= rows) {
                    continue;
                }
                if (col + dir[1] < 0 || col + dir[1] >= cols) {
                    continue;
                }
                if (visited[row + dir[0]][col + dir[1]]) {
                    continue;
                }
                if (grid[row + dir[0]][col + dir[1]] == 0) {
                    continue;
                }

                stack.add(List.of(row + dir[0], col + dir[1]));
            }
            count += 1;
        }

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
        StackfulIsland si = new StackfulIsland();
        si.print();
        System.out.println(si.calculate());
    }
}
