# -*- coding: utf-8 -*-
##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
Module that privides common networks.
"""


from .sononet import SonoNet
from .unet import UNet
from .vae import VUNet, VanillaNet
from .nvnet import NvNet
from .voxelmorphnet import VoxelMorphNet
from .vtnet import VTNet, ADDNet
from .rcnet import RCNet
from .brainnetcnn import BrainNetCNN
from .deeplabnet import DeepLabNet
from .pspnet import PSPNet
from .braingengan import (
    BGDiscriminator, BGEncoder, BGCodeDiscriminator, BGGenerator)
from .resnet import ResAENet
from .attention import STAAENet
from .deepcluster import DeepCluster
from .torchvisnet import *
