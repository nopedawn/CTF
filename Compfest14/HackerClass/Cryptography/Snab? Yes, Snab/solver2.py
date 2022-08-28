from Cryptodome.Util.number import *

p = 1995013714358934674788753256494703046979981946405060402188831027417831621430580449
q = 2351073938238335675017307353569618225242960896099574020278868141802745118893116717
r = 23728

pmr = p-r
qmr = q-r

pwords = long_to_bytes(pmr)
qwords = long_to_bytes(qmr)

out = ""
for i in range(len(pwords)):
    out += chr(pwords[i]) + chr(qwords[i])

print(out)