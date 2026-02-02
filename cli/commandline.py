"""
A simple command line interface (cli).

The cli can be used for single or multiple line entries.
Single line entries are processed as commands,
while multiple line entries are processed as code.

This module does not process the commands or the code
but passes them to the specified executor function.
"""

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class MainEnv:
    """
    The MainEnv data class contains the texts associated with the cli environment.

    prompt
        A prompt to display on each new line.
    header
        A header text to display when the cli is started.
    instructions
        An instruction text to display when the cli is started.
    trailer
        A trailer text to display when the cli is stopped.
    """

    prompt: str = ">"
    header: str = ""
    instructions: str = ""
    trailer: str = ""


@dataclass
class MultilineEnv:
    """The MultilineEnv data class describes the multiline environment.

    is_multiline
        A flag indicating if the cli allows multiple line entries.
    multiline_prompt
        In multiline mode, the cli prompt when entering multiple lines.
    multiline_escape
        In multiline mode, the sequence of characters used to indicate an entry is a command.
    multiline_end
        In multiline mode, the sequence of characters to indicate the end of a multiline entry.
    stripmultiline_escape
        In multiline mode, a flag indicating if the escape sequence
        should be stripped from the entry before processing.
    stripmultiline_end
        In multiline mode, a flag indicating if the end sequence
        should be stripped from the entry before processing.
    """

    is_multiline: bool = True
    multiline_prompt: str = "..."
    multiline_escape: str = "."
    multiline_end: str = ";"
    strip_multiline_escape: bool = True
    strip_multiline_end: bool = True


class CLI:
    """
    CLI

    The command line interface class.
    """

    def __init__(
        self,
        command_executor: Optional[Callable[[str], None]],
        code_executor: Optional[Callable[[str], None]],
    ) -> None:
        """__init__

        Initialises the cli.

        Args:
            command_executor (Callable[[str], None]):
                A reference to the function that will handle the execution of a command.
            code_executor (Callable[[str], None]):
                A reference to the function that will handle the execution of code.
        """

        self.command_executor: Optional[Callable[[str], None]] = command_executor
        self.code_executor: Optional[Callable[[str], None]] = code_executor

        self.main_env: MainEnv = MainEnv()
        self.multiline_env: MultilineEnv = MultilineEnv()

        self.halt: bool = False

    def start(self) -> None:
        """start

        Starts the cli.

        """
        #  Print header and/or instructions as required.

        if self.main_env.header != "":
            print(self.main_env.header)

        if self.main_env.instructions != "":
            print(self.main_env.instructions)

        #  Loop until the stop method is called.

        while not self.halt:

            #  Read the entry.

            _buffer: str = input(self.main_env.prompt + " ")

            if self.multiline_env.is_multiline:

                #  In multiline mode keep reading entries until the end sequence is read.

                while (
                    not _buffer.startswith(self.multiline_env.multiline_escape)
                ) and (not _buffer.endswith(self.multiline_env.multiline_end)):
                    _buffer += " " + input(self.multiline_env.multiline_prompt + " ")

                #  In multiline mode, strip escape sequence if required, and process command.

                if _buffer.startswith(self.multiline_env.multiline_escape):
                    if self.multiline_env.strip_multiline_escape is True:
                        _buffer = _buffer[1:]
                    if self.command_executor and len(_buffer.strip()) > 0:
                        self.command_executor(_buffer)
                    continue

                #  In multiline mode, strip end sequence if required, and process code.

                if _buffer.endswith(self.multiline_env.multiline_end):
                    if self.multiline_env.strip_multiline_end is True:
                        _buffer = _buffer[:-1]
                    if self.code_executor:
                        self.code_executor(_buffer)
                    continue

            #  If not multiline mode process entry as command.
            if self.command_executor:
                self.command_executor(_buffer)

        #  Print trailer as required.

        if self.main_env.trailer != "":
            print(self.main_env.trailer)

    def stop(self) -> None:
        """stop

        Stops the cli.

        """
        self.halt = True

    def set_prompt(self, prompt: str) -> None:
        """
        set_prompot

        Sets the main prompt to the specified string.

        Args:
            self (str): The propmt to set.
        """
        self.main_env.prompt = prompt

    def set_main_env(self, text_env: MainEnv) -> None:
        """
        set_main_env

        Sets the main environment.

        Args:
            main_env (MainEnv): The main environment to set.
        """
        self.main_env = text_env

    def set_multiline_env(self, multiline_env: MultilineEnv) -> None:
        """
        set_multiline_environment

        Sets the multiline environemnt.

        Args:
            multiline_env (MultilineEnv): The multiline environment to set.
        """
        self.multiline_env = multiline_env
