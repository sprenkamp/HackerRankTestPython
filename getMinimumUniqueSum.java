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
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static int getMinimumUniqueSum(List<Integer> arrayList) {
    // Write your code here
    //Set<Integer> setNew = new HashSet<Integer>(arr);
    Collections.sort(arrayList);
   
    Integer[] A = arrayList.toArray(new Integer[arrayList.size()]); 
    int n = A.length;

    int sum = A[0];
    int prev = A[0];

    for( int i = 1; i < n; i++ ) {
        int curr = A[i];

        if( prev >= curr ) {
            curr = prev+1;
        }
        sum += curr;
        prev = curr;
    }

    return sum; 
 }

}

public class Solution {