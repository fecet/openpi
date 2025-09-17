# %%

from pathlib import Path
from openpi.training import config as _config
from openpi.policies import policy_config_torch as policy_config
from openpi.shared import download
import torch

# %%

ckpt_dir = Path("/data/private/robot/pi05_droid_torch")
config = _config.get_config("pi05_droid")
with torch.device("cuda:0"):
    policy = policy_config.create_trained_policy(config, ckpt_dir, pytorch_device="cuda:0")

print(config)
print(policy)

# %%

config

# %%

from openpi.models_pytorch.pi0_pytorch import PI0Pytorch


# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
# %%
