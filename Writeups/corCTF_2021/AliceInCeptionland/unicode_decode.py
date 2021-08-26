x = "\0R\u009c\u007f\u0016ndC\u0005\u00EE\u0093M\u00ED\u00C3\u00D7\u007f\u0093\u0090\u007fS}\u00AD\u0093)\u00FF\u00C3\f0\u0093g/\u0003\u0093+\u00C3\u00B6\0Rt\u007f\u0016\u0087dC\a\u00EE\u0093p\u00ED\u00C38\u007f\u0093\u0093\u007fSz\u00AD\u0093\u00C7\u00FF\u00C3\u00D30\u0093\u0086/\u0003q"
xdecoded = b"\x00R\x9c\x7f\x16ndC\x05\xee\x93M\xed\xc3\xd7\x7f\x93\x90\x7fS}\xad\x93)\xff\xc3\x0c0\x93g/\x03\x93+\xc3\xb6\x00Rt\x7f\x16\x87dC\x07\xee\x93p\xed\xc38\x7f\x93\x93\x7fSz\xad\x93\xc7\xff\xc3\xd30\x93\x86/\x03q"

d = ["\u000f", "\u0005\u0006\u0005\u0005\u0006", "\u001d\u001d\u001d\u001d\u001d", "\u0015\u0015\u0015\u0016\u0016", "nmmnmn", "ffff", "~}}~", "uvvu", "\0", "FFFF", "^]]^", "UVVU", "\f\u000f\f\u000f\f\f", "\u0004\a\u0004\u0004\a\u0004", "\u001f\u001c\u001c\u001c\u001c", "\u0014\u0014\u0014\u0014\u0017", "ol", "gg", "||\u007f|", "twtt", "OL", "GG", "\\\\_\\", "TWTT", "\0", "\0", "\u001c\u001c\u001f\u001f\u001f", "\u0017\u0017\u0017\u0014\u0014\u0014", "olll", "dggg", "|\u007f|", "wwtt", "OLLL", "DGGG", "\\_\\", "WWTT", "\0", "\u0005\u0006\u0005\u0006\u0005", "\u001d\u001d\u001d\u001e\u001e", "\u0016\u0015\u0016\u0015\u0016\u0015", "nmnm", "fef", "}}}", "\0", "NMNM", "FEF", "]]]", "\0", "\n\n\n\n\n", "\u0001\u0001\u0002\u0002\u0001\u0001", "\u001a\u001a\u001a\u001a\u0019", "\0", "ijj", "babb", "y", "\0", "IJJ", "BABB", "Y", "\0", "\0", "\0\u0003\u0003\u0003\u0003\0", "\u001b\u001b\u001b\u001b\u001b", "\u0010\u0013\u0013\u0013\u0010", "k", "``", "{{x", "\0", "K", "@@", "[[X", "\0", "\b\v\b\b\b", "\0\u0003\0\u0003\0\u0003", "\u001b\u0018\u0018\u0018\u0018", "\0", "hhkh", "c`", "xxx{", "\0", "HHKH", "C@", "XXX[", "\0", "\t\n\n\n\n\t", "\u0002\u0001\u0001\u0002\u0001", "\u001a\u001a\u0019\u0019\u0019", "\u0011\u0011\u0012\u0012\u0011\u0011", "jji", "bbb", "yzz", "qqrrqr", "JJI", "BBB", "YZZ", ]

data = ""

for i in x:
	data += i.encode("unicode_escape").decode()

print([i for i in xdecoded][::-1])