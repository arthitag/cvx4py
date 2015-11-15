#add more keywords and functions
#support different types of numbers:   exp notation

import ply.lex as lex


class cvxLexer(object):
    def __init__(self):
        print 'initing cvxLexer'

    # List of token names.
    tokens = [
        'INT',
        'FLOAT',
        #arithmetic operators
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        #punctuators
        'LPAREN', 'RPAREN',
        'SEMICOLON', 'COLON', 'DOT', 'SINGLEQUOTE',
        'EQUAL',
        'COMMENT',

        'ID',

        #logical
        'LOGICALEQUAL', 'LESSTHAN', 'GREATERTHAN', 'LESSTHANEQUAL', 'GREATERTHANEQUAL',
    ]

    #edit this to add new keywords. Maybe keep it in a separate file so that later adding to it is more modular
    reserved = {
        #basic keywords
        'cvx_begin' : 'CVX_BEGIN', 'cvx_end' : 'CVX_END', 'variable' : 'VARIABLE', 'dual' : 'DUAL', 'minimize' : 'MINIMIZE', 'maximize' : 'MAXIMIZE', 'subject' : 'SUBJECT', 'to' : 'TO',
        #non linear functions
        'abs' : 'ABS', 'exp': 'EXP', 'log' : 'LOG', 'max' : 'MAX', 'min' : 'MIN', 'norm' : 'NORM', 'polyval' : 'POLYVAL', 'power' : 'POWER', 'std' : 'STD', 'sqrt' : 'SQRT', 'var' : 'VAR',
        #fill more
        #http://cvxr.com/cvx/doc/funcref.html
    }

    tokens = tokens + reserved.values()

    # Regular expression rules for simple tokens
    t_PLUS       = r'\+'; t_MINUS      = r'-'; t_TIMES      = r'\*'; t_DIVIDE      = r'\/'
    t_LPAREN     = r'\('; t_RPAREN     = r'\)';
    t_SEMICOLON  = r'\;'; t_COLON      = r'\:'; t_DOT        = r'\.'; t_SINGLEQUOTE = r'\''
    t_EQUAL  = r'\='
    #t_COMMENT = r'\$'
    #logical operators
    t_LOGICALEQUAL  = r'\==';  t_LESSTHAN = r'\<';  t_GREATERTHAN = r'\>';  t_LESSTHANEQUAL = r'\<=';  t_GREATERTHANEQUAL = r'\>='

    def t_COMMENT(self, t):  #ignore anything after this, till newline  #http://blog.ostermiller.org/find-comment
        r'\%.*'
        return t

    #keep defination of FLOAT above that of INT (precedence)
    def t_FLOAT(t):
        r'(\d*)?[.]\d+'
        t.value = float(t.value)
        return t

    def t_INT(t):
        r'\d+'
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    #Define a rule to get ID and keywords
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'ID')    # Check for reserved words
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)
        t.type = 'ERROR'
        return t


    def buildLex(self):
        # Build the lexer
        self.lexer = lex.lex(module = self)
