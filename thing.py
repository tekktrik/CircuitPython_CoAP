from circuitpython_coap import get

@get("FDS")
def addition(a: int, b: int) -> int:
    """AAAA"""
    return a + b


x = addition()