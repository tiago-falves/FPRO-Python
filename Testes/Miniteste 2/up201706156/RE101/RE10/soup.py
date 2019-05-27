# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:42:42 2018

@author: joao

4)
Write a function soup(matrix, word) that, given a matrix of letters, returns the first
location of the word in the matrix.
For example, let's say we have the following matrix and are trying to find the word "PORTO".
  1 2 3 4 5 6
A X A B N T O
B Y T N R I T
C U P O M D S
D I O H U O O
E R T E L Q X
F I W J K P Z
Then the function returns "C2" because the word starts in line=C, column=2.
Notice that the words can be in any direction: northwest, north, northeast, east, southeast,
south, southwest or west.
All letters are given in upper-case and the function returns the first occurrence of the word using
lexicographical order (i.e. if the word can be found in "A4" and "B2", then it returns "A4").
Save the program in the file soup.py
For example:
● mx = (('X', 'A', 'B', 'N', 'T', 'O'),
('Y', 'T', 'N', 'R', 'I', 'T'),
('U', 'P', 'O', 'M', 'D', 'S'),
('I', 'O', 'H', 'U', 'O', 'O'),
('R', 'T', 'E', 'L', 'Q', 'X'),
('I', 'W', 'J', 'K', 'P', 'Z'))
● soup(mx, 'PORTO')) returns the string "C2" (as illustrated above)
● soup(mx, 'HOTEL') returns the string "D3"
● soup(mx, 'RIO') returns the string "B4"
"""
def soup(matrix, word):
    def search(row,col,ix_letter):
        possible= []
        next_letter = ix_letter + 1
        if next_letter == len(word):
            return 1
        passou = False
        for irow in range(-1,2):
            for icol in range(-1,2):      
                
                if irow == 0 and icol == 0:
                    continue
                if row == 0:
                    if irow == -1:
                        continue
                if row == len(matrix[0]) - 1:
                    if irow == 1:
                        continue
                if col == 0:
                    if icol == -1:
                        continue
                if col == len(matrix[0]) - 1:
                    if icol == 1:
                        continue
                
                new_row = row+irow
                new_col = col+icol
                test_letter = word[next_letter]
#                print('test_letter:',word[next_letter],'letter_in_mx:',matrix[new_row][new_col])
                if matrix[new_row][new_col] == test_letter:
#                    print('a')
                    passou = True
                    possible.append((new_row,new_col))
#        print('possible:',possible)
        for test in possible:
            find = search(test[0],test[1],next_letter)
            if find == 1:
                return 1
        if not passou:
            return 0
    dic = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
    poss = []
    for ixr,row in enumerate(matrix):
        for ixc,element in enumerate(row):
            if word[0] == element:
                poss.append((ixr,ixc))

    for possibility in poss:
        found = search(possibility[0],possibility[1],0)
        row_name = dic[possibility[0]]
        column_name = str(possibility[1]+1)
#        print('found:',found)
        if found == 1:
            return row_name + column_name
    return "The word '{}' can't be found in this soup!".format(word)
                    

mx = (('R', 'T', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'), ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z'))
print(soup(mx, 'TIRNO'))

#'R', 'T', 'B', 'N', 'T', 'O'
#'Y', 'T', 'N', 'R', 'I', 'T'
#'U', 'P', 'O', 'M', 'D', 'S'
#'I', 'O', 'H', 'U', 'O', 'O'
#'R', 'T', 'E', 'L', 'Q', 'X'
#'I', 'W', 'J', 'K', 'P', 'Z'



