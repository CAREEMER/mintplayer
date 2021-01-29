class Printer():

    def __init__(self, *args, **kwargs):

        self.options = {
            'position' : 'middle'
        }
        self.options.update(kwargs)

    def print(self, content):

        from os import get_terminal_size

        size = get_terminal_size()
    
        if self.options['position'] == 'middle':
            if size[0] > len(content):
                spaces = ( size[0] - len(content) ) // 2
                print(str().join([' ' for i in range(0,spaces)]) + content)
            else:
                print(content)

        elif self.options['position'] == 'right':
            if size[0] > len(content):
                spaces = size[0] - len(content)
                print(str().join([' ' for i in range(0,spaces)]) + content)
            else:
                print(content)


class Command():

    def __init__(self):

        self.list_of_commands = {
        'help' : 'Gives a list of commands with descriptions. Usage: help [command(optional)]',
        'ps' : 'Plays a song. Usage: playsong [path-to-the-mp3]',
        'pause' : 'Pauses currently playing song.',
        'unpause' : 'Unpauses stopped song',
        'psr' : 'Plays a random song from your favorites!',
        'addsong' : 'Adding mp3 song to your favorites. Usage : addsong [path-to-the-mp3]',
        'lib' : 'Gives a nice list of your favourite songs!',
        'exit' : 'Closes the app'
        }

        self.player = Player()
        self.mp = Printer()
    
    def exe(self, notself):

        args = notself.split(' ')

        if args[0] == 'help':
            if len(args) == 1:
                for command in self.list_of_commands:
                    print(f'{command} - {self.list_of_commands[command]}')
            else:
                args.pop(0)
                for command in args:
                    try:
                        print(f'{command} - {self.list_of_commands[command]}')
                    except:
                        print(f'There is no such command here named {command}')

        elif args[0] == 'addsong':
            pass

        elif args[0] == 'ps':
            try:
                self.player.play(args[1])
            except:
                print(f'There is no song at this path >{args[1]}')
        
        elif args[0] == 'pause':
            self.player.stop()

        elif args[0] == 'unpause':
            self.player.unp()
        
        elif args[0] == 'exit':
            self.mp.print('Goodbye! See you soon!')
            self.player.exit(100)

        else: 
            print(f'There is no such command here named {command}')


class Player():
    def __init__(self):
        from pygame import mixer
        self.player = mixer
        self.player.init()

    def play(self, path):
        self.player.music.set_volume(0.1)
        self.player.music.load(path)
        self.player.music.play()

    def stop(self):
        self.player.music.stop()

    def unp(self):
        self.player.music.unpause()

    def exit(self, delay):
        from time import sleep

        if self.player.music.get_busy() == True:
            self.player.music.fadeout(delay)
            sleep(delay/100)
        exit()

    