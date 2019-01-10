#Bryan Guzman
#Unix ID: bg615349@itsunix.albany.edu
#Discussion: Wednesday @ 9:20
#Program to count the number of inputs, max integer, the highest number of 1's in binary 
#and the numbers with the most 1's in binary

.data
	input: 		.byte 	0:80			#Byte array with 80 indexes to store the input
	integers:	.word	0:40			#Integer array will save the values from input
	tempInt:	.word	0:40
	promptIn:	.asciiz	"Enter the line?"	#Prompt for line of char
	promptInt:	.asciiz	"No. of integers: "	#Used for printing out the number of ints in array
	promptMaxInt:	.asciiz	"Maximum integer: "	#Used for printing out the greatest int in array
	promptMaxOne:	.asciiz	"Maximum number of 1's in the binary representation: "		#Used for printing out the max number of 1's
	promptMaxOneInt:.asciiz	"Integers of maximum number of 1's in the binary representation: "	#Used for printing out the number/s with the greatest amount of 1's		
	newLine:	.asciiz	"\n"			#Used for formatting
	isEmptyMsg:	.asciiz	"Empty Line"
	cstack:		.byte	0:20
	imOut:		.asciiz	"I'm Out of the Loop"
	char:		.space	10000000
.text
.globl main

	main:	
	#Prompt user to input a line of ints
	li 	$v0, 4
	la 	$a0, promptIn	
	syscall
	
	#Read the line of integers
	li 	$v0, 8
	la 	$a0, input
	li 	$a1, 80
	syscall
	
	la	$s0, input				#input = s0
	la	$s1, integers				#integers = s1
	
	
	jal 	whiteSpace				#Goto whiteSpace function
	jal 	makeInts				#Goto makeInts function
	jal 	numberOfInts				#Goto numberOfInts function
	jal 	maxInt					#Goto maxInt function
	jal 	maxOnes					#Goto maxOnes function
	
	
	#li	$t1, 0
	#print_integer:
	#lw	$t0, integers($t1)
	#beq	$t0,-1,exit_print
	
	#jal 	new_Line
	
	#li 	$v0, 1
	#move 	$a0, $t0
	#syscall
	#addi	$t1,$t1,4
	#j	print_integer
	
	#exit_print:
	j end
	
	
	
	
	
	
	
	
################################################################################################################################################	
	#Checks to make sure array is not just whitespace characters
whiteSpace:
	lbu 	$t3, ($s0)		#t3 is stored into input array
	while:

	beq 	$t3, $zero, endWhiteSpace	#Ends white space method
	#li $v0, 11
	#la $a0, ($s0)
	#syscall
	beq	$t3, 0x0A,isEmpty	#if t0 is a newLine char
	bgt 	$t3, 20,endWhiteSpace	#if t0 is a null character
	beq	$t3, 0x09,isEmpty	#if t0 is a tab
	beq	$t3, 0x0B,isEmpty	#if t0 is a tab
	
	blt	$t3, 0x30,whiteSpace	#if t0 is less that 0
	bgt	$t3, 0x39,whiteSpace 	#if t0 is greater than 9
	
	addi	$t3,$t3,1		#increment to the next index
	
	j while
	
	#Prints out "Empty line" when nothing is entered
	isEmpty:
	li $v0, 4
	la $a0, isEmptyMsg
	syscall
	j end
	
	#Exits whitespace function to return to main
	endWhiteSpace:
	jr	$ra
#################################################################################################################################################	
	#Constructs the ints and saves them to the integer array
makeInts:
	la 	$t1, integers			#t1 is the base address of integer array
	la 	$t2, input			#t2 is the base address of input array
	la 	$s0, cstack			#Load cstack address
	la 	$s1, ($ra)			#save the return address to main
	add 	$t0, $zero,$zero		#set t0 to zero
	add	$t9,$zero,$zero			#set t9 to zero to act as an index tracker
	addi	$s2,$s2, 0			#used to increment integer array
	li	$s5, 48				#Set to 48 or '0'
	li	$s6, 57				#set to 57 or '9'
	
	sub2:
	lbu  	$t0, input($t9)			#Load the byte into t0
	beqz	$t0,lastIndex			#if t0 is null go to loop 3
	blt	$t0,$s5,increment		#If byte is less than 0 go to sub2
	bgt	$t0,$s6,increment		#If byte is greater than 9 go to sub2
	addi	$t3, $zero,0			#Set counter to 0
	
	
	loop1:
	beq	$t0,$zero,exit			#If at the end of input array, go to loop 2
	sub	$a1,$t0,48			#48 is the ASCII for '0', subtracting to get actual value and save into a1
	addi	$t3,$t3,1			#Increment counter by 1
	jal	push				#Push a1 onto stack 
	addi	$t9,$t9,1			#increment to next byte
	lbu	$t0,input($t9)			#Load the next byte
	#Used to determine if t0 is a digit
	blt	$t0,$s5,exit			#Branch to sub 2 if < 0
	bgt	$t0,$s6,exit			#Branch to sub3 if > 9
	j	loop1
	
	exit:
	addi	$t4, $zero, 0			#t4 = sum = 0
	addi	$t5, $zero, 1			#t5 = P = 1
	addi	$t6, $zero, 10			#t6 = R = 10
	
	loop2:
	beq	$t3,$zero, saveSum		#if counter is zero go to save sum
	sub	$t3,$t3,1			#t3 = t3 - 1 || t3--
	jal 	pop				#Get digit from stack
	mul	$t7, $v1, $t5			#t7 = D, D * P, D is the popped digit from stack
	add	$t4,$t4,$t7			#Sum = sum + (D * P)
	mul	$t5,$t5,$t6			#P = P * R
	j	loop2
	
	saveSum:#need to increment array
	sw	$t4,integers($s2)		#Save int into integer array
	addi	$s2,$s2,4			#increment to next index integers array
	j	sub2
	
	increment:
	addi	$t9,$t9,1			#increment to next byte on input array
	j	sub2				#Go back to sub2
	
	lastIndex:
	li	$t8,-1				#Used for sentinal value
	#addi	$s2,$s2,4			#increment one more index
	sw	$t8,integers($s2)		#Store -1 in the last index
	jr	$s1				#Return to main
	
	#Used to put a digit in the stack
	push:
	sb	$a1, ($s0)			#Stores a1 digit onto stack
	addi	$s0,$s0,1			#Increment stack pointer by 1
	jr	$ra
	#Used to grab a digit from the stack
	pop:
	addi	$s0,$s0,-1
	lb	$v1, ($s0)			#Pop digit off of stack and save in v1
	jr	$ra
#################################################################################################################################################	
	#Counts the number of ints in the array
numberOfInts:
	lw	$t0,integers			#Load the address of the array into t0
	li	$t2,0				#Set t2 to zero to be used as counter
	la	$t4, ($ra)			#Save return address for later
	li 	$t1, 0				#used to increment the array
	
	numLoop:				#Loop to go through array and count ints
	lw	$t0,integers($t1)		#set t0 to next int		
	beq	$t0,-1,exit_numLoop
	addi	$t2,$t2,1			#increment counter by 1
	addi	$t1,$t1,4			#increment to next int in array	
	j	numLoop
	
	exit_numLoop:
	jal new_Line				#print out a new line
	li $v0,4				#prep system to print a string
	la $a0, promptInt			#Print out the message "No. of Ints"
	syscall
	
	li $v0,1				#prep system to print out a word
	move $a0,$t2				#move counter into a0
	syscall					#print out the counter
	
	jr	$t4				#Jump back to main method	
	
#################################################################################################################################################	
	#Finds the largest int in the array
maxInt:
	la	$t0, integers			#load address of integers to t0
	la	$t4, ($ra)			#save return address for later
	li	$t1,0				#set t1 to zero, will be used for maxInt
	li	$t2,0				#Will be used as a temp value
	li	$t3,0				#Will be used to increment through the integer array
	
	max_Loop:				#loop to go through the integers array and find max int
	lw	$t0,integers($t3)		#Load the first integer into t0
	beq	$t0,-1,exit_maxLoop		#When sentinal value is found, exit the loop
	bgt	$t0,$t1,setMax			#branch if the integer is greater than maxInt
	addi	$t3,$t3,4			#increment to next integer
	jal	max_Loop			#Jump back to the max_Loop
	
	setMax:					#Sets t1 to the max integer in the array
	move	$t1, $t0			#moves the integer stored in t0 to t1
	j	max_Loop				#Goes back to max_Loop
	
	exit_maxLoop:				#Used to print out final answer and return to main
	jal	new_Line			#print out a new line
	
	li 	$v0,4				#prep system to print out a string
	la 	$a0,promptMaxInt			#move message to a0
	syscall					#print out promptMaxInt message
	
	li 	$v0,1				#prep system to print out an int
	move 	$a0,$t1				#move sum to a0 
	syscall					#print out the sum
	jr	$t4
	
###################################################################################################################################	
	#Finds the integer with the maximum number of ones
maxOnes:
	la 	$t4,($ra)			#save the address to return to main
	li	$t1, 0				#will be used to index through integer array
	li	$t2, 0				#will be used to hold the number of 1's in integer
	li	$t3, 0				#will be used as a max comparison
	li	$t5, 2				#will be used as divisor
	li	$t6, 0				#will be used to hold remainder
	li	$t7,0				#will be used to increment through array storing integer values for printing
	li	$s7,0				#will be used to increment through array storing integer values for printing
	li 	$a1, 0				#used as a temp register to manipulate the integer in the array
	
	loop_maxOnes:
	lw	$t0,integers($t1)		#Load the next integer into t0
	li	$t2,0				#reset counter to zero at the beginning of loop
	beq	$t0,-1,print_numMaxOnes		#Exit the loop at the end of array
	move	$a1,$t0				#use a1 as a temp register
	jal	divOnes				#start dividing the integer here
	return1:
	beq	$t2,$t3,numMaxOnes		#if another number with the same amount of ones is in the array
	bgt 	$t2,$t3,numMaxOnes		#check to see which number has the maximum number of ones
	return2:
	addi	$t1,$t1,4			#increment to next integer
	j	loop_maxOnes			#go back to loop_maxOnes
	
	divOnes:				#Will divide a0 by 2 and check if remainder is equal to 1
	rem	$t6,$a1,$t5			#integer/2 and t6 = remainder
	mflo	$a1				#s4 = quotient
	blt 	$a1,1,countMaxOnes_Done		#finished counting the 1's in integer
	beq	$t6,1,count_maxOnes		#if the remainder is equal to 1, goto count max ones
	bgt	$a1,-1,divOnes			#If integer is greater than 0, repeat division 
	
	count_maxOnes:
	#la	$s0,($ra)				
	addi	$t2,$t2,1			#will count the number of ones in an integer
	j	divOnes				#jump back to after line 248
	
	countMaxOnes_Done:
	#la	$s0,($ra)			#Back to Main?
	addi	$t2,$t2,1
	move	$s7, $t2
	j	return1				#Back to main?
	
	numMaxOnes:				#Will check which number has the maximum amount of ones
	#la	$s0,($ra)			#save the return address to return to right spot in code
	move	$t3,$t2				#max number of ones stored in t3
	jal	storeInt			#Jump to method save the integer for printing
	j	return2				#Go back to loop_maxOnes
	
	storeInt:				#will put the current integer into an array for printing out 
	sw	$t0,tempInt($t7)		#store int into tempInt
	addi	$t7,$t7,4			#increment to next byte
	jr	$ra				#return to numMaxOnes
	
	
	print_numMaxOnes:
	jal	new_Line			#Print out a new line
	
	li	$v0,4				#Prep system to print string
	la	$a0, promptMaxOne		#Print out promptMaxOne message
	syscall
	
	li	$v0,1				#Prep system to print a word
	move	$a0,$t3				#move max number of ones count into a0
	syscall					#print out the value
	
	jal 	new_Line			#print out a new line
	
	li	$v0,4				#prep system to print out a string
	la	$a0, promptMaxOneInt		#print out promptMaxOneInt message
	syscall
	
	move	$s1,$t7
	li	$t7,0				#set the incrementor back to 0
		
	loop_tempInt:
	lw	$t8,tempInt($t7)
	beq	$t7,$s1,exit_loopTempInt
	
	li	$v0,1				#prep system to print a word
	move	$a0,$t8				#move integer stored in t8 to a0
	syscall					#print out integer
	
	addi	$t7,$t7,4			#increment to next integer
	jal	new_Line			#Print a new line
	j	loop_tempInt			#go back to loop_tempInt
	
	exit_loopTempInt:
	jr	$t4				#go back to main
	
###################################################################################################################################
	#Will print out a new line
	new_Line:
	li $v0, 4
	la $a0, newLine
	syscall
	jr $ra
	
##################################################################################	
	#Used to end the program
	end:
	li $v0, 10
	syscall
	
