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

import java.util.HashSet;

class Result {

    /*
     * Complete the 'getMinimumUniqueSum' function below.
     *
     * The function is expected to return an INTEGER. The function accepts
     * INTEGER_ARRAY arr as parameter.
     */

    public static int getMinimumUniqueSum(List<Integer> arr) {
        // Write your code here
        // Set<Integer> setNew = new HashSet<Integer>(arr);
        List<Integer> a = new ArrayList<Integer>();

        Integer[] item = arr.toArray(new Integer[arr.size()]);
        for (int i = 0; i < item.length; i++) {
            for (int j = i + 1; j < item.length; j++) {
                if (item[i] == item[j]) {
                    System.out.println(item[j]);
                    a.add(item[j]);
                }
            }
        }

        List<Integer> b = new ArrayList<Integer>();
        for (int i : a) {
            b.add(i + 1);
        }

        List<Integer> newList = new ArrayList<Integer>(arr);
        newList.addAll(b);

        List<Integer> setNew = newList.stream().distinct().collect(Collectors.toList());

        System.out.println(setNew);
        int sum = 0;
        for (int i : setNew) {
            sum += i;
        }
        return sum;
    }

}

public class Solution {