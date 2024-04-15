from typing import Protocol

class IHelloService(Protocol):
    def say_hello(self) -> None: ...
