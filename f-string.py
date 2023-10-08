line="Hi this is {} from {} {} year"
name="Pragya"
branch="IT"
year="1st"
#STRING FORMATING---->Older method
print(line.format(name,branch,year))
#STRING FORMATING USING f-string
print(f"Hi this is {name} from {branch} {year} year")
price=79.923924829
print(f"price={price:.2f}")#price upto 2 decimal places