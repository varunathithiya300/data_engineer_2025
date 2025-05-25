# A = [1,2,3]
# B = [6,5,4]
# C = [7,8,9]
# X = [A] + [B] + [C]

# print(X)
# print(list(zip(*X)))

subjects, students = map(int, input().split())
marks = []
for subject in range(subjects):
    for student in range(students):
        marks.extend([map(float, input().split())])

print(marks)