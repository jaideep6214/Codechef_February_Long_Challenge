# Codechef_February_Long_Challenge

# Question-1:You are given an integer N. Find the largest integer between 1 and 10 (inclusive) which divides N.

Input
The first and only line of the input contains a single integer N.

Output
Print a single line containing one integer ― the largest divisor of N between 1 and 10.

Constraints
2≤N≤1,000
Subtasks
Subtask #1 (100 points): original constraints

Example Input 1
24
Example Output 1
8
Explanation
The divisors of 24 are 1,2,3,4,6,8,12,24, out of which 1,2,3,4,6,8 are in the range [1,10]. Therefore, the answer is max(1,2,3,4,6,8)=8.

Example Input 2
91
Example Output 2
7
Explanation
The divisors of 91 are 1,7,13,91, out of which only 1 and 7 are in the range [1,10]. Therefore, the answer is max(1,7)=7.

# Question-2:You are given a sequence A1,A2,…,AN. Find the maximum value of the expression |Ax−Ay|+|Ay−Az|+|Az−Ax| over all triples of pairwise distinct valid indices (x,y,z).

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing one integer ― the maximum value of |Ax−Ay|+|Ay−Az|+|Az−Ax|.

Constraints
1≤T≤5
3≤N≤105
|Ai|≤109 for each valid i
Subtasks
Subtask #1 (30 points): N≤500
Subtask #2 (70 points): original constraints

Example Input
3
3
2 7 5
3
3 3 3
5
2 2 2 2 5
Example Output
10
0
6
Explanation
Example case 1: The value of the expression is always 10. For example, let x=1, y=2 and z=3, then it is |2−7|+|7−5|+|5−2|=5+2+3=10.

Example case 2: Since all values in the sequence are the same, the value of the expression is always 0.

Example case 3: One optimal solution is x=1, y=2 and z=5, which gives |2−2|+|2−5|+|5−2|=0+3+3=6.

# Question-3: A time is a string in the format "HH:MM AM" or "HH:MM PM" (without quotes), where HH and MM are always two-digit numbers. A day starts at 12:00 AM and ends at 11:59 PM. You may refer here for understanding the 12-hour clock format.

Chef has scheduled a meeting with his friends at a time P. He has N friends (numbered 1 through N); for each valid i, the i-th friend is available from a time Li to a time Ri (both inclusive). For each friend, can you help Chef find out if this friend will be able to attend the meeting? More formally, check if Li≤P≤Ri for each valid i.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single time P.
The second line contains a single integer N.
N lines follow. For each valid i, the i-th of these lines contains two space-separated times Li and Ri.
Output
For each test case, print a single line containing one string with length N. For each valid i, the i-th character of this string should be '1' if i-th friend will be able to attend the meeting or '0' otherwise.

Constraints
1≤T≤500
1≤N≤500
each time is valid in the 12-hour clock format
for each valid i, the time Ri is greater or equal to Li
Subtasks
Subtask #1 (100 points): original constraints

Example Input
2
12:01 AM
4
12:00 AM 11:42 PM
12:01 AM 11:59 AM
12:30 AM 12:00 PM
11:59 AM 11:59 PM
04:12 PM
5
12:00 AM 11:59 PM
01:00 PM 04:12 PM
04:12 PM 04:12 PM
04:12 AM 04:12 AM
12:00 PM 11:59 PM
Example Output
1100
11101
Explanation
Example case 1:

Friend 1: 12:01 AM lies between 12:00 AM and 11:42 PM (that is, between 00:00 and 23:42 in the 24-hour clock format), so this friend will be able to attend the meeting.
Friend 2: 12:01 AM lies between 12:01 AM and 11:59 AM (between 00:01 and 11:59 in the 24-hour clock format).
Friend 3: 12:01 AM does not lie between 12:30 AM and 12:30 PM (between 00:30 and 12:30 in the 24-hour clock format), so this friend will not be able to attend the meeting.
Friend 4: 12:01 AM does not lie between 11:59 AM and 11:59 PM (between 11:59 and 23:59 in the 24-hour clock format).
Example case 2: For friend 3, 04:12 PM lies between 04:12 PM and 04:12 PM (inclusive) and hence this friend will be able to attend the meeting.

# Question-4: There are N frogs (numbered 1 through N) in a line. For each valid i, the i-th frog is initially at the position i, it has weight Wi, and whenever you hit its back, it jumps a distance Li to the right, i.e. its position increases by Li. The weights of the frogs are pairwise distinct.

You can hit the back of each frog any number of times (possibly zero, not necessarily the same for all frogs) in any order. The frogs do not intefere with each other, so there can be any number of frogs at the same time at each position.

Your task is to sort the frogs in the increasing order of weight using the smallest possible number of hits. In other words, after all the hits are performed, then for each pair of frogs (i,j) such that Wi<Wj, the position of the i-th frog should be strictly smaller than the position of the j-th frog. Find the smallest number of hits needed to achieve such a state.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers W1,W2,…,WN.
The third line contains N space-separated integers L1,L2,…,LN.
Output
For each test case, print a single line containing one integer ― the smallest number of times you need to hit the backs of the frogs.

Constraints
1≤T≤2⋅104
2≤N≤4
1≤Wi≤N for each valid i
1≤Li≤5 for each valid i
no two frogs have the same weight
Subtasks
Subtask #1 (50 points):

T=50
N=2
Subtask #2 (50 points): original constraints

Example Input
3
3
3 1 2
1 4 5
3
3 2 1
1 1 1
4
2 1 4 3
4 1 2 4
Example Output
3
6
5
Explanation
Example case 1: We can hit the back of the first frog three times.

Example case 2: We can hit the back of the first frog four times, then hit the back of the second frog two times.

# Question-5:Сhef has assembled a football team! Now he needs to choose a name for his team. There are N words in English that Chef considers funny. These words are s1,s2,…,sN.

Chef thinks that a good team name should consist of two words such that they are not funny, but if we swap the first letters in them, the resulting words are funny. Note that under the given constraints, this means that a word is a non-empty string containing only lowercase English letters.

Can you tell Chef how many good team names there are?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated strings s1,s2,…,sN.
Output
For each test case, print a single line containing one integer — the number of ways to choose a good team name.

Constraints
1≤T≤100
2≤N≤2⋅104
2≤|si|≤20 for each valid i
s1,s2,…,sN contain only lowercase English letters
s1,s2,…,sN are pairwise distinct
the sum of N over all test cases does not exceed 2⋅104
Subtasks
Subtask #1 (20 points): s1,s2,…,sN contain only letters 'a' and 'b'

Subtask #2 (80 points): original constraints

Example Input
3
2
suf mas
3
good game guys
4
hell bell best test
Example Output
2
0
2
Explanation
Example case 1: The good team names are ("muf", "sas") and ("sas", "muf").

Example case 2: There are no good team names because all funny words start with 'g'.

Example case 3: The good team names are ("hest", "tell") and ("tell", "hest").

# Question-6: Chef and Divyam are playing a game with the following rules:

First, an integer X! is written on a board.
Chef and Divyam alternate turns; Chef plays first.
In each move, the current player should choose a positive integer D which is divisible by up to Y distinct primes and does not exceed the integer currently written on the board. Note that 1 is not a prime.
D is then subtracted from the integer on the board, i.e. if the integer written on the board before this move was A, it is erased and replaced by A−D.
When one player writes 0 on the board, the game ends and this player wins.
Given X and Y, determine the winner of the game.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers X and Y.
Output
For each test case, print a single line containing the string "Chef" if Chef wins the game or "Divyam" if Divyam wins (without quotes).

Constraints
1≤T≤106
1≤X,Y≤106
Subtasks
Subtask #1 (5 points): Y=1
Subtask #2 (10 points):

1≤T≤102
1≤X≤6
Subtask #3 (85 points): original constraints

Example Input
3
1 2
3 1
2021 42
Example Output
Chef
Divyam 
Divyam
Explanation
Example case 1: Since D=1 is divisible by 0 primes, Chef will write 0 and win the game in the first move.

Example case 2: Chef must choose D between 1 and 5 inclusive, since D=6 is divisible by more than one prime. Then, Divyam can always choose 6−D, write 0 on the board and win the game.

# Question-7:You are given a sequence of positive integers A1,A2,…,AN. You should answer Q queries. In each query:

You are given a positive integer M.
Consider all non-empty subsequences of A with length ≤M. Recall that a subsequence is any sequence that can be created by deleting zero or more elements without changing the order of the remaining elements.
For each of these subsequences, compute the bitwise XOR of its elements. Your task is to determine the sum of these values. Since this sum can be very large, compute it modulo 998,244,353.
Input
The first line of the input contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains a single integer Q.
Q lines follow. Each of these lines contains a single integer M describing a query.
Output
For each query, print a single line containing one integer ― the sum of bitwise XORs for all subsequences of A with length ≤M, modulo 998,244,353.

Constraints
1≤N,Q≤2⋅105
1≤Ai<230 for each valid i
1≤M≤N
Subtask
Subtask #1 (10 points): 1≤N,Q≤1,000
Subtask #2 (90 points): original constraints

Example Input
4
1 3 5 2
2
1
2
Example Output
11
34
Explanation
In the first query, the answer is just the sum of elements of A (modulo 998,244,353), which is 1+3+5+2=11.

In the second query, the answer is the sum of bitwise XORs for all subsequences with length 1 or 2, which is 1+3+5+2+(1⊕3)+(1⊕5)+(1⊕2)+(3⊕5)+(3⊕2)+(5⊕2)=34
