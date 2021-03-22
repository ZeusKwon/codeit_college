# codeit_college

## 실습과제 1

2,000명의 코드잇 대학교 학생들이 수강신청을 했습니다.
수강신청에는 다음 3개의 조건이 있습니다.

1. “information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
2. “commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
3. 수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.

기존 DataFrame에 “status”라는 이름의 column을 추가하고, 학생이 수강 가능한 상태이면
“allowed”, 수강 불가능한 상태이면 “not allowed”를 넣어주세요.
-  -  -
## 실습과제 2

수강 신청이 완료되었습니다. 이제 각 과목을 수강하는 학생수에 따라 크기가 다른 강의실을 배치하려고 합니다.
강의실은 규모에 따라 “Auditorium”, “Large room”, “Medium room”, “Small room” 총 4가지 종류가 있습니다.
아래 조건에 따라 강의실 종류를 지정해 주세요.

1. 80명 이상의 학생이 수강하는 과목은 "Auditorium"에서 진행됩니다.
2. 40명 이상, 80명 미만의 학생이 수강하는 과목은 "Large room"에서 진행됩니다.
3. 15명 이상, 40명 미만의 학생이 수강하는 과목은 "Medium room"에서 진행됩니다.
4. 5명 이상, 15명 미만의 학생이 수강하는 과목은 "Samll room"에서 진행됩니다.
5. 폐강 등의 이유로 Status가 "not allowed"인 수강생은 room assignment 또한 "not assigned"가 되어야 합니다.
-  -  -
## 실습과제 3

이전 과제에서 강의실 크기에 따라 “room assignment” column을 만들어 주었습니다.
이제 이 “room assignment”에 따라 강의실 이름을 붙여주려고 합니다.
아래 세 가지 조건을 만족하도록 코드를 작성하세요.

1. 같은 크기의 강의실이 필요한 과목에 대해 알파벳 순서대로 방 번호를 배정하세요.
예를 들어 Auditorium이 필요한 과목으로 “arts”, “commerce”, “science” 세 과목이 있다면, “arts”는 “Auditorium-1”, “commerce”는 “Auditorium-2”, “science”는 “Auditorium-3” 순서로 방 배정이 되어야 합니다.
2. “status” column이 “not allowed”인 수강생은 “room assignment” column을 그대로 “not assigned”로 남겨둡니다.
3. “room assignment” column의 이름을 “room number”로 바꿔주세요.
