#region

    # The main.py file is used to run and/or create the template for the next challengs.
    
    # Usage:
    # -----------------------------------------------------

    # Run the following command to run a challenge:

    # python3 main.py -<challenge_number>
        # e.g. python3 main.py -0
    
    # If there is already a challenge with <challenge_number> in the challenges folder, it will run the challenge, 
    # otherwise it asks you, if a new challenge template should be created via a (y/n) question.
    # "y" will create a new challenge with the name: "Challenge<challenge_number>.py"
    # "n" will exit the program.

#endregion

################################################################################

# Import modules
import os
import re
import sys

# Parse input
if(len(sys.argv) > 1 and re.match("^\-[0-9]{1,2}$", sys.argv[1]) != None):
    active_challenge_filename = "Challenge" + sys.argv[1][1:].zfill(2) + ".py"
    active_challenge_number = int(sys.argv[1][1:])
else :
    print("Error: invalid argument(s)")
    exit()

# Run selected challenge if it exists
print("Python Challenges: ")
print("-----------------------------------------------------")

if(os.path.isfile("challenges\\" + active_challenge_filename)):
    os.system('cls')
    os.system("python3 challenges\\" + active_challenge_filename)
    exit()
else:
    print("Error: challenge does not exist\n")

    print("Should the challenge be created? (y/n)")
    if(input() == "y"):

        # Load template-code
        with open("challenges\\ChallengeTemplate.py", "r") as template_file:
            template_code = template_file.read()

        # Replace placeholder with challenge number
        template_code = template_code.replace("<0>", str(active_challenge_number))

        # Create challenge template
        with open("challenges\\" + active_challenge_filename, "w") as challenge_file:
            challenge_file.write(template_code)

        print("\nChallenge " + active_challenge_filename + " created")
    else:
        print("\nChallenge " + active_challenge_filename + " not created")

print("\nPython Challenges finished")
print("-----------------------------------------------------\n\n")        
exit()