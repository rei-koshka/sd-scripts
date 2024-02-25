from ..base.generics import TIterableItem
from ..base.ui_wrapper import UIWrapper
from ..base.ui_wrapper_factory import UIWrapperFactory
from ..wrappers.ui_wrapper_tqdm import UIWrapperTQDM

from typing import Iterable

class UIWrapperFactoryTQDM(UIWrapperFactory):
    def create(
        self,
        iterable: Iterable[TIterableItem],
        smoothing: float,
        disable: bool,
        desc: str,
    ) -> UIWrapper:
        return UIWrapperTQDM(
            iterable=iterable,
            smoothing=smoothing,
            disable=disable,
            desc=desc,
        )

