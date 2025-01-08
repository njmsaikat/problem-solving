def solve(s):
    words=s.split(' ')
    name=' '.join(word.capitalize() for word in words)
    return name

print(solve("chris alan"))