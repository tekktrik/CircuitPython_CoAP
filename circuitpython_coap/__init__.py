# SPDX-FileCopyrightText: 2025 Alec Delaney
# SPDX-License-Identifier: MIT

try:
    from typing import Union, Callable, Literal, Dict, TypeAlias
    from functools import wraps
except ImportError:
    pass

_REGISTERED_FUNCS: Dict[str, Dict[str, Callable]] = {}

class _CoapBase:

    def __init__(self) -> None: ...

    def send(self, payload: Union[str, bytes]) -> bool: ...

    def receive(self) -> str: ...


def register(
        method: Literal["GET", "POST", "PUT", "DELETE"],
        uri: str,
    ) -> Callable:

    def register_inner(func: Callable) -> Callable:

        if method not in _REGISTERED_FUNCS:
            _REGISTERED_FUNCS[method] = {}

        # TODO: Handle escaped characters
        
        if uri in _REGISTERED_FUNCS[method]:
            raise RuntimeError("This URI has already been registered")
        
        _REGISTERED_FUNCS[method][uri] = func

        return func
    
    return register_inner


def get(uri: str) -> Callable:
    """Register the function to a GET method."""

def post(uri: str) -> Callable:
    """Register the function to a POST method."""
    
def put(uri: str) -> Callable:
    """Register the function to a PUT method."""

def delete(uri: str) -> Callable:
    """Register the function to a DELETE method."""
