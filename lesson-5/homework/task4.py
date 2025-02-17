def enrollment_stats(lst):
    total_students=sum([raw[1] for raw in lst])
    total_fee=sum([raw[2] for raw in lst])
    print(f'Total students: {total_students}')
    print(f'Total tuition: $ {total_fee}')

def mean(lst):
    student_mean=sum([raw[1] for raw in lst])/len(lst)
    fee_mean=sum([raw[2] for raw in lst])/len(lst)
    print(f'Student mean: {round(student_mean,2)}')
    print(f'Tuition mean: $ {round(fee_mean,2)}')

def median(lst):
    students=sorted([raw[1] for raw in lst])
    fees=sorted([raw[2] for raw in lst])
    if len(lst)%2 == 0:
       student_median=(students[int(len(lst)/2-1)] + students[int(len(lst)/2)]) /2
       fee_median=(fees[int(len(lst)/2-1)] + fees[int(len(lst)/2)]) /2
    else:
        student_median=students[int((len(lst)-1)/2)]
        fee_median=fees[int((len(lst)-1)/2)]
    print(f'Student median: {round(student_median,2)}')
    print(f'Tuition median: $ {round(fee_median,2)}')

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollment_stats(universities)
mean(universities)
median(universities)