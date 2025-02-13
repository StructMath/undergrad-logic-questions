from os import listdir
import re

Qs = listdir("question")
Q = [int(q[:-4]) for q in Qs]
Q.sort()
Qdict = dict(zip(Q, [None]*len(Q)))
C = []

for fp in Q:
    f = open("question/" + str(fp) + ".tex").read()
    comment = None
    ap = False

    if not "\\begin{ans}" in f:
        ap = True
        comment = " No Answer"
    
    cl = re.search(r"%ANS(.*?)($|\n)", f)
    if cl != None:
        ap = True
        comment = cl.group(1)
    
    Qdict[fp] = comment


readme = "Unanswered questions:<br /><br />"

for qn in Q:
    if Qdict[qn] != None:
        readme += str(qn) + Qdict[qn] + "<br />"

readme += "<br />"

H = listdir("homework")
H.sort()

for fp in H:
    f = open("homework/" + fp).readlines()

    QsInH = [int(qn) for qn in f[2].split(',')[:-1]]
    uq = False
    comment = fp + ":<br />"
    
    for qn in QsInH:
        if Qdict[qn] != None:
            uq = True
            comment += str(qn) + Qdict[qn] + "<br />"

    if not uq:
        comment += "Congrats! No unanswered questions.<br />"
    
    readme += comment + "<br />"

Z = listdir("quiz")
Z.sort()

for fp in Z:
    f = open("quiz/" + fp).readlines()

    QsInZ = [int(qn) for qn in f[2].split(',')[:-1]]
    uq = False
    comment = fp + ":<br />"
    
    for qn in QsInZ:
        if Qdict[qn] != None:
            uq = True
            comment += str(qn) + Qdict[qn] + "<br />"

    if not uq:
        comment += "Congrats! No unanswered questions.<br />"
    
    readme += comment + "<br />"

RM = open("README.md", "w")
RM.write(readme)
RM.close()