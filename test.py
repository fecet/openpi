# %%

from pathlib import Path
from openpi.training import config as _config
from openpi.policies import policy_config
from openpi.shared import download

# %%

ckpt_dir = Path("/data/private/robot/pi05_droid_torch")
config = _config.get_config("pi05_droid")
print(config)
policy = policy_config.create_trained_policy(config, ckpt_dir)
print(policy)
