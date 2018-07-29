def find_unmatched_bracecs(inseq):
    seq = list(inseq)
    myseq = []
    remove = []

    for i in range(len(seq)):
        val = seq[i]
        if val == '(':
            myseq.append(i)
        elif val == ')' and not(len(myseq) == 0):
            myseq.pop()
        elif val == ')' and len(myseq) == 0:
            remove.append(i)
    if not(len(myseq) == 0):
        while not(len(myseq) == 0):
            element = myseq.pop()
            remove.append(element)
    k = 0
    for i in reversed(remove):
        seq.pop(i)
        k += 1
    return seq


string = "ab((cd)e)((((((((((((((((((((((((((((((((fg)))))))))))))))))))))))))"
newseq = find_unmatched_bracecs(string)
print ''.join(newseq)