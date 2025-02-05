from decode.data import build_dataset
from decode.logger import logger

import jax
import jax.numpy as jnp
import flax.linen as nn
from flax.training import train_state
import flax.linen.attention as attention
import numpy as np
import optax


class Decode(nn.Module):

    @nn.compact
    def __call__(self, x):
        x = nn.Dense(1024)(x)
        x = nn.relu(x)
        x = nn.Dense(1024)(x)
        x = nn.relu(x)
        return x


if __name__ == "__main__":
    dataset = build_dataset()
    print(dataset)
