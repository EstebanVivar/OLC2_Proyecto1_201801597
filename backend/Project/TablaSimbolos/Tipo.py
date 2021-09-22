from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    DECIMAL = 2
    BOOLEANO = 3
    CHARACTER = 4
    CADENA = 5
    NULO = 6
    ARREGLO = 7

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIV = 4
    MOD = 5
    POT = 6
    NEG = 7
    COMA = 8

class Nativa(Enum):
    LOG10 = 1
    LOG = 2
    SIN = 3
    COS = 4
    TAN = 5
    SQRT = 6
    PARSE = 7
    TRUNC = 8
    FLOAT = 9
    STRING = 10
    TYPEOF = 11
    UPPER = 12
    LOWER = 13


class OperadorRelacional(Enum):
    MENOR = 1
    MAYOR= 2
    MENORIGUAL = 3
    MAYORIGUAL = 4
    COMPARACION = 5
    DIFERENTE = 6

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3