import search

s = search.Search("username", "pass", group = "日向坂", number = None) 
data = s.search(member = "潮　紗理菜") #性、名の間全角スペース 
print(data)

sum_ = s.sum_sheets("潮　紗理菜")
print(sum_)