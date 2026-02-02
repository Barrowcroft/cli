# pylint: skip-file

from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class MainEnv:
    prompt: str
    header: str
    instructions: str
    trailer: str

@dataclass
class MultilineEnv:
    is_multiline: bool
    multiline_prompt: str
    multiline_escape: str
    multiline_end: str
    strip_multiline_escape: bool
    strip_multiline_end: bool

class CLI:
    command_executor: Optional[Callable[[str], None]]
    code_executor: Optional[Callable[[str], None]]
    main_env: MainEnv
    multiline_env: MultilineEnv
    halt: bool

    def __init__(
        self,
        command_executor: Optional[Callable[[str], None]],
        code_executor: Optional[Callable[[str], None]],
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def set_prompt(self, prompt: str) -> None: ...
    def set_main_env(self, text_env: MainEnv) -> None: ...
    def set_multiline_env(self, multiline_env: MultilineEnv) -> None: ...
