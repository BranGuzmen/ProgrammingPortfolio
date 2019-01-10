#Simple program to demonstrate handling arguments and returning values

.data
	message: 	.asciiz "Hello, World!\nMy name is Bryan.\n"
	
.text
	main:
		li $a1, 50		#a1 = 50
		li $a2, 100		#a2 = 100
		
		jal addNumbers
		
		li $v0, 1
		move $a0, $v1
		syscall
		
	li $v0, 10
	syscall
	
	addNumbers:
		add $v1, $a1, $a2
		
		jr $ra
