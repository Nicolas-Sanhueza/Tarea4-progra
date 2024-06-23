import datetime
import typing as ty
import random

def main() -> None:
    """ Main function. """
    print("Hello, World!")
    print("Choose an option:")
    print("1. Print the date")
    print("2. Calculate your final grade")
    print("3. Play rock-paper-scissors")
    print("4. Calculate the factorial of a number")
    choice = input("Enter your choice (number): ")

    if choice == '1':
        date()
    elif choice == '2':
        final_grade()
    elif choice == '3':
        rock_paper_scissors()
    elif choice == "4":
        factorial()
    else:
        print("Invalid choice")

def date() -> None:
    """ Prints today's date. """
    print("Today's date is:", datetime.date.today())

def final_grade() -> None:
    """ Calculate the average in a subject. """
    try:
        assignments = float(input("Enter the grade for assignments (on a scale of 1 to 7): "))
        exams = float(input("Enter the grade for exams (on a scale of 1 to 7): "))
        participation = float(input("Enter the grade for participation (on a scale of 1 to 7): "))
        final_grade = (assignments * 0.5) + (exams * 0.4) + (participation * 0.1)
        print("Your final grade is:", final_grade)
    except ValueError:
        print("Please enter a valid number")

def rock_paper_scissors() -> None:
    """ Play rock, papers and scissors. """
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")


def factorial() -> None:
    """ Call a funcition to calculate the factorial of a number. """
    user_choice = input("Enter a positive int number: ")
    if type(int(user_choice)) != int:
        print("The number chosen must be an int.")
    elif int(user_choice) < 0:
        print("The number chosen must be positive.")
    else:
        print(factorial_auxiliar(int(user_choice)))

def factorial_auxiliar(n: int) -> int:
    """ Calculte the factorial of a number.""" 
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial_auxiliar(n-1)
        

if __name__ == "__main__":
    main()
