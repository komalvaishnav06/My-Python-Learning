# frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])
print(fs1|fs2)

# 2D frozenset
fs = frozenset([1,2,3,frozenset([3,4,5])])
print(fs)