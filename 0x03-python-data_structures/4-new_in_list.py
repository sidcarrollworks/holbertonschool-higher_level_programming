def new_in_list(my_list, idx, element):
    listcpy = my_list.copy()
    if idx < 0:
        return listcpy
    if idx > len(my_list) - 1:
        return listcpy
    else:
        listcpy[idx] = element
        return listcpy
