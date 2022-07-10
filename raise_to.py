def raise_to(exp):
    def raise_to_exp(num):
        return pow(num, exp)

    return raise_to_exp
