from datetime import timedelta
import logging

import arrow
import attr
from frozendict import frozendict
from straight.plugin import load as load_plugins

from . import actions
from . import augmentations

RESOURCES = load_plugins('kardashev.resources', subclasses=augmentations.Augmentation)

logger = logging.getLogger(__name__)


@attr.s()
class Mind:
    date = attr.ib(default=attr.Factory(arrow.utcnow))
    augmentations = attr.ib(default=attr.Factory(lambda: frozendict({
        resource.__name__: resource()
        for resource in RESOURCES
    })))
    computation = attr.ib(default=0.0)

    def update(self, **updates):
        return attr.assoc(self, **updates)

    def handle_action(self, action):
        new_state = {
            'augmentations': frozendict({
                name: augmentation.handle_action(self, action)
                for name, augmentation in self.augmentations.items()
            }),
            'computation': self.get_computation(),
        }
        if action['type'] == actions.ADVANCE:
            new_state['date'] = self.date + timedelta(seconds=self.duration)

        return self.update(**new_state)

    @property
    def duration(self):
        """Return the duration to advance by for the next step.
        """
        return 1

    def get_computation(self):
        return sum([aug.get_computation(self)
                    for aug in self.augmentations.values()])
