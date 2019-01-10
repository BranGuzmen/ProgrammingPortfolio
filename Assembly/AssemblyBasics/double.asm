.data
	myDouble:	.double	7.202
	zeroDouble: 	.double	0.0
.text
	ldc1	$f2,myDouble	#Load a register from coproc1 with myDouble
	ldc1	$f0, zeroDouble	#Load a register form coproc1 with zeroDouble
	
	li 	$v0, 3		#3 used to print out doubles
	add.d 	$f12,$f2,$f0	#need to add these two so that they can be stored in register $f12
	syscall