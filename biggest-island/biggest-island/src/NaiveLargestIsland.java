public class NaiveLargestIsland {
    public static void main(String[] args) {
        Map map = new Map();
        map.print();
        long largestIsland = map.largestIsland();
        System.out.println(largestIsland);
    }
}
