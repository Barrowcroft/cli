#  Barrowcroft, 2024

from typing import Callable

#  A simple command line interface (cli).

class CLI:
    def __init__(
        self,
        command_executor: Callable[[str], None],
        code_executor: Callable[[str], None],
        header: str = "",
        instructions: str = "",
        trailer: str = "",
        prompt: str = ">",
        multiline: bool = True,
        multiline_prompt: str = "...",
        multiline_escape: str = ".",
        multiline_end: str = ";",
        strip_multiline_escape: bool = True,
        strip_multiline_end: bool = True,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def set_prompt(self, prompt: str) -> None: ...
    def set_multiline_prompt(self, prompt: str) -> None: ...
