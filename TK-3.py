def get_divided_list(list_data):
    if len(list_data) > 0:
        average = float(sum(list_data)/len(list_data))
        list_data[:] = [element / average for element in list_data]
        return list_data
    else:
        return 0