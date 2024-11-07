/* A sentence is a list of words that are separated by a single space 
with no leading or trailing spaces.

Words consist of only uppercase and lowercase English letters. 
Uppercase and lowercase English letters are considered different.

A sentence is circular if:
- The last character of a word is equal to the first character of the next word.
- The last character of the last word is equal to the first character of the first word.

Task: Given a string sentence, return true if it is circular. Otherwise, return false.
*/

import ( 
    "fmt" 
    "strings" 
) 

func isCircularSentence(sentence string) bool {
        words := strings.Split(sentence, " ")
        for i := 1; i < len(words); i++ {
            if words[i][0] != words[i-1][len(words[i-1])-1] {
                return false
                    }
                }
        if sentence[0] == sentence[len(sentence)-1] {
            return true
                }
        return false
}

