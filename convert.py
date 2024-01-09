try:
    print(b'Easy \xE2\x9C\x85'.decode("utf-8"))
except UnicodeEncodeError:
    print("Unable to display the check mark emoji: :)")
