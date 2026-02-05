try:
    class student:
        grade=int(input("Enter your grade: "))
        if grade>12:
            print("That is not a valid grade")
            exit()
        print(f"Hi i am a student of grade:{grade}")
    ob=student()
except ValueError:
    print("That is not valid")