import logging

import attr

from . import loggers

logger = logging.getLogger(__name__)


@attr.s()
class Augmentation:
    research_cost = 0

    base_cost = 1.0

    count = attr.ib(default=0)
    computation = attr.ib(default=0)

    def update(self, **updates):
        return attr.assoc(self, **updates)

    def handle_action(self, mind, action):
        if action is None:
            return self

        handler = getattr(self, 'handle_%s' % action['type'], None)
        if handler is not None:
            return handler(mind, action)
        else:
            return self

    def handle_ADVANCE(self, mind, action):
        return self.update(
            computation = self.get_computation(mind),
        )

    def get_computation(self, mind):
        return 0
