// package LAB13;

import java.util.HashMap;

public class CharacterOccurrence {
    public static void main(String[] args) {
        String str = "programming";

        HashMap<Character, Integer> charCount = new HashMap<>();

        for (char c : str.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        for (char c : charCount.keySet()) {
            System.out.println("'" + c + "' occurs " + charCount.get(c) + " times.");
        }
    }
}