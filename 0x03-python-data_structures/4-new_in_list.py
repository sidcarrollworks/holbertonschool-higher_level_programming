def new_in_list(my_list, idx, element):
    listcpy = my_list.copy()
    if idx < 0:
        return listcpy
    if idx > len(my_list):
        return listcpy
    else:
        listcpy[idx] = element
        return listcpy
