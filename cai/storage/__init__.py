"""Application Storage Manager

This module is used to manage application storage.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import os
import shutil
from pathlib import Path
from typing import Union

# from .utils import user_cache_dir, user_config_dir


class Storage:
    app_name: str = "CAI"

    # application config dir
    # _default_app_dir: str = user_config_dir(app_name, roaming=True)
    _default_app_dir: str = os.path.abspath("./bot/config")
    app_dir: Path = Path(os.getenv(f"{app_name}_APP_DIR", _default_app_dir))
    app_dir.mkdir(parents=True, exist_ok=True)
    if not app_dir.is_dir():
        app_dir.unlink(missing_ok=True)
        raise RuntimeError(
            f"Application directory {app_dir} is not a directory!"
        )

    # application cache dir
    # _default_cache_dir: str = user_cache_dir(app_name)
    _default_cache_dir: str = os.path.abspath("./bot/cache")
    cache_dir: Path = Path(
        os.getenv(f"{app_name}_CACHE_DIR", _default_cache_dir)
    )
    cache_dir.mkdir(parents=True, exist_ok=True)
    if not cache_dir.is_dir():
        cache_dir.unlink(missing_ok=True)
        raise RuntimeError(
            f"Application Cache directory {cache_dir} is not a directory!"
        )

    @classmethod
    def get_account_cache_dir(cls, uin: int) -> Path:
        cache = cls.cache_dir / str(uin)
        cache.mkdir(parents=True, exist_ok=True)
        return cache

    @classmethod
    def get_account_config_dir(cls, uin: int) -> Path:
        config = cls.app_dir / str(uin)
        config.mkdir(parents=True, exist_ok=True)
        return config

    @classmethod
    def clear_cache(cls):
        # FIXME: delete used dir only
        for path in cls.cache_dir.iterdir():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()


def change_config_dir(path: Union[Path, str]):
    if isinstance(path, str):
        path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    if not path.is_dir():
        path.unlink(missing_ok=True)
        raise RuntimeError(
            f"Application directory {path} is not a directory!"
        )
    Storage.app_dir = path


def change_cache_dir(path: Union[Path, str]):
    if isinstance(path, str):
        path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    if not path.is_dir():
        path.unlink(missing_ok=True)
        raise RuntimeError(
            f"Application Cache directory {path} is not a directory!"
        )
    Storage.cache_dir = path
