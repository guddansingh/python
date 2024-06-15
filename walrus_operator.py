#this is an walrus operator that used to create loops 

#data = input("enter some data : ")
#while data:
    #print(data)
    #data = input("enter some data : ")

#while (data := input("enter some data : ")):
    #print(data) #this expression do the same work as above4

#this is an another example of the walrus expression
sample_data = [
	{"userId": 1, "name": "rahul", "completed": False},
	{"userId": 1, "name": "rohit", "completed": False},
	{"userId": 1, "name": "ram", "completed": False},
	{"userId": 1, "name": "ravan", "completed": True}
]

print("With Python 3.8 Walrus Operator:") 
for entry in sample_data: 
	if name := entry.get("name"):
		print(f'Found name: "{name}"')

print("Without Walrus operator:")
for entry in sample_data:
	name = entry.get("name")
	if name:
		print(f'Found name: "{name}"')
