class Solution:
    def reverseWords(self, s: str) -> str:
        # better approach
        # traversing through the given string, making every word first and storing it in a temp var word
        # appending each word to another temp arr words, after encountering a space in word

        words = []
        word = ""

        # extracting the words
        for c in words:
            if c != " ":
                word += c
            elif word:
                words.append(word)

        # adding remaining last word
        if word:
            words.append(word)

        
        # reversing the list of words
        words.reverse()

        # joing all words with a single space.
        return ' '.join(words)


# optimal approach
class Solution:
    def reverseWords(self, s: str) -> str:
        # optimal approach using one pass
        # splitting by spaces, reversing and joining the words
        return ' '.join(s.strip().split()[::-1])
