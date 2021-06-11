AA Draw
=======

Antialiased graphics drawing for Pygame.

.. image:: https://raw.githubusercontent.com/HuangPatrick16777216/aadraw/main/images/circles.jpg
   :alt: AA Draw vs pygame.draw antialiasing


What Is Antialiasing?
---------------------

Antialiasing is smoothing the edges in graphical drawing.
This is done by gradually mixing the drawing color with the
background color, as shown in the image above.

Pygame's drawing functions do not have antialiasing implemented,
so the resulting shapes will look jagged and rough.
AA Draw has antialiasing, so the shapes look smooth, as shown above.

AA Draw is designed to be as similar as possible to Pygame, so you
can easily switch between using AA Draw and Pygame draw.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   install
   usage
   support
