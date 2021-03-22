import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

auditorium = list(course_counts[course_counts >= 80].index)
auditorium.sort()
a = 1
for course in auditorium:
    df.loc[(df['course name'] == course) & allowed, 'room assignment'] = 'Auditorium-{0}'.format(a)
    a += 1

large_room = list(course_counts[(course_counts <80) & (course_counts >= 40)].index)
large_room.sort()
a = 1
for course in large_room:
    df.loc[(df['course name'] == course) & allowed, 'room assignment'] = 'Large-{0}'.format(a)
    a += 1
medium_room = list(course_counts[(course_counts < 40) & (course_counts >= 15)].index)
medium_room.sort()
a = 1
for course in medium_room:
    df.loc[(df['course name'] == course) & allowed, 'room assignment'] = 'Medium-{0}'.format(a)
    a += 1
small_room = list(course_counts[(course_counts < 15) & (course_counts >= 5)].index)
small_room.sort()
a = 1
for course in small_room:
    df.loc[(df['course name'] == course) & allowed, 'room assignment'] = 'Small-{0}'.format(a)
    a += 1
df.loc[df['status'] == 'not allowed','room assignment'] = 'not assigned'
df.rename(columns = {'room assignment' : 'room number'}, inplace = True)

# 정답 출력
df