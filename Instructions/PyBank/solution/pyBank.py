import os
import csv
file_to_load = os.path.join('../raw_data','budget_data_1.csv')
file_to_output = os.path.join('../analysis', 'budget_analysis_1.txt')

total_months = 0
total_revenue = 0
revenue_change = 0
prev_revenue = 0
greatest_increase = 0
greatest_decrease = 0

with open(file_to_load) as revenue_data:

    reader = csv.DictReader(revenue_data)

    for row in reader:

    	total_months += 1
    	total_revenue += int(row['Revenue'])

    	revenue_change = int(row['Revenue']) - prev_revenue
    	prev_revenue = int(row['Revenue'])
    	
    	if revenue_change > greatest_increase:
    		greatest_increase = revenue_change
    		greatest_month = row['Date']
    	elif revenue_change < greatest_decrease:
    		greatest_decrease = revenue_change
    		least_month = row['Date']

average_change = round(total_revenue/total_months)

output = (
f"\n------------------------------------------------"
f"\nTotal months: {total_months}"
f"\nTotal revenue: ${total_revenue}"
f"\nAverage monthly revenue change: ${str(average_change)}"
f"\nGreatest revenue increase: ${str(greatest_increase)}, {greatest_month}"
f"\nGreatest revenue decrease: ${str(greatest_decrease)}, {least_month}"
f"\n------------------------------------------------"
)

print(output)

with open(file_to_output, 'w') as txt_file:
	txt_file.write(output)