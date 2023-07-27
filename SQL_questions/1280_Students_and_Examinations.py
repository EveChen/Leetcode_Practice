
https://leetcode.com/problems/students-and-examinations/description/

# Solution 1 - Left join 招數
# Select st.student_id, st.student_name, s.subject_name, Count(e.subject_name) As attended_exams
# From Students st
#     Join Subjects s
#     Left Join Examinations e # 關鍵的一步
#     On st.student_id = e.student_id And e.subject_name = s.subject_name
# Group By st.student_id, st.student_name, s.subject_name
# order by st.student_id, s.subject_name


# Solution 2 - Cross Join (This operation combines each student with every subject, generating all possible combinations.)
Select st.student_id, st.student_name, s.subject_name, Count(e.subject_name) As attended_exams
From Students st
    Cross Join Subjects s
    Left Join Examinations e
    On e.student_id = st.student_id And e.subject_name = s.subject_name
Group By st.student_id, st.student_name, s.subject_name
Order By st.student_id, s.subject_name



# Trial 1 - wrong 難點在如何在學生沒有參與考試的情況下將count寫入0?
# Select st.student_id, st.student_name, e.subject_name, Count(e.subject_name) As attended_exams
# From Students st
#     Left Join Examinations e 
#         On st.student_id = e.student_id
#     Join Subjects s 
#         On e.subject_name = s.subject_name
# Group By st.student_id, st.student_name, e.subject_name


