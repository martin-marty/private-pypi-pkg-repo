try:
    from . import _version

    __version__ = _version.version
except ImportError:
    # package is not installed
    pass
