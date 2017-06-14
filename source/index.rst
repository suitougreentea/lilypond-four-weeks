.. LilyPond Four Weeks documentation master file, created by
   sphinx-quickstart on Tue Jun 13 23:02:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LilyPond Four Weeks's documentation!
===============================================

Contents:

.. toctree::
   :maxdepth: 2

.. lily::

  <<
  \new Staff {
    \relative c'' {
     c4 a d e \break
     g a b c d^\markup \italic "Yeah"
    }
  }
  \new Staff {
    \relative c'' {
     c4 a d e
    }
  }
  >>

.. code-block:: lilypond

  <<
  \new Staff {
    \relative c'' {
     c4 a d e \break
     g a b c d^\markup \italic "Yeah"
    }
  }
  \new Staff {
    \relative c'' {
     c4 a d e
    }
  }
  >>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
