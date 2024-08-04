#  Barrowcroft, 2024

from typing import Callable

#  A simple command line interface (cli).

#  The cli can be used for single or multiple line entries.
#  Single line entries are processes as commands, while multiple line entries are processed as code.


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
    ) -> None:
        """__init__

        Initialises the cli.

        Args:
            command_executor (Callable[[str], None]):
                A reference to the function that will handle the execution of a command.
            code_executor (Callable[[str], None]): _description_
                A reference to the functin that will handle the execution of code.
            header (str, optional): _description_. Defaults to "".
                An optional header text to display when the cli is started.
            instructions (str, optional): _description_. Defaults to "".
                An optional instruction text to display when the cli is started.
            trailer (str, optional): _description_. Defaults to "".
                An optional trailer text to display when the cli is stopped.
            prompt (str, optional): _description_. Defaults to ">".
                The cli prompt.

            multiline (bool, optional): _description_. Defaults to True.
                A flag indicating if the cli allows multiple line entries.
            multiline_prompt (str, optional): _description_. Defaults to "...".
                In multiline mode, the cli prompt when entering multiple lines.
            multiline_escape (str, optional): _description_. Defaults to ".".
                In multiline mode, the sequence of characters used to indicate an entry is a command.
            multiline_end (str, optional): _description_. Defaults to ";".
                In multiline mode, the sequence of characters to indicate the end of a multiline entry.
            strip_multiline_escape (bool, optional): _description_. Defaults to True.
                In multiline mode, a flag indicating if the escape sequence should be stripped from the entry before processing.
            strip_multiline_end (bool, optional): _description_. Defaults to True.
                In multiline mode, a flag indicating if the end sequence should be stripped from the entry before processing.
        """
        self._header: str = header
        self._command_executor: Callable[[str], None] = command_executor
        self._code_executor: Callable[[str], None] = code_executor
        self._instructions: str = instructions
        self._trailer: str = trailer
        self._prompt: str = prompt

        self._multiline: bool = multiline
        self._multiline_prompt: str = multiline_prompt
        self._multiline_escape: str = multiline_escape
        self._multiline_end: str = multiline_end
        self._strip_multiline_escape: bool = strip_multiline_escape
        self._strip_multiline_end: bool = strip_multiline_end

        self._halt: bool = False

    def start(self) -> None:
        """start

        Starts the cli.

        """
        #  Print header and/or instructions as required.

        if self._header != "":
            print(self._header)

        if self._instructions != "":
            print(self._instructions)

        #  Loop until the stop method is called.

        while not self._halt:

            #  Read the entry.

            _buffer: str = input(self._prompt + " ")

            #  In multiline mode keep reading entries until the end sequence is read.

            while (
                (self._multiline is True)
                and (not _buffer.startswith(self._multiline_escape))
                and (not _buffer.endswith(self._multiline_end))
            ):
                _buffer += " " + input(self._multiline_prompt + " ")

            #  In multiline mode, strip escape sequence if required, and process command.

            if (self._multiline is True) and (
                _buffer.startswith(self._multiline_escape)
            ):
                if self._strip_multiline_escape is True:
                    _buffer = _buffer[1:]
                self._command_executor(_buffer)
                continue

            #  In multiline mode, strip end sequence if required, and process code.

            if (self._multiline is True) and (_buffer.endswith(self._multiline_end)):
                if self._strip_multiline_end is True:
                    _buffer = _buffer[:-1]
                self._code_executor(_buffer)
                continue

            #  If not multiline mode process entry as command.

            self._command_executor(_buffer)

        #  Print trailer as required.

        if self._trailer != "":
            print(self._trailer)

    def stop(self) -> None:
        """stop

        Stops the cli.

        """
        self._halt = True

    def set_prompt(self, prompt: str) -> None:
        self._prompt = prompt

    def set_multiline_prompt(self, prompt: str) -> None:
        self._multiline_prompt = prompt
