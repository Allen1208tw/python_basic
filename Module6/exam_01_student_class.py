# 題目 1：學生類別 Student
#
# 請建立一個 Student 類別，用來管理學生資料與成績。
#
# 屬性：
# 1. name：學生姓名
# 2. student_id：學生學號
# 3. grades：成績 list
#
# 方法：
# 1. add_grade(grade)：新增一筆成績。
# 2. get_average()：回傳平均分數。
# 3. show_info()：印出學生姓名、學號、平均分數。
#
# 要求：
# 1. 使用 __init__ 初始化學生資料。
# 2. 建立至少一個 Student 物件。
# 3. 新增至少三筆成績。
# 4. 呼叫 show_info() 顯示學生資料。
#
# 提示：
# - 新增成績可以使用 self.grades.append(grade)。
# - 平均可以用 sum(self.grades) / len(self.grades)。
# - 如果 grades 是空 list，要避免除以 0。

