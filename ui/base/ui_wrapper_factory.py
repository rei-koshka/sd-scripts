from .generics import TIterableItem
from .ui_wrapper import UIWrapper

from typing import Iterable

class UIWrapperFactory:
    def create(
        self,
        iterable: Iterable[TIterableItem],
        smoothing: float,
        disable: bool,
        desc: str,
    ) -> UIWrapper:
        raise NotImplementedError()

