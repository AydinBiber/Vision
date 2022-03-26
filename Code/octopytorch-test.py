from functools import partial
import torch
from torch import nn
import octopytorch as octo

module_bank = octo.DEFAULT_MODULE_BANK.copy()
module_bank[octo.ModuleType.DROPOUT] = partial(nn.Dropout2d, p=0.2, inplace=True)
module_bank[octo.ModuleType.ACTIVATION] = nn.GELU
module_bank[octo.ModuleType.ACTIVATION_FINAL] = partial(nn.LogSoftmax, dim=1)

model = octo.models.Tiramisu(
    in_channels = 3,          # RGB images
    out_channels = 5,         # 5-channel output (5 classes)
    init_conv_filters = 48,   # Number of channels outputted by the 1st convolution
    structure = (
        [4, 4, 4, 4, 4],      # Down blocks
        4,                    # bottleneck layers
        [4, 4, 4, 4, 4],      # Up blocks
    ),
    growth_rate = 12,         # Growth rate of the DenseLayers
    compression = 1.0,        # No compression
    early_transition = False, # No early transition
    include_top = True,       # Includes last layer and activation
    checkpoint = False,       # No memory checkpointing
    module_bank = module_bank # Modules to use
)

# Initializes all the convolutional kernel weights.
model.initialize_kernels(nn.init.kaiming_uniform_, conv=True)
# Shows some information about the model.
model.summary()