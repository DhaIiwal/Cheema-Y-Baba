# fruits = ["Apple", "Orange", "Pear"]
#
# for fruit in fruits:
#     print(fruit)
#     print(fruit, "pie")
#
# for number in range (1, 51):
#     print(number)
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)

low_score = 199
for score in student_scores:
    if score < low_score:
        low_score = score
print(low_score)
total =  [150 + 142 + 185 + 120 + 171 + 184 + 149 + 24 + 59 + 68 + 199 + 78 + 65 + 89 + 86 + 55 + 91 + 64 + 89]
print(total)

