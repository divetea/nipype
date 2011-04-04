# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Camino top level namespace
"""

from nipype.interfaces.camino.connectivity import Conmap
from nipype.interfaces.camino.convert import Image2Voxel, FSL2Scheme, VtkStreamlines, ProcStreamlines, TractShredder
from nipype.interfaces.camino.dti import DTIFit, ModelFit, DTLUTGen, PicoPDFs, Track, TrackPICo, TrackBayesDirac, TrackDT, FA, MD, TrD, AnalyzeHeader
import nose


def setup():
    print 'camino setup test'

def teardown():
    print 'camino teardown test'
