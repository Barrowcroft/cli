# cli
# A simple command line interface (cli)

The cli can be used for single or multiple line entries.
Single line entries are processes as commands, while multiple line entries are processed as code.

Installation: 

`pip install git+https://github.com/barrowcroft/cli.git`


### Use:

Create the CLI object:

```
from cli.commandline import CLI
cli:CLI = CLI()
```

The CLI object can be created with a number of arguments:

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

Invoke the cli instance:

`cli.start()`

Once the cli instance is runing it can be ended using:

`cli.stop()`

While runing the prompt can be set using:

`cli.set_prompt("new prompt")`

While runing the multiline prompt can be set using:

`cli.set_multiline_prompt("new multiline prompt")`