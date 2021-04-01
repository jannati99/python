studentid={
    "101" : "anisul islam",
    "102" : "jannatul",
    "103" : "fatema"
}
print(studentid["101"])
print(studentid.get("101"))
print(studentid.get("106","not a valid key"))
print(studentid.get("107"))
print(studentid.get("103","not a valid key"))
#using as a integer
student={
    101 : "jannatul"
}
print(student.get(101))