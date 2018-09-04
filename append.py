appendMe = '\nWelcome chandan'

appendFile = open('friends.txt', 'a')
appendFile.write(appendMe)
appendFile.close()