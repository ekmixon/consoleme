from typing import Any, Union


class Singleton(type):
    """Create singleton."""

    _instances = {}

    def __call__(self, *args, **kwargs) -> Union[Any]:
        """Call Singleton."""
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
