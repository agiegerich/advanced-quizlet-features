import sys

client_id = 'fU24waqDNX'

if len(sys.argv) > 2:
    print('Killing program.')
    exit()

secret= ''
with open('secret.txt', 'r') as myfile:
    secret=myfile.read().replace('\n', '')

print(secret)









