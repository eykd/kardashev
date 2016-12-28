import logging

from . import actions
from . import app
from . import loggers

logger = logging.getLogger(__name__)


class CLIApp:
    def __init__(self):
        import urwid
        self.urwid = urwid
        self.store = app.get_store()
        self.date_txt = urwid.Text(self.get_date())
        self.computation_txt = urwid.Text(self.get_computation())
        self.fill = urwid.Filler(
            urwid.Pile([
                self.date_txt,
                self.computation_txt
            ] + [urwid.Text(str(aug)) for aug in self.store.get_state().augmentations.values()]),
            'top',
        )

        self.store.subscribe(self.update_ui)

    def run(self):
        loop = self.urwid.MainLoop(self.fill, unhandled_input=self.handle_input)
        loop.set_alarm_in(1, self.increment_every_second)
        return loop.run()

    def advance(self):
        self.store.dispatch({'type': actions.ADVANCE})

    def update_ui(self):
        self.date_txt.set_text(self.get_date())
        self.computation_txt.set_text(self.get_computation())

    def get_date(self):
        state = self.store.get_state()
        if state is None:
            return ''
        else:
            return state.date.isoformat()

    def get_computation(self):
        state = self.store.get_state()
        if state is None:
            result = 'Computation:'
        else:
            result = 'Computation: %s' % state.computation
        logger.debug(result)
        return result

    def increment_every_second(self, loop, _):
        self.advance()
        loop.set_alarm_in(1, self.increment_every_second)

    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise self.urwid.ExitMainLoop()
        elif key == ' ':
            self.advance()

def main():
    logging.basicConfig(filename='kardashev.log', filemode='w', level=logging.DEBUG)
    CLIApp().run()


if __name__ == '__main__':
    main()
