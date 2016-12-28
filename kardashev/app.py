import logging

import attr
import pydux

from . import actions
from . import minds

logger = logging.getLogger(__name__)


def reducer(state, action):
    """Produce the next state of the app from the previous state and the action.
    """
    logger.debug('State: %s, Action: %s', state is not None, action)
    if state is None:
        state = minds.Mind()

    if action is None:
        return state
    else:
        state = state.handle_action(action)
    logger.debug(repr(state))
    logger.debug(repr(attr.asdict(state)))
    return state


def get_store():
    """Return a pydux store instance for the app.
    """
    store = pydux.create_store(reducer)
    store.dispatch({'type': actions.INIT})
    return store
