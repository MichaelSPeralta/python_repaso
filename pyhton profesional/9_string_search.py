title = 'Professional Title, and this is an amazing Python course. You will learn Python.'
count = title.count('python')

print(count) # 2
print('python' in title.lower()) # True

# startwith('word')
# endwith(''word)

# Alineacion

message = 'Hola mundo wanaco!'

c_message = message.center(20)
l_message = message.ljust(20)
r_message = message.rjust(20)

print(c_message)
print(l_message)
print(r_message, '.')