
class department:
    def __init__(number, selling, managment):
        number.selling = selling
        number.managment = managment

d1 = department("Flooring", "Daniel")

print(d1.selling)
print(d1.managment)

class Associate(department):
    name = "Lucas"
    age = 19

print(Associate.name)
