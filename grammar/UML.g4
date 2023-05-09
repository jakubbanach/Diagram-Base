grammar UML;
options {
	language = 'Python3';
}

program: classDiagram | sequenceDiagram | useCaseDiagram | EOF;

// Class diagram
classDiagram:
	CLASS_START IDENTIFIER? (
		class
		| interface
		| enum
		| abstractClass
	)+ relationship*;
class:
	CLASS IDENTIFIER LEFT_CURLY_BRACKET classContents RIGHT_CURLY_BRACKET;
interface:
	INTERFACE IDENTIFIER LEFT_CURLY_BRACKET classContents RIGHT_CURLY_BRACKET;
abstractClass:
	ABSTRACT IDENTIFIER LEFT_CURLY_BRACKET classContents RIGHT_CURLY_BRACKET;
enum:
	ENUM IDENTIFIER LEFT_CURLY_BRACKET enumContents RIGHT_CURLY_BRACKET;
classContents: (field | method)+;
field: SCOPE IDENTIFIER COLON type LINE_END;
type: IDENTIFIER (LEFT_SQUARE_BRACKET NUMBER_NON_ZERO? RIGHT_SQUARE_BRACKET)?;
method:
	SCOPE IDENTIFIER LEFT_PARENTHESIS arguments? RIGHT_PARENTHESIS COLON type LINE_END;
arguments: argument | argument COMMA arguments;
argument: IDENTIFIER COLON type;
enumContents: (enumField)+;
enumField: IDENTIFIER LINE_END;
relationship:
	IDENTIFIER (objectRelationship | inheritance) LINE_END;
objectRelationship:
	(LEFT_CURLY_BRACKET multiplicity RIGHT_CURLY_BRACKET)? (
		DEPENDENCY
		| ASSOCIATION
		| PARTIAL_AGGREGATION_LEFT
		| PARTIAL_AGGREGATION_RIGHT
		| FULL_AGGREGATION_LEFT
		| FULL_AGGREGATION_RIGHT
	) IDENTIFIER (
		LEFT_CURLY_BRACKET multiplicity RIGHT_CURLY_BRACKET
	)?;
inheritance: (INHERITANCE_LEFT | INHERITANCE_RIGHT) IDENTIFIER;
multiplicity:
	NUMBER
	| ((NUMBER | MANY) MULTIPLICITY_OPERATOR (NUMBER | MANY));

// Use case diagram
useCaseDiagram:
	USE_CASE_START IDENTIFIER? actor* useCaseStatement*;
actor: ACTOR IDENTIFIER LINE_END;
useCaseStatement: package | useCaseDeclaration | dependency;
useCaseDeclaration: CASE IDENTIFIER STRING LINE_END;
dependency: IDENTIFIER dependencyOperator IDENTIFIER LINE_END;
dependencyOperator:
	ASSOCIATION
	| INCLUDE_RIGHT
	| INCLUDE_LEFT
	| EXTEND_RIGHT
	| EXTEND_LEFT;
package:
	PACKAGE LEFT_CURLY_BRACKET (
		useCaseDeclaration
		| dependency
		| package
	)* RIGHT_CURLY_BRACKET;

// Sequence diagram
sequenceDiagram:
	SEQUENCE_START IDENTIFIER? lifeline* seqStatement*;
lifeline: LIFELINE IDENTIFIER LINE_END;
seqStatement: actionsBlock | action;
action:
	IDENTIFIER actionType IDENTIFIER (COLON STRING)? LINE_END;
actionType:
	actionOperator
	| actionOperator NEW
	| actionOperator DELETE;
actionOperator:
	MESSAGE_LEFT
	| MESSAGE_RIGHT
	| ASYNC_MESSAGE_LEFT
	| ASYNC_MESSAGE_RIGHT
	| BACK_MESSAGE_LEFT
	| BACK_MESSAGE_RIGHT;
actionsBlock: alt | opt | par | critical | forLoop | whileLoop;
alt: IF condition instruction ELSE instruction;
opt: IF condition instruction;
par: PAR instruction (AND instruction)*;
critical: CRITICAL instruction;
forLoop: FOR NUMBER instruction;
whileLoop: WHILE condition instruction;
instruction:
	action
	| LEFT_CURLY_BRACKET action RIGHT_CURLY_BRACKET;
condition: (IDENTIFIER | NUMBER) booleanOperator (
		IDENTIFIER
		| NUMBER
	)
	| NOT IDENTIFIER
	| IDENTIFIER;
booleanOperator:
	LESS_THAN
	| GREATER_THAN
	| EQUAL
	| NOT_EQUAL
	| LESS_THAN_OR_EQUAL
	| GREATER_THAN_OR_EQUAL;

// Lexer

CLASS_START: '!classdiagram';
CLASS: 'class';
INTERFACE: 'interface';
ENUM: 'enum';
ABSTRACT: 'abstract';
SCOPE: '+' | '-' | '#' | '~';
DEPENDENCY: '...';
ASSOCIATION: '--';
INHERITANCE_RIGHT: '-->';
INHERITANCE_LEFT: '<--';
PARTIAL_AGGREGATION_RIGHT: '--o';
PARTIAL_AGGREGATION_LEFT: 'o--';
FULL_AGGREGATION_RIGHT: '--*';
FULL_AGGREGATION_LEFT: '*--';
MULTIPLICITY_OPERATOR: '..';
MANY: '*';

USE_CASE_START: '!usecase';
ACTOR: 'actor';
CASE: 'case';
INCLUDE_RIGHT: '-i>';
INCLUDE_LEFT: '<i-';
EXTEND_RIGHT: '-e>';
EXTEND_LEFT: '<e-';
PACKAGE: 'package';

SEQUENCE_START: '!sequence';
LIFELINE: 'lifeline';
NEW: 'new';
DELETE: 'delete';
MESSAGE_RIGHT: '==>';
MESSAGE_LEFT: '<==';
BACK_MESSAGE_RIGHT: '..>';
BACK_MESSAGE_LEFT: '<..';
ASYNC_MESSAGE_RIGHT: '-*>';
ASYNC_MESSAGE_LEFT: '<*-';
IF: 'if';
ELSE: 'else';
PAR: 'par';
AND: 'and';
CRITICAL: 'critical';
FOR: 'for';
WHILE: 'while';
NOT: '!';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
NOT_EQUAL: '!=';
EQUAL: '==';

WHITESPACE: [ \n\t\r]+ -> skip;
COMMENT: '//' .* '\n' -> skip;
IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
NUMBER: '0' | ([1-9]+ [0-9]*);
NUMBER_NON_ZERO: [1-9]+ [0-9]*;
STRING: '"' ~["]* '"';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
LEFT_CURLY_BRACKET: '{';
RIGHT_CURLY_BRACKET: '}';
LEFT_PARENTHESIS: '(';
RIGHT_PARENTHESIS: ')';
COMMA: ',';
LINE_END: ';';
COLON: ':';
