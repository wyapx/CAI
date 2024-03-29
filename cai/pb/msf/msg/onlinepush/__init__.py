"""Message Service Protocol Buffer Model Category.

This module is used to store all message service protobuf files.

Generate all protobuf file using:

.. code-block:: bash

    protoc cai/pb/**/*.proto --python_out=. --mypy_out=readable_stubs:.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""

from .onlinepush_pb2 import *
from .onlinepush_trans_pb2 import *
