# Perulangan adalah sebuah bagian kode selama kondisinya masih memenuhi dan akan berhenti jika kondisinya sudah tidak memenuhi lagi.

index = 1

while index <= 5:
    print("*" * index)
    index += 1

print("Finish")



# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern triangle
def triangle(n):
     
    # number of spaces
    k = n - 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
triangle(n)

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern of numbers
def numpat(n):
     
    # initialising starting number
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # re assigning num
        num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver code
n = 5
numpat(n)

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

n = 5

# sending 5 as argument
# calling Function
contnum(n)


# Python 3.x code to demonstrate star pattern

# # Function to demonstrate printing pattern of alphabets
# def alphapat(n):
	
# 	# initializing value corresponding to 'A'
# 	# ASCII value
# 	num = 65

# 	# outer loop to handle number of rows
# 	# 5 in this case
# 	for i in range(0, n):
	
# 		# inner loop to handle number of columns
# 		# values changing acc. to outer loop
# 		for j in range(0, i+1):
		
# 			# explicitly converting to char
# 			ch = chr(num)
		
# 			# printing char value
# 			print(ch, end=" ")
	
# 		# incrementing number
# 		num = num + 1
	
# 		# ending line after each row
# 		print("\r")

# # Driver Code
# n = 5
# alphapat(n)


