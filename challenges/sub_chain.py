# management of sub-chains

chain = 'Hello world!'

subchain_hello = chain[0:5]  # 'Hello'
subchain_world = chain[6:11]  # 'world'
print(f'Sub chain of, {subchain_hello} ')
print(f'Sub chain of, {subchain_world} ')

# finding the index of a subchain
subchain_index = chain.find(subchain_hello)
print(f'Index of subchain {subchain_hello} is {subchain_index}')

# replacing a subchain
chain = chain.replace(subchain_hello, 'Hi')
print(f'Chain after replacing {subchain_hello} with Hi: {chain}')

# splitting substrings with split()
chain = 'Hello world!'
subchains = chain.split(' ')
print(f'Subchains after splitting {chain} with space: {subchains}')