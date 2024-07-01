# 3. An e-commerce site tracks the purchases made each day. The product that is purchased
# the most one day is the featured product for the following day. If there is a tie for the product
# purchased most frequently, those product names are ordered alphabetically ascending and
# the last name in the list is chosen.[Amazon]
# ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
# 'greenPants', 'greenPants', 'greenPants']
# 'yellowShirt' - 2
# 'redHat' - 2
# 'blackShirt' - 2
# 'bluePants' - 1
# 'greenPants' - 3
# 'pinkHat' - 1
# Output - greenPants



def featuredProduct(arr):
    freq_purchase={}
    for i in arr:
        freq_purchase[i]=freq_purchase.get(i, 0)+1
    most_sales=float("-inf")
    for i in freq_purchase.values():
        if i>most_sales:
            most_sales=i
    def filterElements(item):
        key, value=item
        return value==most_sales
    res=dict(filter(filterElements,freq_purchase.items()))
    res=list(res.keys())
    res.sort()
    return res[len(res)-1]



purchase=['yellowShirt','yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
'greenPants', 'greenPants', 'greenPants']
res=featuredProduct(purchase)
print(res)