import pomodoro
import cmd

class main(cmd.Cmd):
    '''エントリーポイント'''
    intro = "hello\npomodoro: start pomodoro\nquit: end"
    prompt = "> "

    def do_pomodoro(self, arg):
        '''
        start pomodoro
        also: 'p'
        '''
        p = pomodoro.Pomodoro()
        p.pomodoro()

    def do_p(self, arg):
        '''
        Abbreviation of "pomodoro"
        '''
        return self.onecmd("pomodoro")

    def do_show(self, arg):
        '''
        show num of pomodoro
        also: 's'
        '''
        p = pomodoro.Pomodoro()
        p.show_pomodoro()

    def do_s(self, arg):
        '''
        Abbreviation of "show"
        '''
        self.onecmd("show")



    def do_quit(self, arg):
        '''
        quit
        also: 'q'
        '''
        print("bye")
        return True

    def do_q(self, arg):
        '''
        Abbreviation of "quit"
        '''
        return self.onecmd("quit")

    def do_exit(self, arg):
        '''
        also: 'quit'
        '''
        self.do_quit()



m = main()
m.cmdloop()
