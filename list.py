timesteps = 32
nodes = 61803

list = []
count_ts = 1
while True:
    list1 = [count_ts] * nodes
    list.append(list1)
    count_ts += 1  # Replaces count = count + 1
    if count_ts > timesteps:
        break

print(list)
print(len(list))