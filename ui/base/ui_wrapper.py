class UIWrapper:
    def update(self, i: int = 1) -> None:
        raise NotImplementedError()

    def set_postfix(
        self,
        **kwargs,
    ) -> None:
        raise NotImplementedError()

