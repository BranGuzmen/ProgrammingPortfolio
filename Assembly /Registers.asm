#Experimenting with registers

.data 
	newLine:	.asciiz "\n"
.text
	main:
		li $s0, 10		#s0 = 10
		
		jal increaseMyRegister
	#Print a line
	li $v0, 4
	la $a0, newLine
	syscall
		
	#Print value
		li $v0, 1
		move $a0, $s0
		syscall
	
	#End of program
	li $v0, 10
	syscall
	
	
	increaseMyRegister:
		li $sp, -4		#Negative since we want to allocate space in the stack
					#If it was positive we'd be taking space from the stact
		sw $s0, 0($sp)		#Saves the value of s0 to the first spot on the stack
		
		addi $s0, $s0, 30	#s0 = 10 + 30
		
	#Print Value
		li $v0, 1
		move $a0, $s0
		syscall
		
		lw $s0, 0($sp)
		li $sp, 4
		
		jr $ra
