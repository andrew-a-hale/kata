import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class NaiveIsland {
    int size = 5;
    int area = size * size;
    int[] grid;
    Random random = new Random();
    Set<Integer> seenCells = new HashSet<>();

    public NaiveIsland() {
        grid = new int[area];
        for (int i = 0; i < grid.length; i++) {
            if (random.nextBoolean()) {
                grid[random.nextInt(grid.length)] = 1;
            }
        }
    }

    public void getConnectedCells(Set<Integer> connectedCells, int cell) {
        // check left
        if (cell > 0 && cell % size != 0 && !connectedCells.contains(cell - 1)) {
            connectedCells.add(cell - 1);
            if (grid[cell - 1] == 1) {
                getConnectedCells(connectedCells, cell - 1);
            }
        }

        // check up
        if (cell >= size && !connectedCells.contains(cell - size)) {
            connectedCells.add(cell - size);
            if (grid[cell - size] == 1) {
                getConnectedCells(connectedCells, cell - size);
            }
        }

        // check right
        if (cell < area - 1 && cell % size != (size - 1) && !connectedCells.contains(cell + 1)) {
            connectedCells.add(cell + 1);
            if (grid[cell + 1] == 1) {
                getConnectedCells(connectedCells, cell + 1);
            }
        }

        // check down
        if (cell < area - size && !connectedCells.contains(cell + size)) {
            connectedCells.add(cell + size);
            if (grid[cell + size] == 1) {
                getConnectedCells(connectedCells, cell + size);
            }
        }
    }

    public long largestIsland() {
        long largestIsland = 0;
        for (int i = 0; i < area; i++) {
            // skip seen
            if (seenCells.contains(i)) {
                continue;
            }

            // calculate largest island connected to ith cell
            Set<Integer> connectedCells = new HashSet<>();
            connectedCells.add(i);
            long islandSize = 0;
            if (grid[i] == 1) {
                getConnectedCells(connectedCells, i);
                islandSize = connectedCells.stream().filter(x -> grid[x] == 1).count();
                if (islandSize > largestIsland) {
                    largestIsland = islandSize;
                }
            }

            // merge seen cells
            seenCells.addAll(connectedCells);
        }

        return largestIsland;
    }

    public void print() {
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < grid.length; i++) {
            int value = 0;
            if (grid[i] == 1) {
                value = i;
            }
            out.append(String.format(" %02d,%d ", value, grid[i]));
            if (i % size == 4) {
                out.append("\n");
            }
        }
        System.out.println(out);
    }

    public static void main(String[] args) {
        NaiveIsland map = new NaiveIsland();
        map.print();
        long largestIsland = map.largestIsland();
        System.out.println(largestIsland);
    }
}