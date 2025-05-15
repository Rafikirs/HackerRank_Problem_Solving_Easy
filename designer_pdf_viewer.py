def designerPdfViewer(h, word):
    max_height = max(h[ord(char) - ord('a')] for char in word)
    return max_height * len(word)
