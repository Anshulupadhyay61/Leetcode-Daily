class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = []
        i = 0
        j = i+1
        for i in range (len(prices)):
            found = False
            for j in range (i+1,len(prices)):
                if prices[i] >= prices[j]:
                    discount.append(prices[i]-prices[j])
                    found = True
                    break 
            if found == False:
                discount.append(prices[i])
        return discount