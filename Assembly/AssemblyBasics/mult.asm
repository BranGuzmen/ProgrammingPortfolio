#Multiplication demonstration 

.data

.text
	li	$t0, 2000
	la	$t1, 10
	
	mult	$t0,$t1		#t0 * t1
	
	mflo	$s0		#s0 = t0 * t1
	
	li $v0, 1
	move $a0,$s0
	syscall
	
	
