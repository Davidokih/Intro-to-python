import random

message_file = open("message.txt", "r")

contest = message_file.read()
# message_file.close()

# print(contest)

hello_file = open("hello.txt", "w")
# hello_file.write("hello world, this is python")
# hello_file.close()

# numbers_file = open("number_history.txt", "w")
with open("number_history.txt", "w") as numbers_file:

    while True:

        random_number = random.randrange(1000)
        print(random_number)
        numbers_file.write(str(random_number))
        numbers_file.write("\n")
        if random_number == 777:
            print("found")
            numbers_file.write("Found!")
            numbers_file.close()
            break