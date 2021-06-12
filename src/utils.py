#
#  AADraw
#  Antialiased graphics drawing library for Python.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from typing import List, Tuple


def bounds(v: float, vmin: float = 0, vmax: float = 1) -> float:
    """
    Bound a number between a min and max.
    :param v: Number
    :param vmin: Minimum value
    :param vmax: Maximum value
    """
    return min(max(v, vmin), vmax)


def mix(c1: Tuple, c2: Tuple, fac: float) -> List[int]:
    """
    Mixes two RGB colors.
    :param c1: Color 1
    :param c2: Color 2
    :param fac: Factor of the second color.
    """
    return [int(c1[i]*(1-fac) + c2[i]*fac) for i in range(3)]


def pythag(x, y):
    return (x**2 + y**2) ** 0.5
