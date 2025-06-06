choice = 2
match choice:
    case 1 :
        print("your choice is 1")
    case 2:
        select = 1
        match select:
            case 1:
                print("nested case 2")
        print("your choice is 2")
    case 3|4:
        print("your choice is 3 or 4")
    case _:
        print("wrong choice")