import factory

from . import minds


class MindFactory(factory.Factory):
    class Meta:
        model = minds.Mind
