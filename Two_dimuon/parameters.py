# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Wed 23 Mar 2011 22:58:09



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116639,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 174.3,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.18,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 174.3,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.188,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.385,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MN1 = Parameter(name = 'MN1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{MN1}',
                lhablock = 'MASS',
                lhacode = [ 3000001 ])

MN2 = Parameter(name = 'MN2',
                nature = 'external',
                type = 'real',
                value = 10,
                texname = '\\text{MN2}',
                lhablock = 'MASS',
                lhacode = [ 3000002 ])

MZD = Parameter(name = 'MZD',
                nature = 'external',
                type = 'real',
                value = 0.4,
                texname = '\\text{MZD}',
                lhablock = 'MASS',
                lhacode = [ 3000022 ])

MM = Parameter(name = 'MM',
                nature = 'external',
                type = 'real',
                value = 0.105,
                texname = '\\text{MM}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.4611,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.44140351,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.04759951,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value =  1,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WN2 = Parameter(name = 'WN2',
               nature = 'external',
               type = 'real',
               value =  1,
               texname = '\\text{WN2}',
               lhablock = 'DECAY',
               lhacode = [ 3000002 ])

WZD = Parameter(name = 'WZD',
               nature = 'external',
               type = 'real',
               value =  1,
               texname = '\\text{WZD}',
               lhablock = 'DECAY',
               lhacode = [ 3000022 ])

CKM11 = Parameter(name = 'CKM11',
                  nature = 'internal',
                  type = 'complex',
                  value = '0.974',
                  texname = '\\text{CKM11}')

CKM22 = Parameter(name = 'CKM22',
                  nature = 'internal',
                  type = 'complex',
                  value = '0.973',
                  texname = '\\text{CKM22}')

CKM33 = Parameter(name = 'CKM33',
                  nature = 'internal',
                  type = 'complex',
                  value = '0.999',
                  texname = '\\text{CKM33}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')
