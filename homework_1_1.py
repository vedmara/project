chairs = '15' #this is string format
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message)) #it is not correct message

#correct program
chairs = 15
nails = 4
total_nails = chairs * nails

print('You need to buy {} nails'.format(total_nails)) #it is not correct message

#it will be better
print('How many chairs do you wont to build?')
chairs = int(input())
nails = 4
total_nails = chairs * nails

print('You need to buy {} nails'.format(total_nails))