#Simple addition demonstration 


.data 
	number1:	.word	5
	number2:	.word	-2
.text
	lw	$t0, number1($zero)	#load number1 to register 1
	li	$t1, -2
	
	mul 	$t0,$t0,$t1
	sub	$t1,$t1,$t0		#adding number1 and number2
	
	li	$v0, 1			#preping system to print int
	move	$a0, $t1		#load $t2 into $a0
	syscall				#move is sugar for printing out .word
