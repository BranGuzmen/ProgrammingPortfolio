#New method for adding and subtracting 

.data
	num1:	.word	20
	num2:	.word	15
	
.text 
	lw	$s0, num1	#s0 = 20
	lw	$s1, num2	#s1 = 15
	
	sub	$t0, $s0, $s1	#t0 = 20 - 15
	
	li 	$v0, 1		#system preped to print a word
	move	$a0,$t0		#moves the value of t0 to a0
	syscall
