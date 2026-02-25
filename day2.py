# fee calculator

def calculate_fee(course, marks):

    # course fee
    if course == "DS":
        fee = 40000

    elif course == "WD":
        fee = 30000

    elif course == "AI":
        fee = 20000

    else:
        return "Course not found"

    # discount based on marks
    if marks > 90:
        discount = 5000

    elif 80 <= marks <= 90:
        discount = 2000

    elif 60 <= marks < 80:
        discount = 1000

    else:
        discount = 0

    final_fee = fee - discount
    return final_fee


# calling function
course = input("Enter Course (DS/WD/AI): ")
marks = int(input("Enter Marks: "))

result = calculate_fee(course, marks)

print("Final Fee:", result)
