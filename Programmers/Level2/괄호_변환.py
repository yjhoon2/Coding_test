def solution(p):
    def func(p):
        if len(p) == 0:
            return p
        else:
            l, r = 0, 0
            for x in p:
                if x == '(':
                    l += 1
                else:
                    r += 1
                if l == r:
                    break
            u = p[:l+r]
            v = p[l+r:]
            if u[0] == '(':
                return u + func(v)
            else:
                return '(' + func(v) + ')' + ''.join(['(' if x == ")" else ")" for x in u[1:-1]])
    return func(p)