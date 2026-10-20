# 普通文本
def write_common_text():
    with open("C:/Users/muyijt0/Desktop/a.txt", "a", encoding="utf-8") as f:
        f.write("你好")
write_common_text()

#####################################################################################
# csv文本
import csv

## 写入列表
data = [["id", "name"], [1, "Alice"], [2, "Bob"], [3, "Charlie"]]
with open("C:/Users/muyijt0/Desktop/student_list.csv", "a", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

## 写入字典
rows = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
with open("C:/Users/muyijt0/Desktop/student_dict.csv", "a", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name"])
    writer.writeheader()
    writer.writerows(rows)
