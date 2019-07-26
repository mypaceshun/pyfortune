import search

s = search.Search("user", "pass", group = ["欅坂", "日向坂"], number = None) 
data = s.search(member = "潮　紗理菜") #性、名の間全角スペース 
#print(data)

sum_ = s.sum_sheets("潮　紗理菜")
#print(sum_)

output = s.past_member()
print(output)
