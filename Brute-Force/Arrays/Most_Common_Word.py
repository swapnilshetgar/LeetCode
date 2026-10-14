class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
                # Convert to lowercase
        paragraph = paragraph.lower()
        
        # Replace punctuation with spaces
        words = ""
        for ch in paragraph:
            if ch.isalpha():
                words += ch
            else:
                words += " "
        
        # Split into words
        words = words.split()
        
        # Find most common non-banned word
        max_count = 0
        answer = ""
        
        for word in words:
            
            # Skip banned words
            if word in banned:
                continue
            
            count = 0
            
            # Count occurrences
            for w in words:
                if w == word:
                    count += 1
            
            if count > max_count:
                max_count = count
                answer = word
        
        return answer