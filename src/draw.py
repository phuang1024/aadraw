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

import pygame
from typing import Tuple
from .utils import *
pygame.init()

__all__ = (
    "circle",
)


def circle(surface: pygame.Surface, color: Tuple, loc: Tuple[float, float], radius: float,
        border: float = 0) -> None:
    """
    Draws a circle.
    :param surface: Pygame surface to draw on.
    :param color: RGB or RGBA color.
    :param loc: (x, y) location.
    :param radius: Radius of the circle.
    :param border: Border thickness (px). Set to 0 for no border. Extends inward.
    """
    cx, cy = loc
    w, h = surface.get_size()
    afac = color[3]/255 if len(color) == 4 else 1
    color = color[:3]

    out_thres = radius
    in_thres = 0 if border == 0 else (radius-border)

    x_min = max(0, int(cx-radius)-1)
    x_max = min(w, int(cx+radius)+2)
    y_min = max(0, int(cy-radius)-1)
    y_max = min(h, int(cy+radius)+2)

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            dist = ((x-cx)**2 + (y-cy)**2) ** 0.5
            out_fac = bounds(out_thres-dist+1)
            in_fac = bounds(dist-in_thres+1)
            col = mix(surface.get_at((x, y)), color, out_fac*in_fac*afac)
            surface.set_at((x, y), col)
