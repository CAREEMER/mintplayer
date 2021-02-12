class Printer():

    def __init__(self, *args, **kwargs):

        self.options = {
            'position' : 'left'
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

        elif self.options['position'] == 'left':
            print(content)


class Command():

    def __init__(self):

        self.list_of_commands = {
        'help' : 'Gives a list of commands with descriptions. Usage: help [command(optional)].',
        'ps' : 'Plays a song. Usage: playsong [path-to-the-mp3].',
        'psf' : 'Plays a song from your favorites! Usage: psf [songname].', 
        'pause' : 'Pauses currently playing song.',
        'unpause' : 'Unpauses stopped song.',
        'stop' : 'Stops currently playing song.',
        'vol' : 'Sets level of the volume. Usage: vol [0.0 - 1.0]',
        'psr' : 'Plays a random song from your favorites!',
        'addsong' : 'Adding mp3 song to your favorites. Usage: addsong [path-to-the-mp3].',
        'lib' : 'Gives a nice list of your favourite songs!',
        'exit' : 'Closes the app.'
        }

        self.player = Player()
        self.mp = Printer()
        self.Lib = Librarian()
    
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
            from os import replace, getcwd, path
            try:
                replace(args[1], path.join(getcwd(), 'songlib', path.basename(args[1])))
                self.Lib.add_fav(path.basename(args[1]))
            except:
                print(f'There is no song at this path >{args[1]}')

        elif args[0] == 'ps':
            try:
                self.player.play(args[1])
            except:
                print(f'There is no song at this path >{args[1]}')

        elif args[0] == 'psf':
            if len(args) == 1:
                print("There is no song. Please, use 'help psf'.")
            else:
                from os import path
                self.player.play(path.join('songlib', args[1]))
        
        elif args[0] == 'stop':
            self.player.stop()

        elif args[0] == 'pause':
            self.player.pause()

        elif args[0] == 'unpause':
            self.player.unp()
        
        elif args[0] == 'vol':
            if len(args) == 1:
                print("There is no level of the volume. Please, use 'help vol'.")
            elif 0 <= float(args[1]) <= 1:
                self.player.setvol(float(args[1]))
            else:
                print('The volume level must set between 0 and 1 [0; 1].')

        elif args[0] == 'lib':
            for idx, song in enumerate(self.Lib.extract_favs()):
                print(f'{idx + 1} - {song}')

        elif args[0] == 'psr':
            import random
            from os import path

            favs = self.Lib.extract_favs()
            self.player.play(path.join('songlib', favs[random.randint(0, len(favs) - 1)]))

        elif args[0] == 'exit':
            self.mp.print('Goodbye! See you soon!')
            self.player.exit(300)

        elif args[0] == '':
            pass

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

    def pause(self):
        self.player.music.pause()

    def unp(self):
        self.player.music.unpause()

    def setvol(self, level):
        self.player.music.set_volume(level)

    def exit(self, delay):
        from time import sleep

        if self.player.music.get_busy() == True:
            self.player.music.fadeout(delay)
            sleep(delay / 300)
        exit()


class Librarian():

    def __init__(self):
        Librarian.update(self)

    def update(self):
        from os import listdir
        from os.path import isfile, join

        self.lib = {
            'favs' : [filename for filename in listdir('songlib') if (isfile(join('songlib', filename))) & ('.mp3' in filename)],
        }

    def extract_favs(self):
        return self.lib['favs']

    def add_fav(self, songname):
        Librarian.update(self)
