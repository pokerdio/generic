


def xpand(card):
    """card is tuple of 4 bools"""
    for i in range(4):
        if not card[i]:
            yield (*card[:i], True, *card[i + 1:])

def make_xpand_dict():
    tf = (True, False)
    g = {}
    for a in tf:
        for b in tf:
            for c in tf:
                for d in tf:
                    g[(a,b,c,d)] = list(xpand((a,b,c,d)))
    return g


def xpand2(card):
    """card is an int"""
    for bit in (1,2,4,8):
        if not (card & bit):
            yield card | bit

def make_xpand_dict2():
    g = {}
    for a in (0,1):
        for b in (0,2):
            for c in (0,4):
                for d in (0,8):
                    g[a+b+c+d] = list(xpand2(a+b+c+d))
    return g


def expand(badugi, card, v = {}):
    """badugi is a tuple of 4 bit card suit combos; card is a 4bit combo"""
    if badugi is True:
        return True
    if (badugi, card) in v:
        return v[(badugi, card)]

    s = set()

    for i in (1,2,4,8):
        if card & i:
            for b in badugi:
                s.add(i | b)
    s2 = s.copy()
    for i in s:
        for j in s:
            if i != j and i | j == i: # j is a subset of i
                s2.discard(j)
                
    ret = tuple(sorted(s2))
    v[(badugi, card)] = ret
    return ret
    

def make_b(g = []):
    """how many cards in a binary card suits representation"""
    if not g:
        h = {}
        for a in (0,1):
            for b in (0,2):
                for c in (0,4):
                    for d in (0,8):
                        h[a+b+c+d] = (a > 0) + (b > 0)+  (c > 0) + (d > 0)
        g.append (h)
        
    return g[0]

b_dict = make_b()

def recursive_display(max_depth):
    def dec (f, depth=[0]):
        def helper(*stuff):
            space = "---" * depth[0]  
            if depth[0] <= max_depth:
                print(space + ">", stuff)
            depth[0] += 1
            last_depth = depth[0]
            ret = f(*stuff)
            depth[0] =last_depth
            if depth[0] <= max_depth:
                print(space + "v", ret)
            return ret
        return helper
    return dec
#@recursive_display(4)
def go(combos, take_cards, left_cards, pattern_idx, badugi):
    g = {}

    global b_dict
    
    if take_cards == 0:
        if badugi == (15,):
            return combos
        return 0
    if pattern_idx == 16:
        return 0

    s = go(combos, take_cards, left_cards, pattern_idx + 1, badugi) # when we skip the current suit pattern

    new_combos = combos
    pat_count = b_dict[pattern_idx] # how many suits in current pattern
    for n_count in range(1, 1 + take_cards // pat_count): # how many card numbers
        badugi  = expand(badugi, pattern_idx) # when we use the current suit pattern more
        new_combos *= (left_cards + 1 - n_count)
        new_combos //= n_count
        s += go(new_combos, take_cards - n_count * pat_count, left_cards - n_count, pattern_idx + 1, badugi)

    return s
    
def solve(n):
    return go(1, n, 13, 1, (0,))


def doeet():
    s = 0
    for n in range(4, 14):
        k = solve(n)
        print(n, k)
        s += k
    return s
