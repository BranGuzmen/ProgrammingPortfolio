.data
myMessage: .asciiz 	"Hello World\n"		#myMessage stores message Hello World
.text
	li $v0, 4		#4 is used to print to screen
	la $a0, myMessage
	syscall
	