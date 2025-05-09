def bai1():
    my_tuple = (1,2,4,4,5,6,6,7) #to create a tuple of numbers and print one item.
    a, b, *c = my_tuple  #to unpack a tuple into several variables.
    print(a,b,c) 
    my_list = list(my_tuple)
    my_list.append(8)
    my_tuple = tuple(my_list)
    print(my_tuple)  #to add an item to a tuple.
    print(my_tuple.index(6))
    seperated = list()
    for i in my_tuple:
        if my_tuple.count(i) > 1:
            seperated.append(i)
    seperatedd = set(seperated)
    print(seperatedd)

def bai2():
    friends = {1,2,3,4}
    friends2 = {1,2,3,4,5}
    sentences = ["I love Python", "Python is great", "I love coding"]
    print(max(friends))
    print(min(friends))
    print(1 in friends)
    if friends & friends2:
        print("Có phần tử chung")
    else:
        print("Không có phần tử chung")
    
    listt = []
    for i in sentences:
        word = i.split()
        listt.extend(word)
    
    all_words = set(listt)
    for i in all_words:
        x = listt.count(i)
        print(f"Từ {i} xuất hiện  {x} lần")
    
    missing_in_set2 = friends - friends2
    missing_in_set1 = friends2 - friends

    print(f"set2 bị thiếu {missing_in_set2}")
    print(f"set1 bị thiếu {missing_in_set1}")

def bai3():
    # 1. Convert two lists into a dictionary
    keys = ["name", "age", "city"]
    values = ["John", 28, "TPHCM"]
    my_dictionary = dict(zip(keys,values))
    print(my_dictionary)


    # 2.Merge two Python dictionaries into one
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    copy = dict1.copy()
    copy.update(dict2)
    print(copy)

    my_dict = {
        "name" : "Lucy",
        "subjects" :
        {
            "math" : 80,
            "history" : 50
        } 
}
    print(my_dict["subjects"]["history"])


    employees = ["Alice", "Bob", "Charlie"]





employees = ["Alice", "Bob", "Charlie"]
employee_dict = {}

for name in employees:
    employee_dict[name] = {"role": "staff", "active": True}  # mỗi người 1 bản riêng

print(employee_dict)








# Dictionary ban đầu
original_dict = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female',
    'country': 'Vietnam',
    'email': 'alice@example.com'
}

# Các key muốn trích ra
keys_to_extract = ['name', 'email']

# Tạo dictionary mới chỉ với những key trên
new_dict = {}

for key in keys_to_extract:
    if key in original_dict:
        new_dict[key] = original_dict[key]

# In ra dictionary mới
print("Dictionary mới sau khi trích các key cần thiết là:")
print(new_dict)











# Từ điển ban đầu
my_dict = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female',
    'country': 'Vietnam'
}

# Danh sách các key cần xóa
keys_to_delete = ['age', 'gender']

# Duyệt từng key trong danh sách và xóa khỏi dict nếu tồn tại
for key in keys_to_delete:
    if key in my_dict:
        del my_dict[key]  # hoặc: my_dict.pop(key)

# In ra kết quả
print(my_dict)










my_dict = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female',
    'country': 'Vietnam'
}

# Kiểm tra giá trị có tồn tại không
value_to_check = 'Alice'

if value_to_check in my_dict.values():
    print(f"Giá trị '{value_to_check}' tồn tại trong dictionary.")
else:
    print(f"Giá trị '{value_to_check}' không tồn tại trong dictionary.")











my_dict = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female',
    'country': 'Vietnam'
}

# Đổi tên key 'name' thành 'first_name'
if 'name' in my_dict:
    my_dict['first_name'] = my_dict.pop('name')

# In ra dictionary sau khi đổi tên key
print(my_dict)











scores = {
    'Alice': 88,
    'Bob': 95,
    'Charlie': 70,
    'David': 85
}


# Tìm key có giá trị nhỏ nhất
min_key = min(scores, key=scores.get)

print(f"Người có điểm thấp nhất là: {min_key} với điểm {scores[min_key]}")








student = {
    "name": "Alice",
    "grades": {
        "math": 85,
        "english": 90
    }
}
student["grades"]["math"] = 95
print(student)










text = "Hello, how are you doing today?"

# B1: Tạo dictionary rỗng để lưu tần suất xuất hiện
char_count = {}

# B2: Duyệt từng ký tự trong đoạn văn
for char in text:
    if char in char_count:
        char_count[char] += 1  # Nếu đã có thì tăng lên 1
    else:
        char_count[char] = 1   # Nếu chưa có thì gán bằng 1

# B3: In kết quả
for char, count in char_count.items():
    print(f"'{char}': {count}")











# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Tối ưu hóa kiểm tra
        if n % i == 0:
            return False
    return True

# Nhập giá trị N
N = 20

# Tìm các số nguyên tố < N
prime_numbers = []
for num in range(2, N):
    if is_prime(num):
        prime_numbers.append(num)

# Tạo dictionary với key bắt đầu từ 1
prime_dict = {}
for i in range(len(prime_numbers)):
    prime_dict[i + 1] = prime_numbers[i]

# In kết quả
print("Dictionary các số nguyên tố là:")
print(prime_dict)






# Dữ liệu nhân viên ban đầu (ID: thông tin)
employees = {
    1001: {'name': 'Alice', 'department': 'HR', 'salary': 50000},
    1002: {'name': 'Bob', 'department': 'IT', 'salary': 70000},
    1003: {'name': 'Charlie', 'department': 'HR', 'salary': 52000},
    1004: {'name': 'David', 'department': 'Finance', 'salary': 60000},
    1005: {'name': 'Eve', 'department': 'IT', 'salary': 75000}
}

# Tạo dictionary mới để nhóm theo phòng ban
dept_employees = {}

# Duyệt từng nhân viên trong employees
for emp_id, info in employees.items():
    department = info['department']  # Lấy tên phòng ban
    name = info['name']              # Lấy tên nhân viên
    salary = info['salary']          # Lấy lương

    # Nếu phòng ban chưa có trong dict thì tạo list mới
    if department not in dept_employees:
        dept_employees[department] = []

    # Thêm nhân viên vào danh sách phòng ban tương ứng
    dept_employees[department].append({'name': name, 'salary': salary})

# In ra kết quả
print("Danh sách nhân viên theo phòng ban:")
for dept, employees in dept_employees.items():
    print(f"- {dept}:")
    for emp in employees:
        print(f"   Tên: {emp['name']}, Lương: {emp['salary']}")



if __name__ == '__main__':
    bai3()