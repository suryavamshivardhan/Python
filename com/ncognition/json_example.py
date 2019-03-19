import json
def json_example():
    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }

    #write json to a file
    with open('C:/MyDocs/Training/Python/WorkSpace/resources/input','w') as input_file:
        json.dump(x,input_file)

    #write json to string
    json_string = json.dumps(x)
    #print('json data after reading after serialization',json_string)

    #read json data from file
    with open('C:/MyDocs/Training/Python/WorkSpace/resources/input','r') as input_file:
        data = json.load(input_file)
    #print('json data after loading from file : ',data)

    #read json from string
    data = json.loads(json_string)
    #print('json data after deserialization : ',data)

    #data access from json objects
    for key in data:
        print(key,' - ',data[key])
        if key == 'cars':
            counter = 0
            for car in data[key]:
                counter+=1
                print('The car model{0} is : '.format(counter) , car['model'])
            print('The total number of cars are : ',counter)

json_example()