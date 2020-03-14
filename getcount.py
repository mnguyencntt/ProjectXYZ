count = 0
with open("index.html", "r") as f:
  for line in f:
    count += 1
print('%s' % str(count))
