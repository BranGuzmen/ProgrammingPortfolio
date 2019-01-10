#Reading an int as an input

.data
	prompt:	.asciiz	"Enter your age: "
	message: .asciiz "\nYour age is: "
	
.text
	#Prompt user to enter age
	li $v0, 4
	la $a0, prompt
	syscall
	
	#Get users age
	li $v0, 5		#5 means tells the system that an int wants to be recorded
	syscall
	
	#Store the result in t0
	move $t0,$v0		#t0 = user's age
	
	#Display message
	li $v0, 4
	la $a0, message
	syscall
	
	#Print the age
	li $v0, 1
	move $a0,$t0
	syscall
