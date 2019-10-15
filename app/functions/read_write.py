def dict_to_list(data):
    list_of_data = []
    if(data):
        for key in data:
            list_of_data.append(data[key])
        return(list_of_data)
    else:
        print("Data is empty. Cannot convert to list!")