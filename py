# Define a function to analyze smoking status and provide advice
def analyze_smoker(smoker_status):
    # Check if the person is a smoker
    if smoker_status == 1:
        # Print advice for smokers to consider quitting
        print("To lower your cost, you should consider quitting smoking")
    else:
        # Print a message indicating smoking is not an issue
        print("Smoking is not an issue for you")
# Define a function to estimate insurance cost based on various factors
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
    # Calculate the estimated insurance cost using the given formula
    estimated_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
    
    # Print the estimated insurance cost with the person's name
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    
    # Call the analyze_smoker function to provide advice based on smoking status
    analyze_smoker(smoker)
