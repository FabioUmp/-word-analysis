from collections import Counter

def transform_dataset(data):
    qualified_students = {}
    subject_summary = Counter()
    for student in data:
        if all(grade > 70 for grade in student["grades"]):
            qualified_students[student["student_id"]] = round(sum(student["grades"]) / len(student["grades"]), 2)
            subject_summary += Counter(student["subjects"])
    return {'qualified_students': qualified_students, 'subject_summary': dict(subject_summary)}


data = [{"student_id": "S123", "grades": [88, 92, 85], "subjects": ["Math", "Science", "History"]}, {"student_id": "S124", "grades": [65, 95, 80], "subjects": ["Math", "Science", "English"]}, {"student_id": "S125", "grades": [91, 89, 92], "subjects": ["Math", "Physics", "History"]}]
print(transform_dataset(data))
