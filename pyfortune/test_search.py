import search

s = search.Search("user", "pass", group = "日向坂", number = "2")
data = s.search(member = "潮　紗理菜") #性、名の間全角スペース
print(data)