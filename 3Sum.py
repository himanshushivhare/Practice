
def func(seq, k):
    seq.sort()
    for i in xrange((len(seq)-2)):
        l = i+1
        r = len(seq) - 1
        while l < r:
            if (seq[i] + seq[l] + seq[r]) == k:
                print ("Found triplet %d %d %d" % (seq[i], seq[l], seq[r]))
                return True
            elif (seq[i] + seq[l] + seq[r]) < k:
                l += 1
            else:
                r -= 1


lis = [-1, -4, 45, 5, 10, 8]
k = 0

func(lis, k)
