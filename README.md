# Griptape Extension Template

A Github template repository for creating Griptape extensions.

## Getting Started

Via github web page:

Click on `Use this template`

![](https://docs.github.com/assets/cb-36544/images/help/repository/use-this-template-button.png)


Via `gh`:

```
$ gh repo create griptape-extension-name -p griptape/griptape-extension-template
```

## What is a Griptape Extension?

Griptape Extensions can add new functionality to the [Griptape framework](https://github.com/griptape-ai/griptape), such as new Tools, Drivers, Tasks, or Structures.
With extensions, you can integrate custom APIs, tools, and services into the Griptape ecosystem.

This repository provides a recommended structure for organizing your extension code, as well as helpful tools for testing and development.

## Extension Structure

The template repository is structured as follows:

```bash
tree -I __init__.py -I __pycache__

├── griptape
│   └── extension_name # Name whatever you want
│       └── tools
│           └── reverse_string
│               └── tool.py
            ...more directories for other interfaces (drivers, tasks, structures, etc)...
└── tests
    └── unit
        └── tools
            └── test_reverse_string_tool.py
├── examples
    └── tools
        └── example_agent.py # Example usage of the extension 
├── LICENSE # Choose the appropriate license
├── Makefile # Contains useful commands for development
├── pyproject.toml # Contains the project's metadata
├── README.md #  Describes the extension and how to use it
```

## Development

### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management.
It is recommended to configure Poetry to use [in-project](https://python-poetry.org/docs/configuration/#virtualenvsin-project) virtual environments:

```bash
poetry config virtualenvs.in-project true
```

This will create a `.venv` directory in the project root, where the virtual environment will be stored.
This ensures that the virtual environment is always in the same location, regardless of where the project is cloned.

### Useful Commands

#### Installing Dependencies

```bash
make install
```

#### Running Tests

```bash
make test
```

#### Running Checks (linting, formatting, etc)

```bash
make check
```

#### Running Formatter

```bash
make format
```

#### Running Example

This template includes an [example](https://github.com/griptape-ai/tool-template/blob/main/examples/tools/example_agent.py) demonstrating how to use the extension. It shows how to import the `ReverseStringTool`, provide it to an Agent, and run it.

1. Set the required environment variables. The example needs the `OPENAI_API_KEY` environment variable to be set.
2. Run the example:

```bash
poetry run python examples/tools/example_agent.py
```

If successful, you should see:
```
[11/18/24 14:55:14] INFO     ToolkitTask 6bb7fa5581d147b2a39e801631c98005
                             Input: Use the ReverseStringTool to reverse 'Griptape'
[11/18/24 14:55:15] INFO     Subtask c3036471831144529b8d5300c6849203
                             Actions: [
                               {
                                 "tag": "call_VE4tGBFL7iB7VDbkKaIFIkwY",
                                 "name": "ReverseStringTool",
                                 "path": "reverse_string",
                                 "input": {
                                   "values": {
                                     "input": "Griptape"
                                   }
                                 }
                               }
                             ]
                    INFO     Subtask c3036471831144529b8d5300c6849203
                             Response: epatpirG
[11/18/24 14:55:16] INFO     ToolkitTask 6bb7fa5581d147b2a39e801631c98005
                             Output: The reversed string of "Griptape" is "epatpirG".
```

## Installing in Other Projects

Extensions are designed to be shared. Extensions are made to easily install into existing Python projects.

The easiest way to include your extension into an existing project is to install directly from the repository, like so:
```bash
poetry add git+https://github.com/{your-org}/{your-extension-name}.git
```

To install a local copy of the extension for development, run:
```bash
poetry add -e /path/to/your/extension
```

Any changes made to the extension will be automatically reflected in the project without needing to reinstall it.

Advanced customers may seek to publish their extensions to PyPi. Those instructions are beyond the scope of this README.
