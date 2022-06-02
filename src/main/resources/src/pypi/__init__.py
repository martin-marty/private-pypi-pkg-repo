try:
    from . import _version

    __version__ = _version.version
except ImportError:
    # package is not installed
    import importlib_metadata
    __version__ = importlib_metadata.version("{$python_package}")
    pass
