import sys

rope_count = int(input())
ropes_weight = []

for i in range(rope_count):
    ropes_weight.append(int(input()))
ropes_weight.sort(reverse=True)

max_weight_per_rope = []
for j in range(rope_count):
    max_weight_per_rope.append(ropes_weight[j] * (j+1))

print(max(max_weight_per_rope))