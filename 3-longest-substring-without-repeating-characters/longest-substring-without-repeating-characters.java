class Solution {
    public int lengthOfLongestSubstring(String s) {
        List<Character> lis=new ArrayList<>();
        int max_length=0;
        for(char i:s.toCharArray()){
            if(lis.contains(i)){
                lis = new ArrayList<>(lis.subList(lis.indexOf(i) + 1, lis.size()));
            }
            lis.add(i);
            max_length=Math.max(max_length,lis.size());
        }
        return max_length;
    }
}