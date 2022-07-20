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

    # Run the following command to run test(s):

        # python3 main.py -t
        # "-t" will run the test for all challenges

    # -----------------------------------------------------

#endregion

################################################################################

# Import modules
import os
import re
import sys
import subprocess

# Parse input
if(len(sys.argv) == 2):
    if(re.match("^\-[0-9]{1,2}$", sys.argv[1]) != None):
        active_challenge_filename = "Challenge" + sys.argv[1][1:].zfill(2) + ".py"
        active_challenge_number = int(sys.argv[1][1:])
        challenge_test = False
    elif(re.match("^\-t$", sys.argv[1]) != None):
        challenge_test = True
    else:
        print("Error: Invalid argument")
        exit()
else :
    print("Error: invalid argument(s)")
    exit()

print("Python Challenges: ")
print("-----------------------------------------------------")

# Run test for all challenges
if(challenge_test):
    # Get all challenge filenames
    challenge_filenames = []
    for filename in os.listdir("challenges"):
        if(re.match("^Challenge[0-9]{1,2}\.py$", filename) != None):
            challenge_filenames.append(filename)

    # Run test for all challenges
    if(len(challenge_filenames) > 0):
        for challenge_filename in challenge_filenames:
            return_code = subprocess.call(
                "python3 challenges\\" + challenge_filename,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
            if return_code == 0:
                print(challenge_filename +   ": Passed")
            else:
                print(challenge_filename +   ": X Failed")
    exit()

# Run selected challenge if it exists
if(os.path.isfile("challenges\\" + active_challenge_filename)):
    os.system('cls')
    os.system("python3 challenges\\" + active_challenge_filename)
    exit()    
# Ask if a new challenge should be created
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