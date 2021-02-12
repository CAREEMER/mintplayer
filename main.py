import classes

mp = classes.Printer()
cmd = classes.Command()
mp.print('Welcome to the mintplayer!')
mp.print('Enter the command below: (help for an help)')

while 1:
        cmd.exe(input('>'))