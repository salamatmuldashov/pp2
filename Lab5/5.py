import re
pattern = "arfsdfrrcat123435dog"
a = re.search('.+cat\d{2,}dog$',pattern) # /d
if a:
    print("yes")
else:
    print("no")


