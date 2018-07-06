# -*- coding: UTF-8 -*-
import os
import csv

file_to_load = os.path.join('../raw_data', 'election_data_1.csv')
file_to_output = os.path.join('../analysis', 'election_analysis_1.txt')

total_votes = 0

# candidate options and vote counters
candidate_options = []
candidate_votes = {}

# winning candidate and winning vote tracker
winning_candidate = ""
winning_count = 0

with open(file_to_load) as polling_data:
	reader = csv.DictReader(polling_data)

	for row in (reader):

		# tally one vote for every row
		total_votes += 1

		# append candidate if not in list
		candidate_name = row['Candidate']

		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name] = 0

		candidate_votes[candidate_name] += 1

# print results and export data to text file
with open(file_to_output, "w") as txt_file:

	election_results = (
		f"\n\n---------------------\n"
		f"Election Results:\n"
		f"---------------------\n"
		f"Total Votes: {total_votes}\n"
		f"---------------------\n")
	print(election_results, end="")

	txt_file.write(election_results)

	# loop through candidates to get vote count for each
	for candidate in candidate_votes:

		votes = candidate_votes.get(candidate)
		vote_percentage = float(votes)/float(total_votes) * 100

		voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
		print(voter_output, end="")

		txt_file.write(voter_output)

		# determine winning candidate
		if votes > winning_count:
			winning_count = votes
			winning_candidate = candidate

	winner_results = (
		f"---------------------\n"
		f"Winner: {winning_candidate}\n"
		f"---------------------\n"
	)

	print(winner_results)

	txt_file.write(winner_results)




