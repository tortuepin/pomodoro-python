import pomodoro
import cmd

class main(cmd.Cmd):
    '''エントリーポイント'''
    intro = "hello\npomodoro: start pomodoro\nquit: end"
    prompt = "> "

    def do_pomodoro(self, arg):
        p = pomodoro.Pomodoro()
        p.pomodoro()

    def do_quit(self, arg):
        print("bye")
        return True

    def do_exit(self, arg):
        self.do_quit()



m = main()
m.cmdloop()
