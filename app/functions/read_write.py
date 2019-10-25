def dict_to_list(data):
    list_of_data = []
    keys = []
    if(data):
        for key in data:
            keys.append(key)
        for key in data:
            list_of_data.append(data[key])
        return(list_of_data, keys)
    else:
        print("Data is empty. Cannot convert to list!")