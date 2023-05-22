gradeOne = float(input('Grade 1: '))
gradeTwo = float(input('Grade 2: '))
gradeThree = float(input('Grade 3: '))
gradeFour = float(input('Grade 4: '))


def academic_average(grade1, grade2, grade3, grade4):
    return (grade1 + grade2 + grade3 + grade4) / 4


result = academic_average(gradeOne, gradeTwo, gradeThree, gradeFour)

print('Your school grade is: {}'.format(result))
