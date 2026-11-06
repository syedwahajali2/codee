import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"]
marks = [78, 92, 65, 88, 73]

average = sum(marks) / len(marks)
top_student = students[marks.index(max(marks))]

plt.figure(figsize=(8, 5))
plt.bar(students, marks)
plt.axhline(average, linestyle="--", label=f"Average: {average:.1f}")
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.savefig("student_performance.png")
plt.show()

print("Class average:", round(average, 2))
print("Top student:", top_student)
