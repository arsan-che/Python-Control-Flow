# Define a function to analyze smoking status and provide advice
def analyze_smoker(smoker_status):
    # Check if the person is a smoker
    if smoker_status == 1:
        # Print advice for smokers to consider quitting
        print("To lower your cost, you should consider quitting smoking")
    else:
        # Print a message indicating smoking is not an issue
        print("Smoking is not an issue for you")
