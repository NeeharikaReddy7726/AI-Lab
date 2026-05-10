import pandas as pd
import numpy as np

data = pd.read_csv("cities.csv")

points = data.values
print(points[:5]) 
def compute_ssd(points, centers, labels):
    ssd = 0
    for i in range(len(points)):
        center = centers[labels[i]]
        ssd += np.sum((points[i] - center) ** 2)
    return ssd

def gradient_descent(points, k=3, iterations=100):
    # random centers
    centers = points[np.random.choice(len(points), k, replace=False)]

    for _ in range(iterations):
        # assign clusters
        labels = []
        for p in points:
            distances = [np.linalg.norm(p - c) for c in centers]
            labels.append(np.argmin(distances))

        labels = np.array(labels)

        # update centers (mean)
        new_centers = []
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) > 0:
                new_centers.append(np.mean(cluster_points, axis=0))
            else:
                new_centers.append(centers[i])

        centers = np.array(new_centers)

    ssd = compute_ssd(points, centers, labels)
    return centers, labels, ssd

def newton_method(points, k=3, iterations=50):
    centers = points[np.random.choice(len(points), k, replace=False)]

    for _ in range(iterations):
        labels = []
        for p in points:
            distances = [np.linalg.norm(p - c) for c in centers]
            labels.append(np.argmin(distances))

        labels = np.array(labels)

        # Newton-like update
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) > 0:
                centers[i] = np.mean(cluster_points, axis=0)

    ssd = compute_ssd(points, centers, labels)
    return centers, labels, ssd

centers_gd, labels_gd, ssd_gd = gradient_descent(points)
centers_nm, labels_nm, ssd_nm = newton_method(points)

print("\n Gradient Descent ")
print("Centers:\n", centers_gd)
print("SSD:", ssd_gd)

print("\n Newton Method ")
print("Centers:\n", centers_nm)
print("SSD:", ssd_nm)