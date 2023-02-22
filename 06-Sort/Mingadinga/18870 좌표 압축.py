import sys
read = sys.stdin.readline

n = int(read())
points = list(map(int, read().split()))
result = []

unique_points = sorted(list(set(points)))

# 시간 초과
# for point in points:
#  result.append(unique_points.index(point))

unique_point_index = {}
for i in range(len(unique_points)):
  unique_point_index[unique_points[i]] = i

for point in points:
  print(unique_point_index[point], end = ' ')
