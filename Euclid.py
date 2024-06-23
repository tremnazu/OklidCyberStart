import math

points = [(40, 2), (6, 21), (7, 6), (35, 53), (17, 10)]

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("Noktalar arasındaki mesafe:", distances)
print("Minimum mesafe:", min_distance)




