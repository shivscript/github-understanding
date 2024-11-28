import matplotlib.pyplot as plt
from collections import Counter

# List representing the letters of your name
list_a = ['S', 'I', 'D', 'D', 'H', 'A', 'R', 'T', 'H']

print(Counter("Sidhartha"))

# Counting the occurrences of each letter
s = list_a.count('S')
i = list_a.count('I')
d = list_a.count('D')
h = list_a.count('H')
a = list_a.count('A')
t = list_a.count('T')
r = list_a.count('R')

# Lists for x-axis (letters) and y-axis (counts)
letters = ['S', 'I', 'D', 'A', 'H', 'T', 'R']
counts = [s, i, d, a, h, t, r]

# Creating the line plot
plt.plot(letters, counts, marker='D', linestyle='-', color='b')

# Adding labels and title
plt.xlabel('Letters')
plt.ylabel('Counts')
plt.title('Letter Frequencies in the Name "Siddarth"')

# Displaying the plot
plt.show()
