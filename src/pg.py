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

"""
Draws on Pygame surfaces.
"""

import pygame
from typing import Tuple
pygame.init()


def set_at(surf: pygame.Surface, loc: Tuple[int, int], color: Tuple[int, int, int, int]) -> None:
    surf.set_at(loc, color)

def get_at(surf: pygame.Surface, loc: Tuple[int, int]) -> Tuple[int, int, int, int]:
    color = surf.get_at(loc)
    if len(color) == 3:
        return (color[0], color[1], color[2], 255)
    elif len(color) == 4:
        return tuple(color)
    else:
        raise ValueError(f"Expected color length of pygame.Surface to be 3 or 4, but got {len(color)}")
