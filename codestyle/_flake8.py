from typing import Any, List, Optional, Tuple
import argparse
import os
import sys

from flake8 import defaults
from flake8.main import application


class InjectedApplication(application.Application):
    """Flake8 app with updated default values."""

    def parse_preliminary_options(
        self, *args: Any, **kwargs: Any
    ) -> Tuple[argparse.Namespace, list]:
        """Get preliminary options from the CLI, pre-plugin-loading.

        Args:
            args: command-line arguments passed in directly
            kwargs: command-line arguments passed in directly

        Returns:
            populated namespace and list of remaining argument strings
        """
        # rewrite default params
        self.prelim_arg_parser.set_defaults(
            exclude=(*defaults.EXCLUDE, "build", "dist"),
            ignore=(
                # flake8
                # "E203",  # TODO:
                "E731",
                "W503",
                "W504",
                "W605",
                # flake8-class-attributes-order
                # "CCE001",  # TODO:
                # flake8-docstrings
                "D100",
                "D104",
                "D107",
                "D200",
                "D204",
                "D205",
                "D212",
                "D214",
                "D301",
                "D400",
                "D401",
                "D402",
                "D412",
                "D413",
                "D415",
                # flake8-rst-docstrings
                "RST201",
                "RST203",
                "RST210",
                "RST213",
                "RST301",
                "RST304",
                # flake8-string-forma
                "P101",
                # darglint
                "DAR003",
                "DAR103",
                "DAR203"
                # pep8-naming
                "N812",
                # other ignores
                # "E1101",  # TODO:
                # "E800",  # TODO:
                # "I",  # TODO:
                # "S",  # TODO:
                # "W0221",  # TODO:
            ),
        )

        return super().parse_preliminary_options(*args, **kwargs)

    def register_plugin_options(self) -> None:
        """Register options provided by plugins to our option manager."""
        super().register_plugin_options()

        # rewrite default values for plugins
        line_length = int(os.environ.get("LINE_LENGTH", "99"))
        self.option_manager.parser.set_defaults(
            # flake8
            max_line_length=line_length,
            max_doc_length=line_length,
            # flake8-class-attributes-order
            class_attributes_order=(
                "field",
                "meta_class",
                "nested_class",
                "magic_method",
                "property_method",
                "static_method",
                "private_method",
                "method",
                "class_method",
            ),
            # flake8-docstrings
            docstring_convention="google",
            # flake8-quotes
            docstring_quotes="double",
            inline_quotes="double",
            multiline_quotes="double",
            # darglint
            docstring_style="google",
            ignore_regex="^_(.*)",
            strictness="short",
        )


def main(argv: Optional[List[str]] = None) -> None:
    """Execute the main bit of the application.

    This handles the creation of an instance of :class:`InjectedApplication`,
    runs it, and then exits the application.

    Args:
        argv: the arguments to be passed to the application for parsing

    """
    if argv is None:
        argv = sys.argv[1:]

    app = InjectedApplication()
    app.run(argv)
    app.exit()
