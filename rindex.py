quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)
#2
result = quote.rindex('small')
print("Substring 'small ':", result)

# rindex 3
q= 'Do small things with great love'

print(q.rindex('t', 2))

# 4
print(q.rindex('th', 6, 20))

# 5
print(q.rindex('o small ', 10, -1))