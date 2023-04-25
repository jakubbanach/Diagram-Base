grammar UML;
options{
    language = Python3;
}

//Diagram klasy

DiagramUML: (DiagramKlas|DiagramSekwencji|DiagramUseCase);
DiagramKlas: '!classdiagram' (Klasa|Interface|Enum|Abstract)+ Związek*;

Klasa: 'class' Nazwa '{' Inside '}';
Interface: 'interface' Nazwa '{' Inside '}';
Enum: 'enum' Nazwa '{' InsideEnum '}';
Abstract: 'abstract' Nazwa '{' Inside '}' ;

Nazwa: [a-Z]+[a-Z0-9]*;
Inside: (Pole|Metoda)*;
Pole: Zasięg Nazwa ':' Typ ';';
Zasięg: '+'|'-'|'#'|'~';
Typ: 'int'|'string'|'double'|'char'|'float' ('[' ([1-9]+[0-9]*)? ']')?; //.....
Metoda: Zasięg Nazwa '(' Argumenty ')' ':' Typ ';';
Argumenty: Nazwa ':' Typ;

InsideEnum: PoleEnum*;
PoleEnum: Nazwa ';';

Związek: Nazwa ZKrotnością|Dziedziczenie';';
ZKrotnością: '{' Krotność '}' '..'|'--'|'o--'|'--o'|'*--'|'--*' Nazwa '{' Krotność '}';
Dziedziczenie: '<--'|'-->' Nazwa;
Krotność: Liczba|(Liczba|'*' '..' Liczba|'*');
Liczba: '0'|([1-9]+[0-9]*);
//SPRAWDZIĆ


// Początek: '!';
// DiagramKlas:;
DiagramUseCase:;
DiagramSekwencji:;

// Zależność: '..';
// Asocjacja: '--';
// Agregacja_częściowaL: 'o--';
// Agregacja_częściowaP: '--o';
// Agregacja_całkowitaL: '*--';
// Agregacja_całkowitaP: '--*';
// DziedziczenieL: '<--';
// DziedziczenieP: '-->';
// KlamraL: '{';
// KlamraP: '}';
// FunkcjaL: '(';
// FunkcjaP: ')';
// EndOfLine: ';';
// PrzedTypem: ':';
// Klasa_asocjacyjna
// Klasa_abstrakcyjna
// Uogólnienie_Dziedziczenie
// Komentarz
// Typ (string, int, ….)
// Nazwa klasy
// Funkcja → ‘()’
// Zwracanie → ‘:’

//
// Publiczna: '+';
// Prywatna: '-';
// Chroniona: '#';
// Zakres_pakietu: '~';

//Krotnosci
// Krotność: '..';

// Aktor
// Linia życia (inna niż aktor)
// Wywołanie procedury
// Powrót
// Wywołanie asynchroniczne
// Tworzenie uczestnika
// Usuwanie uczestnik
// **alt** (od *alternative* ) określający warunek wykonania bloku operacji, odpowiadający instrukcji *if-else* ; warunek umieszcza się wówczas wewnątrz bloku w nawiasach kwadratowych
// **opt** (od *optional* ) reprezentujący instrukcję  *if* (bez  *else* )
// **par** (od  *parallel* ) nakazujący wykonać operacje równolegle
// **loop** definiujący pętlę typu *for* (o określonej z góry liczbie iteracji) lub *while* (wykonywanej dopóki pewien warunek jest prawdziwy)
// **break** wykonanie fragmentu i zakończenie interakcji
// **seq** słaba sekwencja (podobnie do współbieżności) dotyczy zdarzeń z kilku linii

// **Przypadek użycia**
// **Aktor**
// **Interakcja**
// **Include**
// **Extend**
// **Dziedziczenie**

// Typ diagramu
// Początek diagramu
// Koniec diagramu
// Tekst