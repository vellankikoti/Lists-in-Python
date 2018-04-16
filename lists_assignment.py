
# 1. Write a Python function called compare date that takes as arguments two lists of two integers each. Each list contains a month and a year, in that order. The function should return -1 if the first month and year are earlier than the second month and year, 0 if they are the same, and 1 if the first month and year are later than the second. Your code should work for any legal input for month and year. Example calls and expected output are shown below:
# >>> compare_date( [10,1995], [8,1995] )
# 1
# >>> compare_date( [5,2010], [5,2010] )
# 0
# >>> compare_date( [10,1993], [8,1998] )
# -1

l1 = [10,1995]
l2 = [8,1995]
def func(l1,l2):
	if l1[0] > l2[0]:
		print(1)
	elif l1[0] < l2[0]:
		print(-1)
	else:
		print(0)
l1 = [8,1995]
l2 = [10,1995]
print(func(l1,l2))

# output: 1

# 2. Assume v is a list containing numbers. Write Python code to find and print the highest two values in v.
# If the list contains only one number, print only that number. If the list is empty, print nothing.
# For example, if we assigned v = [ 7, 3, 1, 5, 10, 6 ]
# then the output of your code should be something like 7 10
# If we are given that v = [ 7 ] then the output of your code should be 7

def max_smax(list):
	max = 0
	smax =0
	for val in list:
		if val > max:
			max,smax =  val,max
		elif val < max and val > smax:
			smax = val
		else:
			continue
	return max,smax

v = [7,3,1,5,10,6]
print("Maximum and second maximum numbers are:",max_smax(v))

# 3. Consider a data, where just the name of the restaurant, the type of restaurant, and the ratings are provided. Assume these values have already been read into a list of lists of the form below:
# restaurants = [ [ Acme, Italian, 2, 4, 3, 5],[ Flintstone, Steak, 5, 2, 4, 3, 3, 4],[ Bella Troy, Italian, 1, 4, 5] ]
# Write a segment of Python code that prints all Italian restaurants in the restaurants list that have no ratingsof value 1 and at least one rating of value 5.
# In the above example, Acme would be printed in the output, but Flintstone and Bella Troy would not. Flintstone is not Italian and Bella Troy has a 1 rating. 

restaurants = [["Acme","Italian",2,4,3,5],["Flintstone","Steak",5,2,4,3,3,4],["Bella Troy","Italian",1,4,5]]
for value in restaurants:
		if value[1] == "Italian" and 1 not in value and 5 in value:
			print(value[0])

"""4. In the game of chess you can often estimate how well you are doing by adding the values of the pieces you have captured.
 The pieces are Pawns, Bishops, Knights, Rooks and Queens. Their values are
P - (P)awn, value = 1
B - (B)ishop, value = 3
K - (K)night, value = 3
R - (R)ook, value = 5
Q - (Q)ueen, value = 9
Write a Python function called chess_score that takes a single string as an argument and returns the
combined  values represented by the pieces in the string. You may assume that only P, B, K, R and Q appear in the string. 
You may not use any if statements and you may not use any loops. As an example,
print chess_score(BQBP)
should output the value 16 because there are 2 Bishops (3 points each), 1 Queen (9 points each), and 1 Pawn (1 point each).
"""

d = {"P":1,"B":3,"K":3,"R":5,"Q":9}
s = "BQBP"
s2 = d["B"]+d["Q"]+d["B"]+d["P"]
print("chess_score for BQBP:",s2)

"""5. You are given a file that contains, on each line of input, three integers separated by commas.
Write a Python program that sums all of the first integers, the second integers, and the third integers,
outputting the resulting sums all on one line, separated by commas. As a simple example, if the input is 
2, 5,7 
3, 6, 10
1, 2, -3
2, 4, 1
Then the output should be
8, 17, 15"""

def list_add(*args):
	l = []
	for index in range(len(args[0])):
		sum = 0
		for val in args:
			sum = sum + val[index]
		l.append(sum)
	return l
l1 = [2,5,7]
l2 = [3,6,10]
l3 = [1,2,-3]
l4 = [2,4,1]

l = list_add(l1,l2,l3,l4)
print("Sum of the lists is:",l)

