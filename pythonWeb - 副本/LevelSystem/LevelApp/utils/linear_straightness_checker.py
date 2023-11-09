from loguru import logger


def calculate_straightness_error(an_values, B):
    n = len(an_values)

    # 计算折线纵坐标总值
    total_sum = sum(an_values)

    # 计算首尾线各点的纵坐标值
    line_values = [total_sum * (i / n) for i in range(1, n + 1)]

    # 初始化折线纵坐标值列表
    broken_line_values = []

    # 计算折线纵坐标值
    for i in range(n):
        if i == 0:
            broken_line_values.append(an_values[i])
        else:
            broken_line_values.append(an_values[i] + broken_line_values[i - 1])

    # 计算折线各点的纵坐标值与首尾线各点的纵坐标差值
    delta_values = [broken_line_values[i] - line_values[i] for i in range(n)]

    # 查询纵坐标差值最大值、最小值
    max_delta = max(delta_values)
    min_delta = min(delta_values)

    # 直线度误差计算值
    S = abs(max_delta) + abs(min_delta)
    S = S * 0.02 / 1000 * B

    logger.info(f'本次计算的偏移数组为:{an_values},水平仪的长度为:{B},所计算的误差为:{S}')

    return S