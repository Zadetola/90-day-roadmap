def check_strength(password):
    if len(password) >= 8:
        return 'Strong'
    else:
        return 'Weak'