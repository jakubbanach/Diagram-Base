grammar UML;
options {
	language='Python3';
}

s: (classDiagram | sequenceDiagram | useCaseDiagram) EOF;

// Class diagram
classDiagram:
	'!classdiagram' IDENTIFIER? (
		class
		| interface
		| enum
		| abstractClass
	)+ relationship*;
class: 'class' IDENTIFIER '{' classContents '}';
interface: 'interface' IDENTIFIER '{' classContents '}';
abstractClass: 'abstract' IDENTIFIER '{' classContents '}';
enum: 'enum' IDENTIFIER '{' enumContents '}';
classContents: (field | method)+;
field: scope IDENTIFIER ':' type ';';
scope: '+' | '-' | '#' | '~';
type: (
		'int'
		| 'string'
		| 'double'
		| 'char'
		| 'float'
		| IDENTIFIER
	) ('[' NUMBER_NON_ZERO? ']')?;
method: scope IDENTIFIER '(' arguments ')' ':' type ';';
arguments: argument | argument ',' arguments;
argument: IDENTIFIER ':' type;
enumContents: (enumField)+;
enumField: IDENTIFIER ';';
relationship: IDENTIFIER (objectRelationship | inheritance) ';';
objectRelationship:
	('{' multiplicity '}')? (
		'..'
		| '--'
		| 'o--'
		| '--o'
		| '*--'
		| '--*'
	) IDENTIFIER ('{' multiplicity '}')?;
inheritance: ('<--' | '-->') IDENTIFIER;
multiplicity: NUMBER | ((NUMBER | '*') '..' (NUMBER | '*'));

// Use case diagram
useCaseDiagram: '!usecase' IDENTIFIER? actor* useCaseStatement*;
actor: 'actor' IDENTIFIER ';';
useCaseStatement: package | useCaseDeclaration | dependency;
useCaseDeclaration: 'case' IDENTIFIER STRING ';';
dependency: IDENTIFIER dependencyOperator IDENTIFIER ';';
dependencyOperator: '--' | '-i>' | '<i-' | '-e>' | '<e-';
package: 'package' '{' (useCaseDeclaration | dependency | package)* '}';

// Sequence diagram
sequenceDiagram: '!sequence' IDENTIFIER? lifeline* seqStatement*;
lifeline: 'lifeline' IDENTIFIER ';';
seqStatement: actionsBlock | action;
action: IDENTIFIER actionType IDENTIFIER (':' STRING)? ';';
actionType:
	actionOperator
	| actionOperator 'new'
	| actionOperator 'delete';
actionOperator: '==>' | '<==' | '-->' | '<--' | '-*>' | '<*-';
actionsBlock: alt | opt | par | critical | forLoop | whileLoop;
alt: 'if' condition instruction;
opt: 'if' condition instruction 'else' instruction;
par: 'par' instruction ('and' instruction)*;
critical: 'critical' instruction;
forLoop: 'for' NUMBER instruction;
whileLoop: 'while' condition instruction;
instruction: action | '{' action '}';
condition: (IDENTIFIER | NUMBER) booleanOperator (
		IDENTIFIER
		| NUMBER
	)
	| '!' IDENTIFIER | IDENTIFIER;
booleanOperator: '<' | '>' | '>=' | '<=' | '!=' | '==';

// Lexer
WHITESPACE: [ \n\t\r]+ -> skip;
COMMENT: '//' .* '\n' -> skip;
IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
NUMBER: '0' | ([1-9]+ [0-9]*);
NUMBER_NON_ZERO: [1-9]+ [0-9]*;
STRING: '"' ~["]* '"';
