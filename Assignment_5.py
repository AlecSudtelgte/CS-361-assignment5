log = {}
while True:
    print('What you like to do today:\n A) Input Workout\n B) Edit Workout Entry\n C) Delete Workout Entry\n D) View Workout Log\n E) Workouts You Should Try!\n F) End Session\n Input: ')
    answer = input()
    if answer == "A":
        print("Date(MM/DD/YYYY):")
        date = input()
        print("Workout Name:")
        name = input()
        print("Reps:")
        reps = input()
        print("Weight/Distance:")
        weight = input()
        print('Units:')
        units = input()
        log[len(log)] = {"Date": date,
                         "Workout_Name": name,
                         "Reps": reps,
                         "Weight/Distance": weight,
                         "Units": units}
    elif answer == "B":
        print(log)
        print("Please enter the number of the workout you'd like to edit: ")
        answer = int(input())
        print("Which area would you like to change:")
        print(log[answer])
        print("Input: ")
        edit_section = input()
        print("What would you like to change it to:")
        log[answer][edit_section] = input()
        print('Your log has been changed!')
        print(log[answer])
    elif answer == "C":
        print(log)
        print("Please enter the number of the workout you'd like to delete: ")
        answer = int(input())
        print("Are you sure you would like to delete this work out? (Y/N)")
        print(log[answer])
        sub_qes = input()
        if sub_qes == 'Y':
            del log[answer]
            if len(log) > 0:
                for i in range(answer, len(log)):
                    log[i] = log.pop(i+1)
            print('Your log has been changed!')
        else:
            print('Your log has not been changed!')
    elif answer == "D":
        print("Here is your log: ")
        print(log)
    elif answer == "E":
        print("Here's a great workout you should try!")
        print('https://www.youtube.com/watch?v=TwD-YGVP4Bk')
    elif answer == "F":
        print("Thanks and come again!")
        break
    else:
        print("UNKNOWN ANSWER PLEASE USE CAPITAL LETTERS TO SPECIFY WHAT YOU WANT TO DO.")
