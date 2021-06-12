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
Antialiased Pygame drawing library.
"""

"""
Variable names used:
- x, y: Current x or y of pixel-by-pixel drawing.
- w, h: Width and height of shape dimensions
- width, height: Dimensions of surface
- cx, cy: Center X, center Y
- dx, dy: Dimension x, dimension y of shape
"""

import pygame
from typing import Tuple
from .utils import *
pygame.init()

__all__ = (
    "circle",
    "rect",
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
    width, height = surface.get_size()

    afac = color[3]/255 if len(color) == 4 else 1
    color = color[:3]
    out_thres = radius
    in_thres = 0 if border == 0 else (radius-border)

    x_min = max(0, int(cx-radius)-1)
    x_max = min(width, int(cx+radius)+2)
    y_min = max(0, int(cy-radius)-1)
    y_max = min(height, int(cy+radius)+2)
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            dist = pythag(x-cx, y-cy)
            out_fac = bounds(out_thres-dist+1)
            in_fac = bounds(dist-in_thres+1)
            col = mix(surface.get_at((x, y)), color, out_fac*in_fac*afac)
            surface.set_at((x, y), col)


def rect(surface: pygame.Surface, color: Tuple, dims: Tuple[float, float, float, float],
        border: float = 0, border_radius: float = 0, border_top_left_radius: float = ...,
        border_top_right_radius: float = ..., border_bottom_left_radius: float = ...,
        border_bottom_right_radius: float = ...) -> None:
    """
    Draws a rectangle.
    :param surface: Pygame surface to draw on.
    :param color: RGB or RGBA color.
    :param dims: Dimensions (x, y, w, h).
    :param border: Border thickness in pixels. Extends inward.
    :param border_radius: Radius for border rounding.
    :param border_top_left_radius: Radius of corresponding corner.
    :param border_top_right_radius: Radius of corresponding corner.
    :param border_bottom_left_radius: Radius of corresponding corner.
    :param border_bottom_right_radius: Radius of corresponding corner.
    """
    width, height = surface.get_size()
    dx, dy, dw, dh = dims
    b = border
    radii = (
        border_radius if border_top_left_radius     is ... else border_top_left_radius,
        border_radius if border_top_right_radius    is ... else border_top_right_radius,
        border_radius if border_bottom_right_radius is ... else border_bottom_right_radius,
        border_radius if border_bottom_left_radius  is ... else border_bottom_left_radius,
    )
    thresholds = [(r, (0 if border == 0 else r-border)) for r in radii]

    afac = color[3]/255 if len(color) == 4 else 1
    color = color[:3]

    x_min = max(0,     int(dx)   -1)
    x_max = min(width, int(dx+dw)+2)
    y_min = max(0,     int(dy)   -1)
    y_max = min(width, int(dy+dh)+2)
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            # Calculate corner info
            corner_info = None
            if x < dx+radii[0] and y < dy+radii[0]:          # Top left corner
                corner_info = (0, dx+radii[0], dy+radii[0])
            elif x > dx+dw-radii[1] and y < dy+radii[1]:     # Top right corner
                corner_info = (1, dx+dw-radii[1], dy+radii[1])
            elif x > dx+dw-radii[2] and y > dy+dh-radii[2]:  # Bottom right corner
                corner_info = (2, dx+dw-radii[2], dy+dh-radii[2])
            elif x < dx+radii[3] and y > dy+dh-radii[3]:     # Bottom left corner
                corner_info = (3, dx+radii[3], dy+dh-radii[3])

            # Calculate edge antialiasing
            out_fac = bounds(x-dx+1) * bounds(dx+dw-x+1) * bounds(y-dy+1) * bounds(dy+dh-y+1)
            if border == 0:
                in_fac = 1
            else:
                in_fac = bounds(dx+b-x+1) + bounds(x-(dx+dw-b)+1) + bounds(dy+b-y+1) + bounds(y-(dy+dh-b)+1)
            final_fac = in_fac * out_fac

            if corner_info is not None:
                # If pixel is corner replace edge aa with corner aa
                num, cx, cy = corner_info
                dist = pythag(x-cx, y-cy)
                out_fac = bounds(thresholds[num][0]-dist+1)
                in_fac = bounds(dist-thresholds[num][1]+1)
                final_fac = out_fac*in_fac*afac

            col = mix(surface.get_at((x, y)), color, final_fac)
            surface.set_at((x, y), col)
