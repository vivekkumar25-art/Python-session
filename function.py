# def calculate_total(price, quanlity):
#     total = price * quanlity
#     print("line", total)


# calculate_total(20, 2)
# calculate_total(30,3)


def fine(late, book_typr="standard",primiun=False):
    if book_typr == "standard":
        if late <= 5:
            fine = late * 5

        else:
            fine = 5 * 5 + ((late - 5) * 10)

    elif book_typr == "reference":
        fine = late * 20

    else:
        fine = 0
        print("invalid")
    if primiun:
        fine = fine * 0.80

    return fine

print(fine(3))





