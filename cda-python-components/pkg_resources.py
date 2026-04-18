"""Minimal pkg_resources shim for this repo.

This is used only to satisfy legacy imports from pisense.
"""

import importlib
import os

from packaging.requirements import Requirement


class VersionConflict(Exception):
    """Raised when an installed package does not meet the required version."""
    pass


class DistributionNotFound(Exception):
    """Raised when a required package cannot be imported."""
    pass


def require(requirement):
    if not isinstance(requirement, str):
        raise TypeError('require() expects a string requirement')

    req = Requirement(requirement)
    module_name = req.name

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as ex:
        raise DistributionNotFound(str(ex)) from ex

    version = getattr(module, '__version__', None)
    if version is None:
        return [module]

    if req.specifier and not req.specifier.contains(version, prereleases=True):
        raise VersionConflict(
            f'{module_name} {version} does not satisfy {req.specifier}',
        )

    return [module]


def resource_filename(package_or_requirement, resource_name):
    if isinstance(package_or_requirement, str):
        package_name = package_or_requirement
    else:
        package_name = package_or_requirement.__name__

    package_name = package_name.split('.')[0]
    try:
        package = importlib.import_module(package_name)
    except ModuleNotFoundError as ex:
        raise DistributionNotFound(str(ex)) from ex

    package_path = os.path.dirname(package.__file__)
    resource_path = os.path.join(package_path, resource_name)
    if not os.path.exists(resource_path):
        raise FileNotFoundError(resource_name)
    return resource_path


def cleanup_resources():
    # This shim does not extract resources to temporary files, so nothing
    # needs to be cleaned up.
    return
