import datetime
import csv
import os

file_to_load = os.path.join("../raw_data", "employee_data1.csv")
file_to_output = os.path.join("../analysis", "employee_analysis_1.txt")

full_name = {}
us_state_abbrev = {
    'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA','Colorado': 'CO',
    'Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID',
    'Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN',
    'Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
    'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC',
    'North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX',
    'Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
    'Wisconsin': 'WI','Wyoming': 'WY',
}

# open as f to get column headers to write to txt_file output
with open(file_to_load, 'r') as f:
	reader = csv.DictReader(f)
	headers = reader.fieldnames
	header_output = (
		f"{headers[0]}, {headers[1]}, {headers[2]}, {headers[3]}, {headers[4]}\n"
	)

# open again to pull employee data, row by row
with open(file_to_load) as employee_data:

	reader = csv.DictReader(employee_data)

	with open(file_to_output, "w") as txt_file:

		txt_file.write(header_output)

		for row in reader:

			# split name into first/last
			name_list = row['Name'].split()
			full_name['first'] = name_list[0]
			full_name['last'] = name_list[1]

			# pull emp id
			employee_id = row['Emp ID']

			# convert DOB
			dob = row['DOB']
			dob = datetime.datetime.strptime(dob, '%Y-%m-%d').strftime('%m/%d/%y')

			# encrypt SSN
			ssn = row['SSN']
			ssn = ssn.replace(ssn[:6], "***-**", 1)

			# abbreviate state
			state = row['State']
			state = us_state_abbrev[state]

			employee_output = (
				f"{full_name['first']}, {full_name['last']}, {employee_id}, {dob}, {ssn}, {state}\n"
			)

			# NoSQL article format
			# employee_output = (
			# 	f"\n\nFirst name: {full_name['first']}"
			# 	f"\nLast name: {full_name['last']}"
			# 	f"\nEmployee ID: {employee_id}"
			# 	f"\nEmployee DOB: {dob}"
			# 	f"\nEmployee SSN: {ssn}"
			# 	f"\nState: {state}"
			# )

			print(employee_output, end="")
			txt_file.write(employee_output)
