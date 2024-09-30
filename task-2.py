from collections import deque


def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    dq = deque(cleaned_string)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


test_string = "око"
print(f"Is palindrome: {is_palindrome(test_string)}")
