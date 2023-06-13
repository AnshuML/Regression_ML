import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from  dataclasses import dataclass
import sys
import os
