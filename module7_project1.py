last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics','calculus','poetry','history']
grades = [98,97,85,88]
subjects.append('computer science')
subjects.append('visual arts')
grades.append(100)
grades.append(93)
gradebook = zip(subjects,grades)
print(list(gradebook))
full_gradebook = gradebook + last_semester_gradebook 
