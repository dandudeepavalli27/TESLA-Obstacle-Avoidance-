# SESSION 28 – Obstacle Avoidance

# Step 1: Input values
distance = 0.25   # obstacle distance in meters
threshold = 0.3   # safe distance

# Step 2: Apply rule
if distance < threshold:
    print("Turn Right")
else:
    print("Move Forward")

print("\nProgram Executed Successfully")
