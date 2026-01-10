========
wem2ogg
========

.. start short_desc

**Convert Wwise WEM files to OGG.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/wem2ogg/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/wem2ogg/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/wem2ogg/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/wem2ogg/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/wem2ogg/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/wem2ogg/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/wem2ogg/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/wem2ogg/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/wem2ogg/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/wem2ogg/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/wem2ogg/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/wem2ogg?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/wem2ogg?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/wem2ogg
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/wem2ogg
	:target: https://pypi.org/project/wem2ogg/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/wem2ogg?logo=python&logoColor=white
	:target: https://pypi.org/project/wem2ogg/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/wem2ogg
	:target: https://pypi.org/project/wem2ogg/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/wem2ogg
	:target: https://pypi.org/project/wem2ogg/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/wem2ogg
	:target: https://github.com/domdfcoding/wem2ogg/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/wem2ogg
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/wem2ogg/v0.2.0
	:target: https://github.com/domdfcoding/wem2ogg/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/wem2ogg
	:target: https://github.com/domdfcoding/wem2ogg/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2026
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/wem2ogg
	:target: https://pypistats.org/packages/wem2ogg
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``wem2ogg`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install wem2ogg

.. end installation

Usage
--------------

``wem2ogg`` provides a single function, ``wem_to_ogg``.

.. code-block:: python

	def wem_to_ogg(wem_data: bytes) -> bytes: ...

The function takes the contents of a Wwise ``.wem`` file,
and returns the contents of a ``.ogg`` file for the same audio.
