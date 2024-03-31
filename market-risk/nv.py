import numpy as np
import math


def compute_nv(close_ratios: list) -> float:
    data = [math.log(x["t1"]/x["t0"]) for x in close_ratios]
    std_dev = np.std(data)
    # print("Normalized Volatility:", std_dev)
    return std_dev


def nv_usdt() -> float:
    # 2024/3/25
    # 104,578M
    # 34,589M
    cr = [
        {"t0": 1.00, "t1": 1.00},  # 1 week, 
        {"t0": 1.00, "t1": 1.00},  # 1 month,
        {"t0": 1.00, "t1": 1.00},  # 3 months,
        {"t0": 0.999862, "t1": 1.00},  # 6 months,
        {"t0": 1.00, "t1": 1.00},  # 1 year
    ]
    return compute_nv(cr)


def nv_usdc() -> float:
    # 2024/3/25
    # 32,448M
    # 4,573M
    cr = [
        {"t0": 1.00, "t1": 1.00},  # 1 week, 
        {"t0": 1.00, "t1": 1.00},  # 1 month,
        {"t0": 1.00, "t1": 1.00},  # 3 months,
        {"t0": 0.999965, "t1": 1.00},  # 6 months,
        {"t0": 1.00, "t1": 1.00},  # 1 year
    ]
    return compute_nv(cr)


def nv_dai() -> float:
    # 2024/3/25
    # 4,917M
    #   239M
    cr = [
        {"t0": 0.999197, "t1": 0.998911},  # 1 week, 
        {"t0": 0.998250, "t1": 0.998911},  # 1 month,
        {"t0": 0.998467, "t1": 0.998911},  # 3 months,
        {"t0": 0.999839, "t1": 0.998911},  # 6 months,
        {"t0": 1.00, "t1": 0.998911},  # 1 year
    ]
    return compute_nv(cr)


def nv_frax() -> float:
    # 2024/3/25
    # 647M
    # 5.486M
    cr = [
        {"t0": 0.997730, "t1": 0.997556},  # 1 week, 
        {"t0": 0.994715, "t1": 0.997556},  # 1 month,
        {"t0": 0.997169, "t1": 0.997556},  # 3 months,
        {"t0": 0.998317, "t1": 0.997556},  # 6 months,
        {"t0": 0.999855, "t1": 0.997556},  # 1 year
    ]
    return compute_nv(cr)


def nv_btc() -> float:
    # 2024/3/25
    # 1,385,231M
    #  17,295M
    cr = [
        {"t0": 63509.00, "t1": 69702.00},  # 1 week, 
        {"t0": 62068.00, "t1": 69702.00},  # 1 month,
        {"t0": 42221.00, "t1": 69702.00},  # 3 months,
        {"t0": 26917.00, "t1": 69702.00},  # 6 months,
        {"t0": 28043.00, "t1": 69702.00},  # 1 year
    ]
    return compute_nv(cr)


def nv_eth() -> float:
    # 2024/3/25
    # 433,812M
    #  10,778M
    cr = [
        {"t0": 3322.89, "t1": 3507.66},  # 1 week, 
        {"t0": 3421.89, "t1": 3507.66},  # 1 month,
        {"t0": 2294.34, "t1": 3507.66},  # 3 months,
        {"t0": 1667.99, "t1": 3507.66},  # 6 months,
        {"t0": 1872.25, "t1": 3507.66},  # 1 year
    ]
    return compute_nv(cr)


def nv_near() -> float:
    # 2024/3/25
    # 7,435M
    #   264M
    cr = [
        {"t0": 6.46, "t1": 6.95},  # 1 week, 
        {"t0": 4.45, "t1": 6.95},  # 1 month,
        {"t0": 3.67, "t1": 6.95},  # 3 months,
        {"t0": 1.12, "t1": 6.95},  # 6 months,
        {"t0": 1.99, "t1": 6.95},  # 1 year
    ]
    return compute_nv(cr)


def nv_woo() -> float:
    # 2024/3/25
    # 823M
    #  16M
    cr = [
        {"t0": 0.427146, "t1": 0.435257},  # 1 week, 
        {"t0": 0.543260, "t1": 0.435257},  # 1 month,
        {"t0": 0.417799, "t1": 0.435257},  # 3 months,
        {"t0": 0.171109, "t1": 0.435257},  # 6 months,
        {"t0": 0.213773, "t1": 0.435257},  # 1 year
    ]
    return compute_nv(cr)


def nv_aurora() -> float:
    # 2024/3/25
    # 168M
    #   1M
    cr = [
        {"t0": 0.392167, "t1": 0.371140},  # 1 week, 
        {"t0": 0.310026, "t1": 0.371140},  # 1 month,
        {"t0": 0.288464, "t1": 0.371140},  # 3 months,
        {"t0": 0.051002, "t1": 0.371140},  # 6 months,
        {"t0": 0.191150, "t1": 0.371140},  # 1 year
    ]
    return compute_nv(cr)


def nv_ref() -> float:
    # 2024/3/25
    # 15M
    # 0.08M
    cr = [
        {"t0": 0.345448, "t1": 0.465672},  # 1 week, 
        {"t0": 0.265102, "t1": 0.465672},  # 1 month,
        {"t0": 0.279394, "t1": 0.465672},  # 3 months,
        {"t0": 0.050750, "t1": 0.465672},  # 6 months,
        {"t0": 0.123471, "t1": 0.465672},  # 1 year
    ]
    return compute_nv(cr)


def nv_linear() -> float:
    # 2024/3/25
    cr = [
        {"t0": 7.74, "t1": 8.37},  # 1 week, 
        {"t0": 5.30, "t1": 8.37},  # 1 month,
        {"t0": 4.35, "t1": 8.37},  # 3 months,
        {"t0": 1.29, "t1": 8.37},  # 6 months,
        {"t0": 2.20, "t1": 8.37},  # 1 year
    ]
    return compute_nv(cr)


def nv_stnear() -> float:
    # 2024/3/25
    cr = [
        {"t0": 8.24, "t1": 8.89},  # 1 week, 
        {"t0": 5.64, "t1": 8.89},  # 1 month,
        {"t0": 4.62, "t1": 8.89},  # 3 months,
        {"t0": 1.38, "t1": 8.89},  # 6 months,
        {"t0": 2.34, "t1": 8.89},  # 1 year
    ]
    return compute_nv(cr)


if __name__=="__main__":
    # data = [1, 2, 3, 4, 5]
    # std_dev = np.std(data)
    # log_10 = math.log(10)
    # print("standard_deviation:", std_dev)
    print("Normalized Volatility (  usdc):", nv_usdc())
    print("Normalized Volatility (  usdt):", nv_usdt())
    print("Normalized Volatility (   dai):", nv_dai())
    print("Normalized Volatility (  frax):", nv_frax())
    print("Normalized Volatility (   btc):", nv_btc())
    print("Normalized Volatility (   eth):", nv_eth())
    print("Normalized Volatility (  near):", nv_near())
    print("Normalized Volatility (   woo):", nv_woo())
    print("Normalized Volatility (aurora):", nv_aurora())
    print("Normalized Volatility (   ref):", nv_ref())
    # print("Normalized Volatility (linear):", nv_linear())
    # print("Normalized Volatility (stnear):", nv_stnear())

    