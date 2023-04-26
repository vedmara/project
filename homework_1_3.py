print('How many omelets do you want to cook today?')
omelet = int(input())
eggs = 4 * omelet
bOxes = eggs // 6
message = 'You can make {} omelettes with {} boxes of eggs'.format(omelet, bOxes)
print(message) 