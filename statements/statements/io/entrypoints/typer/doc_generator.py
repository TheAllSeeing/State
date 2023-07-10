from abc import ABC, abstractmethod
from functools import wraps
from inspect import signature
from types import FunctionType


class IDocFormatter(ABC):
    @abstractmethod
    def get_formatting_dict(self) -> dict[str, str]:
        pass


class FormattedDocFunction:
    def __init__(self, func: FunctionType):
        self.inner = func

    def __get__(self, owner, owner_type: type = None):
        @wraps(self.inner)
        def result(*args, **kwargs):
            return self.inner(*args, **kwargs)
        result.__signature__ = signature(self.inner)

        if owner and isinstance(owner, IDocFormatter):
            result.__doc__ = self.inner.__doc__.format(**owner.get_formatting_dict())
        return result.__get__(owner, owner_type)
