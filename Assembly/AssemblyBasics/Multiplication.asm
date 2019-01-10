#Multiplication demonstration 

.data

.text 
	addi	$s0, $zero, 10	#loads 10 immediately into s0
	addi	$s1, $zero, 4	#loads 4 immediately into s1
	
	mul 	$t0,$s0,$s1	#t0 = s0 * s1
				#mul only lets you multiply two numbers of size 16-bytes	
				
	li 	$v0, 1
	move	$a0, $t0
	syscall
