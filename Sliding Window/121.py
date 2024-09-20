def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy_price = prices[0]
    sell_price = 0
    buy_price_idx = 0

    # Only need to return maxprofit
    for index, price in enumerate(prices):
        if price < buy_price:
            buy_price = price
            buy_price_idx = index
        else:
            if price > sell_price and index > buy_price_idx:
                sell_price = price

    return max(0, sell_price - buy_price)

maxProfit([4, 1, 5, 2, 7])
    