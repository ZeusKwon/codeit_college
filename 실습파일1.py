import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status'] = 'allowed'
# 1번문제
df_not = (df['year'] == 1) & (df['course name'] == 'information technology')
df.loc[df_not,'status'] = 'not allowed'

# # 2번문제
df_not = (df['year'] == 4) & (df['course name'] == 'commerce')
df.loc[df_not,'status'] = 'not allowed'

# 3번문제
course_counts = df['course name'].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
  df.loc[df["course name"] == course, "status"] = "not allowed"
# 정답 출력
df