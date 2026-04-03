# TESLA-Obstacle-Avoidance
Aim
To implement a reactive rule for obstacle avoidance.
General Objective
To study reactive obstacle avoidance strategies and how proximity-based sensor data enables safe navigation in autonomous systems.
Specific Objective
To apply the rule:
Obstacle Distance = 0.25 m
Threshold = 0.3 m
If distance < threshold → Turn Right
Dataset
CARLA Simulator
Source: CARLA Simulator
Procedure
Input obstacle distance
Define safe threshold
Compare distance with threshold
If distance < threshold → Turn Right
Display result
Algorithm
Start
Input obstacle distance
Set threshold
If distance < threshold → Turn Right
Else → Move Forward
Display result
Stop
Code Logic
if distance < threshold:
    action = "Turn Right"
Python Code
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
Output
Turn Right

Program Executed Successfully
Result
Since the obstacle is within unsafe distance:
Turn Right action is executed.
Industry Application
Obstacle avoidance is used in:
Self-driving cars
Robotics navigation
Drones
Autonomous systems
Companies like Tesla, Inc. use this in:
Autopilot systems
Real-time navigation
Collision avoidance systems
Conclusion
Reactive obstacle avoidance ensures immediate safety by responding to nearby obstacles, making it critical for autonomous navigation systems.
