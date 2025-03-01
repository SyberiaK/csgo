| |license| |docs|

Supports Python ``3.9+``.

Module based on `steam <https://github.com/ValvePython/steam/>`_
for interacting with CS2's Game Coordinator.

Forked from `ValvePython/csgo <https://github.com/ValvePython/csgo/>`_ since it seems to be abandoned.

I'm not willing to maintain it but here's some updates I've made:

- Fixed connecting to GC
- Added constants for ``CSGOClient`` events (``EVENT_CONNECTION_STATUS``, ``EVENT_READY``, ``EVENT_NOT_READY``)
- Now the minimal Python requirement is 3.9 (since older version have reached their EOL)

**Documentation**: http://csgo.readthedocs.io (outdated)

| Note that this module should be considered an alpha.
| Contributions and suggestion are always welcome.


Installation
------------

Install the current dev version from ``github``::

    pip install git+https://github.com/SyberiaK/csgo


.. |license| image:: https://img.shields.io/pypi/l/csgo.svg?style=flat&label=license
    :target: https://github.com/SyberiaK/csgo/blob/master/LICENSE
    :alt: MIT License

.. |docs| image:: https://readthedocs.org/projects/csgo/badge/?version=latest
    :target: http://csgo.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation status
