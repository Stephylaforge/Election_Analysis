# The data we need to retrieve
# Add our dependencies
import csv
import os

from nbformat import write

# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")\

# Intialize a total vote counter
total_votes = 0
# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}
# County list and county votes
county_list = []
county_votes = {}
# Track the winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Track the largest county and county voter turnout
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0

# Open the election results and read the csv file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # Print the county name from each row
        county_name = row[1]
        # If the candidate does not match any existing candidate
        #add it to the candidate list
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # if the county list does not match any existing county list
        if county_name not in county_list:
            # Add it to existing list of counties
            county_list.append(county_name)
            # Begin tracking the county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's vote count
        county_votes[county_name] += 1 

# Save the results to ur text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"----------------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Write a repetition statement to get the county from the county dictionary
    for county_name in county_votes :
        # Retrieve the county vote count
        cvotes = county_votes.get(county_name)
        # Calculate the percent of total votes for the county
        cvotes_percentage = float(cvotes) / float(total_votes) * 100
        # Print the county results
        county_results = (
            f"{county_name}: {cvotes_percentage:.1f}% ({cvotes:,})\n")
        print (county_results)
        # Save county votes to text file
        txt_file.write(county_results)
        # Write an if statement to determine the winning county and get its vote count.
        if (cvotes > winning_county_votes) and (cvotes_percentage > winning_county_percentage):
            winning_county_votes = cvotes
            winning_county = county_name
            winning_county_percentage = cvotes_percentage
    # Print the county with the largest turnout to the terminal
    winning_county_summary = (
        f"----------------------------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------------------------------\n")
    print(winning_county_summary)
    # Save the county with the largest turnout to a text file
    txt_file.write(winning_county_summary)

    # Determine the percentage of votes for eaach candidate by looping through the counts
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
         # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # print out each candidate's name, vote count, and percentage of votes to terminal
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote, count, percent, and winning candidate 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percent = vote_percentage and name 
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print winning candidate's results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidates names to the text file
    txt_file.write(winning_candidate_summary)