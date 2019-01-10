#Functions in assembly 

.data
	message:	.asciiz	"Hello to the world. \nMy name is Bryan.\n"
.text
	main:
		jal displayMessage	#Jumps to displayMessage Function
		jal addition
	
	#Tells the system that the program is over
	li $v0, 10
	syscall		
	#Function
	displayMessage:
	li $v0, 4
	la $a0, message
	syscall
	
	jr $ra				#This will make sure the program returns to the main function 
	
	addition:
	li 	$t0, 10
	li	$t1, 20
	add	$s0, $t0,$t1		#s0 = t0 + t1 || s0 = 10 + 20
	
	li $v0, 1
	move $a0, $s0
	syscall
	
	jr $ra
	
