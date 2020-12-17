import math

def find_pyth_exponent(win_pct,scored,against):
    # solve for x where win_pct = (scored^x)/(scored^x + against^x)
    # in Wolfram Language: Reduce[w == s^x/(a^x + s^x), {x}]
    # scored = points for
    # against = points against (for opponents)
    x = math.log(1/win_pct - 1)/(math.log(against) - math.log(scored))
    return round(x.real,3)
    