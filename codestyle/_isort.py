from typing import List, Optional
import functools
import os
import sys

from isort import settings


def _get_params_from_config():
    # https://github.com/PyCQA/isort/blob/bf9398ea0fed45ad1cd2899b8fd1d1c15190f025/isort/main.py#L1056+L1061
    settings_path = os.path.abspath(".") or os.getcwd()
    if not os.path.isdir(settings_path):
        settings_path = os.path.dirname(settings_path)
    settings_path = os.path.abspath(settings_path)
    project_root, config_settings = settings._find_config(settings_path)

    return config_settings


def inject() -> None:
    """Updates default values of ``isort``."""
    line_length = int(os.environ.get("LINE_LENGTH", "79"))
    default_params = {
        "force_to_top": ("typing",),
        "skip_glob": ("**/__init__.py",),
        "line_length": line_length,
        "multi_line_output": 3,
        "reverse_relative": True,
        "default_section": "THIRDPARTY",
        "use_parentheses": True,
        "order_by_type": False,
        "lines_between_types": 0,
        "combine_as_imports": True,
        "include_trailing_comma": True,
        "force_grid_wrap": 0,
        "force_sort_within_sections": True,
        "no_lines_before": ("STDLIB",),
    }

    params_in_config = _get_params_from_config()
    params_to_rewrite = {k: v for k, v in default_params.items() if k not in params_in_config}

    settings.Config = functools.partial(settings.Config, **params_to_rewrite)


def main(argv: Optional[List[str]] = None) -> None:
    """

    Args:
        argv: the arguments to be passed to the application for parsing

    """
    if argv is None:
        argv = sys.argv[1:]

    inject()

    from isort import main as scripts

    scripts.main(argv)
