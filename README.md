# small-project-
# Taking small steps towards expertise 💻✨. Recently built a membership project, showcasing my growth as a coder 🚀.
a=int (input("Enter your age:"))
member = input("Are you a member? (yes/no): ").strip().lower() 
if a < 18:
    if member == "yes":
        print("You pay a membership of $5")
    elif member == "no":
        print("You pay a membership of $8")
    else:
        print("Invalid input for membership. Please enter 'yes' or 'no'.")
else:
    if member == "yes":
        print("You pay a membership of $10")
    elif member == "no":
        print("You pay a membership of $20")
    else:
        print("Invalid input for membership. Please enter 'yes' or 'no'.")
