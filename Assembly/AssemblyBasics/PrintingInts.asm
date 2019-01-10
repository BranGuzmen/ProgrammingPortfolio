.data
	age:	.word	21	#word stores a 32-byte value
.text 
	li 	$v0, 1		#1 is used to print out word values
	lw	$a0, age
	syscall