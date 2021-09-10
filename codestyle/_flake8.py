from typing import List, Optional
import os
import sys

from flake8 import defaults
from flake8.main import application


class InjectedApplication(application.Application):
    """Flake8 app with updated default values."""

    def register_plugin_options(self) -> None:
        """Register options provided by plugins to our option manager."""
        super().register_plugin_options()

        # rewrite default values for plugins
        line_length = int(os.environ.get("LINE_LENGTH", "79"))
        self.option_manager.parser.set_defaults(
            # flake8
            exclude=(*defaults.EXCLUDE, "build", "dist"),
            ignore=(
                # flake8
                "E203",  # to fix incompatibilities with Black
                "E731",
                "W503",
                "W504",
                "W605",
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
                # flake8-string-format
                "P101",
                # darglint
                "DAR003",
                "DAR103",
                "DAR203",
                # pep8-naming
                "N812",
            ),
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
