# cli
# A simple command line interface (cli)

The cli can be used for single or multiple line entries.
Single line entries are processed as commands,
while multiple line entries are processed as code.

This module does not process the commands or the code
but passes them to the specified executor function.

Installation: 

`pip install git+ssh://git@github.com/Barrowcroft/cli.git`

or

`uv add git+https://git@github.com/barrowcroft/cli.git`

### Use:

Create the CLI object:

```
from cli.commandline import CLI
cli:CLI = CLI(my_command_executor, my_code_executor)
```

The CLI object should be created with two arguments:

    command_executor (Optional[Callable[[str], None]]):
        A reference to the function that will handle the execution of a command.

    code_executor (Optional[Callable[[str], None]]):         
        A reference to the function that will handle the execution of code.

Invoke the cli instance:

`cli.start()`

Once the cli instance is runing it can be ended using:

`cli.stop()`

### Configuration:

The main environment is set using the MainEnv data class as follows:

MainEnv data class fields:

    prompt
        A prompt to display on each new line.
    header
        A header text to display when the cli is started.
    instructions
        An instruction text to display when the cli is started.
    trailer
        A trailer text to display when the cli is stopped.

Usage:
```
from cli.commandline import MainEnv

my_main_env:MainEnv = MainEnv()
my_main_env.prompt = ">"
my_main_env.header = "my header text"
my_main_env.instructions = "my instructions text"
my_main_env.trailer = "my trailer text"

cli.set_main_env(my_main_env)
```

The multiline environment is set using the MultilineEnv data class as follows:

MultilineEnv data class fields:

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

Usage:
```
from cli.commandline import MultilineEnv

my_multiline_env:MultilineEnv = MultilineEnv()
my_multiline_env.is_multiline= True
my_multiline_env.multiline_prompt = "..."
my_multiline_env.multiline_escape = "."
my_multiline_env.multiline_end:= ";"
my_multiline_env.strip_multiline_escape = True
my_multiline_env.strip_multiline_end = True

cli.set_multiline_env(my_multiline_env)
```
