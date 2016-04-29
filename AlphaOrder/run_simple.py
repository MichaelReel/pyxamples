def alphorder(s):
    if s == ''.join(sorted(s)):
        print s, "IN ORDER"
    elif s == ''.join(sorted(s, reverse=True)):
        print s, "REVERSE ORDER"
    else:
        print s, "NOT IN ORDER"
		
alphorder("billowy")
alphorder("biopsy")
alphorder("chinos")
alphorder("defaced")
alphorder("chintz")
alphorder("sponged")
alphorder("bijoux")
alphorder("abhors")
alphorder("fiddle")
alphorder("begins")
alphorder("chimps")
alphorder("wronged")