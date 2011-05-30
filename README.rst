===============
kotti_analytics
===============

This is an extension to the Kotti CMS that allows you to add
Google Analytics widgets to your Kotti site.

`Find out more about Kotti`_

Setting up a widget
===========================

To set up the widget to run on every page in Kotti on the
right hand side, add ``kotti_analytics.include_widget`` to the
``kotti.includes`` setting in your Paste Deploy config::

  kotti.includes = kotti_analytics.include_widget

To set the analytics tracking id for the widget, set the
``kotti_analytics.id`` variable.  An example::

  kotti_includes = kotti_analytics.include_widget
  kotti_includes.include_widget.id = UA-XXXXXXX-X

Note that these settings have to be in your ``[app:Kotti]`` section.



.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
