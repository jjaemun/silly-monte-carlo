# -*- coding: utf-8 -*-


import numpy
from typing import Optional, Union, TypeAlias


# Notes
#
# Generally we will pass seeds of type `Seed` to `Simulators`.
#
# The idea is that since `numpy.random.default_rng` can take
# in either an `int`, `None`, or an existing `Generator`, we
# model that behaviour exactly.
#
# Examples
#
# ```python
#   fresh = numpy.random.default_rng(None)
#   seeded = numpy.random.default_rng(0)
#   shared = numpy.random.default_rng(seeded)   # `shared is seeded`
# ```

Seed: TypeAlias = Optional[Union[int, numpy.random.Generator]]
