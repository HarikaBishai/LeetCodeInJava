class Solution {
    public String reverseWords(String s) {
        
        List<String> words = Arrays.stream(s.split(" ")).filter(word -> !word.isEmpty()).collect(Collectors.toList());

        Collections.reverse(words);

        return String.join(" ", words);

    }
}