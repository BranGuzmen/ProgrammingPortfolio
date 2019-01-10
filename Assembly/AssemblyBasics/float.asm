.data
	PI:	.float	3.14
.text
	li	$v0, 2		#2 prints out floats
	lwc1	$f12,PI		#Loads PI into register f12, found in coproc 1 
	syscall