def is_mirror(my_list,i1,i2):
    if len(my_list) <= 1:
        return True
    else:
        if my_list[i1] == my_list[i2]:
            return is_mirror(my_list[i1:i2],i1,i2)