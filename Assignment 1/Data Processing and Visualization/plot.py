import requests
import matplotlib.pyplot as plt
import random

API_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(API_URL)
data = response.json()

names = []
scores = []

# Generating random scores for students as scores are not provided
for user in data:
    names.append(user['name'])
    scores.append(random.randint(50, 100))

# Calculating average
average_score = sum(scores) / len(scores)
print("Average Score:", average_score)

# Graph plotting
plt.bar(names, scores)
plt.xticks(rotation=45)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Scores Visualization")

plt.tight_layout()
plt.show()