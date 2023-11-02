prices={"eggs":2.30,
        "steak":13.50,
        "bacon":2.30,
        "beer":14.9}



student={
    "name":"tejas",
    "age":18,
    "grade":"A"
}
name=student["name"]
age=student["age"]
student["age"]=19
student["city"]="kanpur"
print(student)
print(name)
student["course"]="btech"
for key,value in student.items():
     print(f"{key}:{value}")
if "age" in student:
    print("age exist in the dictionary")
student["course"]="btech"
for value in student.values():
     print(f"{value}")
del student["grade"]
print(student)
phone=student.get("phone","N/A")
print(phone)

dictionary={0:10,
            1:20   
}
print(dictionary)
dictionary[2]=20
dictionary[3]=30
print(dictionary)



dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)