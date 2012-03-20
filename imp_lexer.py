import lexer

RESERVED = 'RESERVED'
INT      = 'INT'
COMMENT  = 'COMMENT'
BOOLEAN  = 'BOOLEAN'
ID       = 'ID'

token_exprs = [
	(r';.+',                     COMMENT),
	(r'[ \n\t]+',                None),
	(r'#[^\n]*',                 None),
	(r'\FORWARD',                RESERVED),
	(r'\LEFT',                   RESERVED),
	(r'\RIGHT',                  RESERVED),
	(r'\FD',                     RESERVED),
	(r'\LT',                     RESERVED),
	(r'\RT',                     RESERVED),
	(r'\PRINT',                  RESERVED),
	(r'\PENUP',                  BOOLEAN),
	(r'\PENDOWN',                BOOLEAN),
	(r'[0-9]+',                  INT),
	(r'[A-Za-z][A-Za-z0-9_]*',   ID),
]

def imp_lex(characters):
	return lexer.lex(characters, token_exprs)
