# Assignment-2-MapReduce

_You must use MapReduce to complete this assignment._ <br>

Acquire Data:<br>
For this assignment, download the Harry Potter Books data from the following link (PDF is also attached):
https://ztcprep.com/library/story/Harry_Potter/Harry_Potter_(www.ztcprep.com).pdf

Extract Data:<br>
Select the book which corresponds to your birth month. For birth month 8-12, divide by 2 and round up.
Once you selected the book, go to page number that corresponds to your birth date (1-31) and extract next 10 pages of the book to a text file (file1.txt).
Next, go to page number that corresponds to your birth year (last 2 digits). For year 2000 onwards, use 1 infront of the year number to find the page number (so year 2000 becomes 100, 2001 - 101 and so on). Extract next 10 pages into another text file (file2.txt).

Write Code to analyze data:<br>
1. Write Python code and use MapReduct to count occurrences of each word in the first text file (file.txt). How many times each word is repeated?
2. From the second text file (file2.txt), write Python code and use MapReduct to count how many times non-English words (names, places, spells etc.) were used. List those words and how many times each was repeated.

