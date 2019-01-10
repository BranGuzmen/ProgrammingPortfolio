#Demonstration of division 

.data

.text
	li	$t0, 30		#t0 = 30
	li	$t1, 5		#t1 = 5
	li 	$t2, 25		#t2 = 25
	li	$t3, 5		#t3 = 5
	li 	$t4, " "	#t4 holds a space
	
	div $s0, $t0, $t1	#s0 = t0/t1 || s0 = 30/5
	
	div $t2,$t3		#t2/t3 || 25/5
	
	mflo $s1 		#Quotient
	mfhi $s2		#Remainder
	
	li $v0, 1
	move $a0,$s0
	syscall
	
	li $v0, 4
	move $a0, $t4
	syscall
	
	#No idea how to insert a space inbetween 6 and 5
	li $v0, 1
	move $a0, $s1
	syscall
	
	
