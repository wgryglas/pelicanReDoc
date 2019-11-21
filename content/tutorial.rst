-------------------
Pipe Tee
-------------------
:date: 2019-10-13 20:06
:modified: 2019-10-13 20:06
:tags: meshing, snappyHexMesh, pipe-tee,
:category: meshing
:slug: simple-meshing
:authors: Wojtciech Gryglas
:summary: Create Mesh in Few Clicks


Start Case
==========

 1. Enter the ``Case Name``
 2. Hit ``Create Case`` button to launch SimFlow

.. image:: ./figures/tutorial/screenshot_0.png
    :alt: launcher window

Import Geometry
===============
After launching software go directly to 

  #. ``Geometry Panel``
  #. Click Load Geometry button
  #. Select appropriate ``pipe-tee.stl`` file
  #. Click ``Open`` button to load geometry

.. image:: ./figures/tutorial/screenshot_2.png


Split Geometry
==============

If the geometry file is of STL type usually we would expect
to have geometry as an only single surface.

.. note:: STL format is a surface mesh format. The geometry is defained
   as a huge collection of small triangular elements which define a surface. 
   This format is usually used in graphics geometry models and recently is 
   well known in the 3D printing world.

.. image:: ./figures/tutorial/screenshot_4.png


.. image:: ./figures/tutorial/screenshot_5.png

Inlet 1 Face
============
Selection
-------------
.. image:: ./figures/tutorial/screenshot_6.png

Rename
-------------
.. image:: ./figures/tutorial/screenshot_8.png

Outlet Face
===========
.. image:: ./figures/tutorial/screenshot_7.png

.. image:: ./figures/tutorial/screenshot_9.png

Inlet 2 Face
============
.. image:: ./figures/tutorial/screenshot_10.png


.. image:: ./figures/tutorial/screenshot_11.png

Meshing Geometry
================

.. image:: ./figures/tutorial/screenshot_12.png

Base Mesh
=========
.. image:: ./figures/tutorial/screenshot_13.png

Create Mesh
===========
.. image:: ./figures/tutorial/screenshot_14.png


View Mesh
=========
.. image:: ./figures/tutorial/screenshot_15.png



.. image:: ./figures/tutorial/screenshot_16.png



.. image:: ./figures/tutorial/screenshot_3.png
