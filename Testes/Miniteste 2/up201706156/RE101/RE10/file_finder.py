# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 11:42:41 2018

@author: joao

3)
Let dirs be a recursively-defined nested list, representing a directory tree containing an
arbitrary number of directories, sub-directories and files.
Consider the following example:
dirs =
["home",
     ["Documents",
          [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
          [ "Python", "hello_world.py", "readme.md" ],
     ],
     ["Downloads",
          [ "Movies",
              [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                "1.avi", "22", "001.mp4"
          ],
     ],
     "tmp.txt", "page.html"
]

In the above example, each directory is defined by a list, and the first element of the list is the
name of that directory (home, Documents, FPRO, etc). The rest of the elements of a list contain
either strings, which are filenames inside that directory, or lists, which contain a sub-directory.
Write a Python function file_finder(dirs, file_name) that returns the full path of a file
file_name (given as a string), or None if it is not in the directory tree dirs. The full path of a
file includes the slash-separated names of all the directories that contain it. Therefore, the full
path of "BreakingBad.mp4" is "home/Downloads/Movies/TV Series/BreakingBad.mp4".
Save the program in the file file_finder.py
For example:
● file_finder(dirs, 'Documents') returns: None (because Documents is a
sub-directory not a file)
● file_finder(dirs, 'recursion.pdf') returns the string:
"home/Documents/FPRO/recursion.pdf"
"""
def file_finder(dirs, file_name):

    for element in dirs:
#        print('element:',element)
        result = dirs[0] + '/'
        if type(element) == list:
#            print('\n\t begin recursion')
            if file_name == element[0]:
                return
            result += file_finder(element, file_name)         
#            print('\t end recursion\n')
        else:
            if element == file_name:
                result += file_name
                break
#        print('result:',result,'\n')

        check_result = result[::-1]
        slash_ix = check_result.find('/')
    #    print('check_result:',check_result[:slash_ix])
        if check_result[:slash_ix] == file_name[::-1]:
#            print('check_result:',check_result[:slash_ix])
            return result
    return result

#print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'Documents'))
#print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'page.html'))
print(file_finder(['home', ['Documents', ['FPRO', 'lists.txt', 'recursion.pdf', 'functions'], ['Python', 'hello_world.py', 'readme.md']], ['Downloads', ['Movies', ['TV Series', 'BreakingBad.mp4', 'TheBigBangTheory.avi'], '1.avi', '22', '001.mp4']], 'tmp.txt', 'page.html'], 'hello_world.py'))



