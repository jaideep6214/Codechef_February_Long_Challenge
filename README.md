# Codechef_February_Long_Challenge
Question-1:You are given an integer N. Find the largest integer between 1 and 10 (inclusive) which divides N.

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

Question-2:You are given a sequence A1,A2,…,AN. Find the maximum value of the expression |Ax−Ay|+|Ay−Az|+|Az−Ax| over all triples of pairwise distinct valid indices (x,y,z).

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
