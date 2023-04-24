grammar Diagrams;
options {
	language = Python3;
}
r: 'hello' ID;
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;