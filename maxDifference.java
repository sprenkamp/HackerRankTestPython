import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'maxDifference' function below.
     *
     * The function is expected to return an INTEGER. The function accepts
     * INTEGER_ARRAY arr as parameter.
     */

    public static int maxDifference(List<Integer> arr) {
        // Write your code here

        List<Integer> a = new ArrayList<Integer>();
        List<Integer> b = new ArrayList<Integer>();
        for (int i : arr) {
            if (a.size() > 0) {
                for (int j : a) {
                    if (i > j) {
                        int c = i - j;
                        b.add(c);
                    } else {
                        int c = i - j;
                        b.add(c);
                    }
                }
            }
            a.add(i);

        }
        int d = Collections.max(b);
        return d;

    }

}

public class Solution {