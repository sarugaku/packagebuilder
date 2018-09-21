===========================================================================================
packagebuilder: A library for building python packages into binary or source distributions.
===========================================================================================

.. image:: https://img.shields.io/pypi/v/packagebuilder.svg
    :target: https://pypi.org/project/packagebuilder

.. image:: https://img.shields.io/pypi/l/packagebuilder.svg
    :target: https://pypi.org/project/packagebuilder

.. image:: https://api.travis-ci.com/sarugaku/packagebuilder.svg?branch=master
    :target: https://travis-ci.com/sarugaku/packagebuilder

.. image:: https://ci.appveyor.com/api/projects/status/y9kpdaqy4di5nhyk/branch/master?svg=true
    :target: https://ci.appveyor.com/project/sarugaku/packagebuilder

.. image:: https://img.shields.io/pypi/pyversions/packagebuilder.svg
    :target: https://pypi.org/project/packagebuilder

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/techalchemy

.. image:: https://readthedocs.org/projects/packagebuilder/badge/?version=latest
    :target: https://packagebuilder.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Summary
=======

Packagebuilder_ is a library designed for building packages. It takes `InstallRequirement`
objects as inputs and first attempts to build a wheel, but falls back to producing a
source distribution if necessary. Invocation is straightforward:

  ::

    >>> import packagebuilder
    >>> import pip_shims
    >>> ireq = pip_shims.shims.InstallRequirement.from_line('vistir')
    >>> builder = packagebuilder.BuiltDist(ireq, sources=packagebuilder.get_sources())
    >>> dist = builder.build()
    >>> dist.metadata.run_requires
    ['requests', 'six', 'backports.weakref; python_version < "3.3"', 'backports.shutil-get-terminal-size; python_version < "3.3"', 'pathlib2; python_version < "3.5"', "yaspin; extra == 'spinner'", "pytest; extra == 'tests'", "pytest-xdist; extra == 'tests'", "pytest-cov; extra == 'tests'", "pytest-timeout; extra == 'tests'", "hypothesis-fspaths; extra == 'tests'", "hypothesis; extra == 'tests'"]

`Read the documentation <https://packagebuilder.readthedocs.io/>`__.
