ex = ["Keep", "Remove", "Keep", "Remove", "Keep"]

def remove_every_other(my_list):
    for i in range(len(my_list)):
        if i % 2 != 0:
            my_list.pop(i)
    return my_list

remove_every_other(ex)