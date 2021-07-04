
#QUESTION 1
#gross revenue
sales = 150
average_price = 2100
cogs_percentage = 0.59

Revenue= sales* average_price
annual_gross_revenue = Revenue
quarterly_gross_revenue = Revenue / 4
monthly_gross_revenue = Revenue / 12

print('annual_gross_revenue = ',annual_gross_revenue )
print('quarterly_gross_revenue =',quarterly_gross_revenue )
print('monthly_gross_revenue', monthly_gross_revenue)

print('\n')
print('='*30)
print('\n')
#QUESTION 2
# net revenue 
cogs = annual_gross_revenue * cogs_percentage
annual_net_revenue = annual_gross_revenue - cogs
quarterly_net_revenue = annual_net_revenue / 4.0
monthly_net_revenue = annual_net_revenue / 12.0

print('annual_net_revenue= ',annual_net_revenue )
print('quarterly_net_revenue =',quarterly_net_revenue )
print('monthly_net_revenue', monthly_net_revenue)











