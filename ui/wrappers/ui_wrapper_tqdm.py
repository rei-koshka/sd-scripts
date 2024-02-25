from ..base.generics import TIterableItem
from ..base.ui_wrapper import UIWrapper

from typing import Iterable

from tqdm import tqdm

class UIWrapperTQDM(UIWrapper):
    def __init__(
        self,
        iterable: Iterable[TIterableItem],
        smoothing: float,
        disable: bool,
        desc: str,
    ):
        self.tqdm = tqdm(
            iterable=iterable,
            smoothing=smoothing,
            disable=disable,
            desc=desc,
        )

    def update(self, i: int = 1) -> None:
        self.tqdm.update(i)

    def set_postfix(
        self,
        **kwargs,
    ) -> None:
        self.tqdm.set_postfix(**kwargs)

