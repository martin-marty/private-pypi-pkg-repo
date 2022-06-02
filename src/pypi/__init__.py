try:
    from . import _version

    __version__ = _version.version
except ImportError:
    # package is not installed
    __version__ = "0.0.0"
    pass
