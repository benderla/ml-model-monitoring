import pandas as pd
from scipy.stats import ks_2samp


def detect_feature_drift(train_feature, prod_feature):

    stat, p_value = ks_2samp(train_feature, prod_feature)

    return p_value

