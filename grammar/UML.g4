grammar UML;
options {
	language = Python3;
}

s: classDiagram | sequenceDiagram | useCaseDiagram;

// Class diagram
classDiagram:
	'!classdiagram' IDENTIFIER (
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
		| 'STRING'
		| 'double'
		| 'char'
		| 'float'
		| IDENTIFIER
	) ('[' NUMBER_NON_ZERO? ']')?;
method: scope IDENTIFIER '(' arguments ')' ':' type ';';
arguments: argument | argument ',' arguments;
argument: IDENTIFIER ':' type;
enumContents: enumField+ ';';
enumField: IDENTIFIER ';';
relationship: IDENTIFIER (objectRelationship | inheritance) ';';
objectRelationship:
	'{' multiplicity '}' (
		'..'
		| '--'
		| 'o--'
		| '--o'
		| '*--'
		| '--*'
	) IDENTIFIER '{' multiplicity '}';
inheritance: ('<--' | '-->') IDENTIFIER;
multiplicity: NUMBER | ((NUMBER | '*') '..' (NUMBER | '*'));

// Use case diagram
useCaseDiagram: '!usecase' IDENTIFIER actor* useCaseStatement*;
actor: 'actor' IDENTIFIER ';';
useCaseStatement: useCaseDeclaration | dependency | package;
useCaseDeclaration: 'case' IDENTIFIER STRING ';';
dependency: IDENTIFIER dependencyOperator IDENTIFIER ';';
dependencyOperator: '--' | '-i>' | '<i-' | '-e>' | '<e-';
package: '{' (useCaseDeclaration | dependency | package) '}';

// Sequence diagram
sequenceDiagram: '!sequence' IDENTIFIER lifeline* seqStatement*;
lifeline: 'lifeline' IDENTIFIER ';';
seqStatement: actionsBlock | action;
action: IDENTIFIER actionType IDENTIFIER ':' STRING ';';
actionType:
	actionOperator
	| actionOperator 'new'
	| actionOperator 'delete';
actionOperator: '==>' | '<==' | '-->' | '<--' | '-*>' | '<*-';
actionsBlock: alt | opt | par | critical | forLoop | whileLoop;
alt: 'if' instruction;
opt: 'if' instruction 'else' instruction;
par: 'par' instruction;
critical: 'critical' instruction;
forLoop: 'for' NUMBER instruction;
whileLoop: 'while' condition instruction;
instruction: action | '{' action '}';
condition: (IDENTIFIER | NUMBER) booleanOperator (
		IDENTIFIER
		| NUMBER
	)
	| '!' IDENTIFIER;
booleanOperator: '<' | '>' | '>=' | '<=' | '!=' | '==';

// Lexer
WHITESPACE: [ \n\t\r]+ -> skip;
COMMENT: '#' .* -> skip;
IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
NUMBER: '0' | ([1-9]+ [0-9]*);
NUMBER_NON_ZERO: [1-9]+ [0-9]*;
STRING: '"' [^"]* '"';

// Początek: '!'; Zależność: '..'; Asocjacja: '--'; Agregacja_częściowaL: 'o--';
// Agregacja_częściowaP: '--o'; Agregacja_całkowitaL: '*--'; Agregacja_całkowitaP: '--*';
// DziedziczenieL: '<--'; DziedziczenieP: '-->'; KlamraL: '{'; KlamraP: '}'; FunkcjaL: '(';
// FunkcjaP: ')'; EndOfLine: ';'; PrzedTypem: ':'; Klasa_asocjacyjna Klasa_abstrakcyjna
// Uogólnienie_Dziedziczenie Komentarz Typ (STRING, int, ….) Nazwa klasy Funkcja → ‘()’ Zwracanie →
// ‘:’

//
// Publiczna: '+'; Prywatna: '-'; Chroniona: '#'; Zakres_pakietu: '~';

//Krotnosci
// Krotność: '..';

// Aktor Linia życia (inna niż aktor) Wywołanie procedury Powrót Wywołanie asynchroniczne Tworzenie
// uczestnika Usuwanie uczestnik **alt** (od *alternative* ) określający warunek wykonania bloku
// operacji, odpowiadający instrukcji *if-else* ; warunek umieszcza się wówczas wewnątrz bloku w
// nawiasach kwadratowych **opt** (od *optional* ) reprezentujący instrukcję *if* (bez *else* )
// **par** (od *parallel* ) nakazujący wykonać operacje równolegle **loop** definiujący pętlę typu
// *for* (o określonej z góry liczbie iteracji) lub *while* (wykonywanej dopóki pewien warunek jest
// prawdziwy) **break** wykonanie fragmentu i zakończenie interakcji **seq** słaba sekwencja
// (podobnie do współbieżności) dotyczy zdarzeń z kilku linii

// **Przypadek użycia** **Aktor** **Interakcja** **Include** **Extend** **Dziedziczenie**

// Typ diagramu Początek diagramu Koniec diagramu Tekst