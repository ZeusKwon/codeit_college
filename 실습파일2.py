import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
df['room assignment'] = 'not assinged'
stu_numlist = df['course name'].value_counts()
auditorium = list(stu_numlist[stu_numlist >= 80].index)

for course in auditorium:
    df.loc[df['course name'] == course, 'room assignment'] = 'Auditorium'
large_room = list(stu_numlist[(stu_numlist <80) & (stu_numlist >= 40)].index)
for course in large_room:
    df.loc[df['course name'] == course, 'room assignment'] = 'Large room'
medium_room = list(stu_numlist[(stu_numlist < 40) & (stu_numlist >= 15)].index)
medium_room
for course in medium_room:
    df.loc[df['course name'] == course, 'room assignment'] = 'Medium room'

small_room = list(stu_numlist[(stu_numlist < 15) & (stu_numlist >= 5)].index)
for course in small_room:
    df.loc[df['course name'] == course, 'room assignment'] = 'Small room'
df.loc[df['status'] == 'not allowed','room assignment'] = 'not assigned'
# 정답 출력
df