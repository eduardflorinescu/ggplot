{ggplot} from `Yhat <http://yhathq.com>`__
==========================================

read more on our
`blog <http://blog.yhathq.com/posts/ggplot-for-python.html>`__

::

    from ggplot import *

    ggplot(aes(x='date', y='beef'), data=meat) + \
        geom_point(color='lightblue') + \
        stat_smooth(span=.15, color='black', se=True) + \
        ggtitle("Beef: It's What's for Dinner") + \
        xlab("Date") + \
        ylab("Head of Cattle Slaughtered")

What is it?
~~~~~~~~~~~

Yes, it's another port of
```ggplot2`` <https://github.com/hadley/ggplot2>`__. One of the biggest
reasons why I continue to reach for ``R`` instead of ``Python`` for data
analysis is the lack of an easy to use, high level plotting package like
``ggplot2``. I've tried other libraries like
```bokeh`` <https://github.com/continuumio/bokeh>`__ and
```d3py`` <https://github.com/mikedewar/d3py>`__ but what I really want
is ``ggplot2``.

``ggplot`` is just that. It's an extremely un-pythonic package for doing
exactly what ``ggplot2`` does. The goal of the package is to mimic the
``ggplot2`` API. This makes it super easy for people coming over from
``R`` to use, and prevents you from having to re-learn how to plot
stuff.

Goals
~~~~~

-  same API as ``ggplot2`` for ``R``
-  never use matplotlib again
-  ability to use both American and British English spellings of
   aesthetics
-  tight integration with
   ```pandas`` <https://github.com/pydata/pandas>`__
-  pip installable

Getting Started
~~~~~~~~~~~~~~~

Dependencies
^^^^^^^^^^^^

I realize that these are not fun to install. My best luck has always
been using ``brew`` if you're on a Mac or just using `the
binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`__ if you're on
Windows. If you're using Linux then this should be relatively painless.
You should be able to ``apt-get`` or ``yum`` all of these. -
``matplotlib`` - ``pandas`` - ``numpy`` - ``scipy`` - ``statsmodels`` -
``patsy``

Installation
^^^^^^^^^^^^

Ok the hard part is over. Installing ``ggplot`` is really easy. Just use
``pip``! An item on the TODO is to add the matplotlibrc files to the pip
installable (let me know if you'd like to help!).

*``matplotlibrc`` will be replaced with themes in the 0.3 release*

::

    # matplotlibrc from Huy Nguyen (http://www.huyng.com/posts/sane-color-scheme-for-matplotlib/)
    $ curl -O https://raw.github.com/yhat/ggplot/master/matplotlibrcs/matplotlibrc-osx.zip
    $ unzip matplotlibrc-osx.zip -d ~/
    # install ggplot using pip
    $ pip install ggplot

NOTE: You might want to install matplotlibrc files for other platforms
(e.g., Windows). See ``matplotlibrcs``.

Loading ``ggplot``
^^^^^^^^^^^^^^^^^^

::

    # run an IPython shell (or don't)
    $ ipython
    In [1]: from ggplot import *

That's it! You're ready to go!

Examples
~~~~~~~~

::

    meat_lng = pd.melt(meat[['date', 'beef', 'pork', 'broilers']], id_vars='date')
    ggplot(aes(x='date', y='value', colour='variable'), data=meat_lng) + \
        geom_point() + \
        stat_smooth(color='red')

``geom_point``
^^^^^^^^^^^^^^

::

    from ggplot import *
    ggplot(diamonds, aes('carat', 'price')) + \
        geom_point(alpha=1/20.) + \
        ylim(0, 20000)

``geom_histogram``
^^^^^^^^^^^^^^^^^^

::

    p = ggplot(aes(x='carat'), data=diamonds)
    p + geom_histogram() + ggtitle("Histogram of Diamond Carats") + labs("Carats", "Freq") 

``geom_density``
^^^^^^^^^^^^^^^^

::

    ggplot(diamonds, aes(x='price', color='cut')) + \
        geom_density()

::

    meat_lng = pd.melt(meat[['date', 'beef', 'broilers', 'pork']], id_vars=['date'])
    p = ggplot(aes(x='value', colour='variable', fill=True, alpha=0.3), data=meat_lng)
    p + geom_density()

``geom_bar``
^^^^^^^^^^^^

::

    p = ggplot(mtcars, aes('factor(cyl)'))
    p + geom_bar()

TODO
~~~~

`The list is long, but
distinguished. <https://github.com/yhat/ggplot/blob/master/TODO.md>`__
We're looking for contributors! Email greg at yhathq.com for more info.
For getting started with contributing, check out `these
docs <https://github.com/yhat/ggplot/blob/master/docs/contributing.md>`__
