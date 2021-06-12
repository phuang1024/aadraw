Using AA Draw
=============

AA Draw is designed to be very similar to Pygame,
so your code can be easily reused.

Below, you can find documentation for each draw function currently available.


``aadraw.circle()``
-------------------
    :params: ``circle(surface, color, loc, radius, border)``
    :param surface: The Pygame surface to draw on.
    :param color: ``RGB`` or ``RGBA`` color of the circle.
    :param loc: ``(x, y)`` location of the center.
    :param border: Border thickness in pixels. Extends inwards.
    :return: ``None``

    Draws an antialiased circle.


``aadraw.rect()``
-----------------
    :params: ``rect(surface, color, dims, border, border_radius,``
        ``border_top_left_radius, border_top_right_radius,``
        ``border_bottom_left_radius, border_bottom_right_radius)``
    :param surface: The Pygame surface to draw on.
    :param color: ``RGB`` or ``RGBA`` color of the circle.
    :param dims: ``(x, y, w, h)`` dimensions of the rectangle.
    :param border: Border thickness in pixels. Extends inwards.
    :param border_radius: Rounding radius for each corner.
    :param border_top_left_radius: Radius of corresponding corner.
    :param border_top_right_radius: Radius of corresponding corner.
    :param border_bottom_left_radius: Radius of corresponding corner.
    :param border_bottom_right_radius: Radius of corresponding corner.
