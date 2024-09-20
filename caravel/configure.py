##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
This module provides tools to check that all the dependencies are installed
properly.
"""


# Imports
from .info import __version__
from .info import LICENSE
from .info import AUTHOR


def logo():
    """ pySAP logo is ascii art using fender font.

    Returns
    -------
    logo: str
        the pysap logo.
    """
    logo = r"""
   _ __    _  _                                                     _
  | '_ \  | || |   __     __ _      _ _   __ _    __ __    ___     | |
  | .__/   \_, |  / _|   / _` |    | '_| / _` |   \ V /   / -_)    | |
  |_|__   _|__/   \__|_  \__,_|   _|_|_  \__,_|   _\_/_   \___|   _|_|
_|'''''|_| ''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|_|'''''|
'`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-''`-0-0-'
    """
    return logo


def info():
    """ Dispaly some usefull information about the package.

    Returns
    -------
    info: str
        package information.
    """
    version = "Package version: {0}\n\n".format(__version__)
    license = "License: {0}\n\n".format(LICENSE)
    authors = "Authors: \n{0}\n".format(AUTHOR)
    return logo() + "\n\n" + version + license + authors
