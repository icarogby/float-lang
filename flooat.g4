grammar flooat;

init: comp;

comp: 'comp' ID '(' parameters ')' '(' parameters ')' '{' descriptionBlock '}';

parameters: (signDec (',' signDec)*)?; // List of signal declarations
descriptionBlock: ((signDec|signAssign|singDecAssign) ';')*;

signDec: 'bit' ('[' Number ']')? ID;
signAssign: ID ('[' Number ']')? '=' (ID ('[' Number ']')?|Bit|BitVec) (Op (ID ('[' Number ']')?|Bit|BitVec))*;
singDecAssign: 'bit' ('[' Number ']')? signAssign;

Op: 'and'|'or'|'not'|'xor';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
Number: [0-9]+;
Bit: '0'|'1';
BitVec: Bit Bit+;

WS: [ \t\r\n]+ -> skip;
