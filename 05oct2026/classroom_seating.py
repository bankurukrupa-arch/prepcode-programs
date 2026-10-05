students = int(input("enter the number of students:"))
benches_capacity = int(input("enter the number of benches:"))
complete_benches = students // benches_capacity
remaining_benches = students % benches_capacity
print("complete benches =",complete_benches)
print("remaining benches =",remaining_benches)