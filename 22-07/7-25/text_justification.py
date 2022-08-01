# Text Justification is the problem of fitting a sequence of n space separated words into a column of
# lines with constant width s, to minimize the amount of white-space between words. Each word can
# be represented by its width wi < s. A good way to minimize white space in a line is to minimize
# badness of a line. Assuming a line contains words from wi to wj , the badness of the line is defined
# as b(i, j) = (s − (wi + . . . + wj ))3 if s > (wi + . . . + wj ), and b(i, j) = ∞ otherwise. A good
# text justification would then partition words into lines to minimize the sum total of badness over all
# lines containing words. The cubic power heavily penalizes large white space in a line. Microsoft
# Word uses a greedy algorithm to justify text that puts as many words into a line as it can before
# moving to the next line. This algorithm can lead to some awful lines. LATEX on the other hand
# formats text to minimize this measure of white space using a dynamic program. Describe an O(n2)
# algorithm to fit n words into a column of width s that minimizes the sum of badness over all lines
# containing words.
