from dataclasses import dataclass, field
from typing import Any, Callable


CallbackType = Callable[..., Any]

class HandlerObject:

    def __init__(self, callback: CallbackType, filters: list[Any]):
        self.callback = callback
        self.filters  = filters
        self.params = callback.__code__.co_varnames


    def _prepare_kwargs(self, kwargs: dict[str, Any]) -> dict[str, Any]:
        return {
            k: v for k, v in kwargs.items() if k in self.params
        }

    async def check_filters(self, *args, **kwargs) -> tuple[bool, Any]:
        for filter in self.filters:
            result = await filter()

            if not result: return False, None

            if isinstance(result, dict):
                kwargs.update(result)
        
        return True, kwargs
    
    async def call(self, *args, **kwargs) -> bool:
        _call, _kwargs = await self.check_filters(*args, **kwargs)

        if _call:
            await self.callback(*args, **self._prepare_kwargs(kwargs | _kwargs))
            return True

        return False