import java.util.ArrayList;
import java.util.List;

class MaxContigSum {

    static int findMaxContigSum(int array[]) {
        int cSum, gSum;
        cSum = gSum = array[0];
        for (int i = 1; i < array.length; i++) {
            cSum = Math.max(array[i], cSum + array[i]);
            gSum = Math.max(gSum, cSum);
        }
        return gSum;
    }

    public static void main(String[] args) {
        int[] a = new int[]{-1, 4, 2, -1};
        int[] b = new int[]{-5, 6, 7, 1, 4, -8, 16};
        int[] c = new int[]{-11, 4, -1, 2};
        Integer maxA = findMaxContigSum(a);
        Integer maxB = findMaxContigSum(b);
        Integer maxC = findMaxContigSum(c);

        System.out.println("Max Contig A: " +  maxA.toString());
        System.out.println("Max Contig B: " +  maxB.toString());
        System.out.println("Max Contig C: " +  maxC.toString());
    }


}