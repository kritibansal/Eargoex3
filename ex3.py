# function to calculate the maximum profit after buying and selling
def maxProfit(prices):                                       
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1: return 0             
    low = prices[0]           # buying day
    maxprofit = 0             # variabe maximum profit
    for i in range(len(prices)):    #loop 
        if prices[i] < low: low = prices[i] #condition
        maxprofit = max(maxprofit, prices[i] - low)  #calcualte maxprofit
    return 'total profit is :%d' %maxprofit, 'buying day is: %d' %int(prices.index(low)+1) , 'selling day is : %d' %int(prices.index(low+maxprofit)+1)

# In[ ]:
