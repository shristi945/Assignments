import simplejson as json

with open('foodyo_output.json', 'r') as fp:
    obj = json.load(fp)



def find_child(list_of_child):
    for child in list_of_child:
        if child['selected'] == 1:
            if len(child['children'])!=0:
                return find_child(child['children'])
            else:
                return

for recommendation in obj['body']['Recommendations']:
    print(recommendation['RestaurantName'])
    i = 2
    flag = 0
    for item in recommendation['menu']:
        if item['type'] == 'sectionheader':
            for child1 in item['children']:
                if child1['type'] == "item" and child1['selected'] == 1 :
                    for k in range(i):
                        print("-", end = "")
                    print(">", end = "")
                    print( child1['name'])
                    i = i+2
                    for child in child1['children']:
                        if child['selected'] == 1:
                            for k in range(i):
                                print("-", end = "")
                            print(">", end = "")
                            print(child['name'])
                            i = i+2
                            if len(child['children'])!=0:
                                find_child(child['children'])
                            else:
                                break
                            
                            
                    
                            
                                
