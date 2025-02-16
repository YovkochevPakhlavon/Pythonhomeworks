universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
n=len(universities)

def enrollment_stats():
    return [[student,fee] for univ, student, fee in universities]
students=[enrollment_stats()[i][0] for i in range(n)]
fees=[enrollment_stats()[i][1] for i in range(n)]

def mean(a):
    return sum(a)/n
 
def median(a):
    a.sort()
    if n%2==0:
        median1=a[n//2]
        median2=a[n//2-1]
        return (median1+median2)/2
    else:
        return a[n//2]

print("Total students: ",sum(enrollment_stats()[i][0] for i in range(n)))
print("Total tuition: ",sum(enrollment_stats()[i][1] for i in range(n)))
print("__________")
print("Student mean: ", round(mean(students),2))
print("Student median: ", round(median(students),2))
print("__________")
print("Tuition mean: ", round(mean(fees),2))
print("Tuition median: ", round(median(fees),2))