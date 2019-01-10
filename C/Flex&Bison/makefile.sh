CC=gcc
CFLAGS=-c -Wall
SOURCES=$(wildcard *.c)
EXECUTABLE=$(SOURCES:.c=)

all: $(EXECUTABLE)

lex.yy.o: lex.yy.c
	$(CC) lex.yy.c -o lex.yy.o

calc.tab.o: calc.tab.c
	$(CC) calc.tab.c -o calc.tab.o

calc: calc.c
	$(CC) calc.c -o calc

clean:
	rm -f lex.yy.o calc.tab.o calc
	echo Finished Cleaning