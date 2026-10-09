from pathlib import Path

import numpy as np
import pandas as pd

import kagglehub

# Download into this project's data folder.
data_dir = Path(__file__).resolve().parent / "data"
path = kagglehub.competition_download(
    'nfl-big-data-bowl-2027',
    output_dir=str(data_dir),
)

print("Path to competition files:", path)
