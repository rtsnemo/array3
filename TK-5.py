def get_squared_list(list_data):
    list_data[:] = [pow(element, 2) for element in list_data]
    return list_data