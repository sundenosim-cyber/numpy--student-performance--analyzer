import matplotlib.pyplot as plt
import numpy as np
import csv
Name = ('nosim', 'dori', 'milly', 'bobby', 'gabuh')
Subjects = ("Maths", "English", "Excel","Python"),
Marks = np.array ([
    [90, 80, 70, 67],
    [78, 89, 78, 67],
    [78, 67, 56, 54],
    [67, 78, 56, 45],
    [95, 76, 87, 45]
])
print (Marks)
print (Name)
print(Subjects)
Subjects_avarages = np.mean(Marks, axis = 0)
print("AVARAGES MARKS PER SUBJECT:")
for i in range(len(Subjects)):
    print(Subjects[i], Subjects_avarages[i])
print("mean:", np.mean(Marks))
print(np.mean(Marks,axis = 1)) # avrg of each student
print(np.sum(Marks,axis = 1)) #sum of each student
print("Maximum Marks for eachh student:")
print(np.max(Marks, axis=1))
print("Minimum marks for each student:")
print(np.min(Marks, axis=1)) #axis works across each student
subject_avarages = np.mean(Marks,axis=0)
student_avarages = np.mean(Marks, axis=1)

print("AVARAGE MARKS PER STUDENT:")
print(student_avarages)
print("AVARAGE MARKS PER SUBJECT:")
print(subject_avarages)


top_index = np.argmax(subject_avarages) #argmax the position index of the highest value
print("Top-performing subject:", Subjects[top_index])
print("Highest average:",subject_avarages[top_index])
#ranking 
ranking = np.argsort(subject_avarages)[::-1]
print ("student ranking:")
student_avarages = np.mean(Marks,axis=1)
top_index = np.argmax(student_avarages)
    
print("top performing student:",
      Name[top_index])
print("Highest avareges:",
      student_avarages[top_index])
#student ranking
ranking = np.argsort(student_avarages)[::-1]
print("student ranking:")
for i in ranking:
    print(Name[i], student_avarages[i])
    pass_marks = 76
    print("PASS AND FAIL ANALYSIS:")
    for i in range(len(Name)):
        if student_avarages[i] >= pass_marks:
            print(Name[i], "PASS")
        else:
            print(Name[i], "FAIL")
            passed = np.sum(subject_avarages >= pass_marks)
failed = len(Name) - passed
pass_rate = (passed / len(Name)) * 100
print("Number passed:", passed)
print("Number failed:", failed)
print("pass rate:", pass_rate, "%")
print("STUDENT GRADES:")
print("Subject perfomannce comparison:")
highest = np.argmax(Subjects_avarages)
lowest = np.argmin(Subjects_avarages)

print("Best performing Subject:", Subjects[0][highest])
print("lowest avarages:", Subjects_avarages[lowest])

plt.bar(Name, student_avarages)

plt.title("Student perfomance Analysis")
plt.xlabel("Student Names")
plt.ylabel("Avarage Marks")

plt.grid(axis="y")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
print("GRAPH CLOSED")
print("STARTING CSV EXPORT")
with open("student_performance.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name"] + list(Subjects))

    for i in range(len(Name)):
        writer.writerow([Name[i]] + list(Marks[i]))

print("CSV file saved successfully!")
print("CSV EXPORT COMPLETED")