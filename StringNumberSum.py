def string_number_sum(a, b):
    if not(isinstance(a, str) and isinstance(b, str)):
        return "invalid data"
    else:
        l1 = len(a)
        l2 = len(b)
        i = 0
        if l1 >= l2:
            i = l1-1
        else:
            i = l2-1
        l1 -= 1
        l2 -= 1
        carry = 0
        sum = ""
        while i >= 0:
            cura = '0'
            curb = '0'
            if l1 >= 0:
                cura = a[l1]
                l1 -= 1
            if l2 >= 0:
                curb = b[l2]
                l2 -= 1
            d1 = ord(cura) - ord('0')
            d2 = ord(curb) - ord('0')

            v = d1 + d2 + carry
            val = ""
            if(v >= 10):
                carry = 1
                val = str(v)
                val = val[len(val)-1]
            else:
                carry = 0
                val = str(v)
            temp = str(val) + sum
            sum = temp
            i -= 1
        if carry > 0:
            temp = str(carry) + sum
            sum = temp
    return sum



a = "123619237123012830790458273453"
b = "12312031926312939012731923712312312381209979"

print (string_number_sum(a, b))
