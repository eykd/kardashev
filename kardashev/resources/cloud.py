import logging
import random

from kardashev.augmentations import Augmentation
from kardashev import loggers

logger = logging.getLogger(__name__)


class SharedHost(Augmentation):
    """Shared Virtual Host
    """
    def handle_INIT(self, mind, action):
        return self.update(
            count = 1,
        )

    def get_computation(self, mind):
        return sum([random.random()
                    for t in range(round(mind.duration))
                    for n in range(self.count)])
