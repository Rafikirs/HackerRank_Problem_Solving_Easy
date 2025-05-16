# Exercise: Designer PDF Viewer
# URL: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true
# Description:
# Given the heights of each letter, compute the area of the highlighted rectangle 
# when selecting a word in a PDF viewer. The area is the height of the tallest letter times the word's length.

def designerPdfViewer(h, word):
    max_height = max(h[ord(char) - ord('a')] for char in word)
    return max_height * len(word)
