%{
#include<stdio.h>
%}

%token NUM
%left '+' '-'
%left '*' '/'

%start line 

%%

line:   
       /* empty */ 
     |line exp '\n' {printf("%d\n",$2);}
     | error '\n';

exp:      exp '+' exp {$$ = $1 + $3;}
        | exp '*' exp {$$ = $1 * $3;}
        | exp '-' exp {$$ = $1 - $3;}
        | exp '/' exp { if ($3 == 0)
                                $$ = 0;
                        else
                                $$ = $1/$3;}
	| '(' exp ')'  { $$ = $2;}
        | NUM          {$$ = $1;};
%%

yyerror()
{
        printf("Error detected in parsing\n");
}

main()
{
        yyparse();
}
