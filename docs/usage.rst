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
