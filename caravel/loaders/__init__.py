##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
This module defines common loaders for imaging-genetic datasets.
"""

from ._csv import CSV
from ._dwi import DWI
from ._edf import EDF
from ._json import JSON
from ._mp4 import MP4
from ._mzml import MZML
from ._nifti import NIFTI
from ._pdf import PDF
from ._plink import PLINK
from ._png import PNG
from ._targz import TARGZ
from ._tsv import TSV
from ._vcf import VCF
from ._xlsx import XLSX
