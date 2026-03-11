DRIFT_THRESHOLD = 0.05

def check_drift(p_value):

    if p_value < DRIFT_THRESHOLD:
        return "drift detected"
    else:
        return "no drift"
