#1.) 
truck = "toyota tacoma"
make_and_model = truck.split()
make = make_and_model[0]
model = make_and_model[1]
truck = {
    "make": make,
    "model": model
}
print(truck)

#2.) 
truck = "toyota tacoma"
make_and_model = truck.split()
make = make_and_model[0].title()
model = make_and_model[1].title()
truck = {
    "make": make,
    "model": model
}
print(truck)

truck = {
    "make": make,
    "model": model
}

truck["make"] = truck["make"].title() 
truck["model"] = truck["model"].title()
print(truck)


#3.) 
trucks = [
  {  "make": "Toyota",
    "model": "Tacoma"
},
{   "make": "Mazda",
    "model": "RX7"

},
{   "make": "Toyota",
    "model": "MR2"
}
]

truck = trucks[0]
print(truck)

truck["make"] = truck["make"].upper()
truck["model"] = truck["model"].upper()
print(truck)

for truck in trucks:
    truck["make"] = truck["make"].upper()
    truck["model"] = truck["model"].upper()

print(trucks)