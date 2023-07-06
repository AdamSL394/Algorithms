class Solution {
    public boolean rotateString(String s, String goal) {
        int len = s.length();

        if(len  == goal.length() &&  len > 0){
            String ss = s + s;
            return ss.contains(goal);
        }
        return false;
    }
}