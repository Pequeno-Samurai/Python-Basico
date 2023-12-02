#string slicing

name = "Rafael Raniere"

first_name = name[:6]
last_name = name[7:]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(reversed_name)

website1 = "https://www.google.com"
website2 = "https://www.wikipedia.com"

slice = slice(12,-4)

print(website1[slice])
print(website2[slice])
