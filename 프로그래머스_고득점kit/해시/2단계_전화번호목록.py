# def solution(phone_book: list) -> bool:
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True


# def solution(phone_book: list) -> bool:
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if (
#                 phone_book[i] in phone_book[j][: len(phone_book[i])]
#                 or phone_book[j] in phone_book[i][: len(phone_book[j])]
#             ):
#                 return False
#     return True


# def solution(phone_book: list) -> bool:
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True


def solution(phone_book: list) -> bool:
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][: len(phone_book[i])]:
            return False
    return True


_phone_book = ["123", "456", "789"]
print(solution(_phone_book))
