// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int n, String s) {
    String str[] = s.split(" ");
    List<String> occupied = new ArrayList<>();
    int available = 0;

    occupied = Arrays.asList(str);

    for(int i = 1; i<= n ; i++) {

            if(!occupied.contains(i+"A") && !occupied.contains(i+"B") && !occupied.contains(i+"C")) {
                available++;
            }
            if(!(occupied.contains(i+"D") && occupied.contains(i+"G"))  && !(occupied.contains(i+"E") || occupied.contains(i+"F"))) {
                available++;
            }
            if(!occupied.contains(i+"H") && !occupied.contains(i+"J") && !occupied.contains(i+"K")) {
                available++;
            }
   }
    return available;
    }
}