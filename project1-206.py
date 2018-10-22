#worked with Hannah Kriftcher and Molly Heller to discuss ways to make each function work

import csv
import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import matplotlib.pyplot as plt


def getData(file):
	f = open(file, "r")
	people_info = []
	for line in f.readlines()[1:]:
		dict = {}
		vals = line.split(",")
		firstName = vals[0].strip()
		lastName = vals[1].strip()
		email = vals[2].strip()
		classes = vals[3].strip()
		dob = vals[4].strip()

		dict["First"] = firstName
		dict["Last"] = lastName
		dict["Email"] = email
		dict["Class"] = classes
		dict["DOB"] = dob

		people_info.append(dict)
	return people_info


def mySort(data, key):
	sorted_list = sorted(data, key = lambda x: x[key])
	new_sorted = []
	for x in sorted_list:
		new_sorted.append(x["First"] + " " + x["Last"])
	return new_sorted[0]



def classSizes(data):
	senior = 0
	junior = 0
	sophomore = 0
	freshman = 0
	for x in data:
		if x["Class"] == "Senior":
			senior = senior + 1
		elif x["Class"] == "Junior":
			junior = junior + 1
		elif x["Class"] == "Sophomore":
			sophomore = sophomore + 1
		elif x["Class"] == "Freshman":
			freshman = freshman + 1

	classes = ["Senior", "Junior", "Sophomore", "Freshman"]
	class_num = [senior, junior, sophomore, freshman]
	list_classes = [(classes[0], class_num[0]), (classes[1], class_num[1]), (classes[2], class_num[2]), (classes[3], class_num[3])]
	sorted_class = sorted(list_classes, key = lambda x: x[-1], reverse = True)
	plt.bar(classes, class_num, label = "Class Sizes", color = 'r')
	plt.show()

	return sorted_class



def findMonth(data):
	jan = 0
	feb = 0
	mar = 0
	apr = 0
	may = 0
	june = 0
	july = 0
	aug = 0
	sept = 0
	octo = 0
	nov = 0
	dec = 0

	for person in data:
		if person["DOB"].split("/")[0] == "1":
			jan = jan + 1
		elif person["DOB"].split("/")[0] == "2":
			feb = feb + 1
		elif person["DOB"].split("/")[0] == "3":
			mar = mar + 1
		elif person["DOB"].split("/")[0] == "4":
			apr = apr + 1
		elif person["DOB"].split("/")[0] == "5":
			may = may + 1
		elif person["DOB"].split("/")[0] == "6":
			june = june + 1
		elif person["DOB"].split("/")[0] == "7":
			july = july + 1
		elif person["DOB"].split("/")[0] == "8":
			aug = aug + 1
		elif person["DOB"].split("/")[0] == "9":
			sept = sept + 1
		elif person["DOB"].split("/")[0] == "10":
			octo = octo + 1
		elif person["DOB"].split("/")[0] == "11":
			nov = nov + 1
		elif person["DOB"].split("/")[0] == "12":
			dec = dec+ 1

	months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
	month_names = (jan, feb, mar, apr, may, june, july, aug, sept, octo, nov, dec)
	distrib = list(zip(months, month_names))
	most_common = sorted(distrib, key = lambda x: x[-1], reverse= True)
	return most_common[0][0]


def mySortPrint(data, key, filename):

	sorted_list = sorted(data, key = lambda x: x[key])
	new_sorted = []
	for x in sorted_list:
		new_sorted.append((x["First"].strip()+","+x["Last"].strip()+","+x["Email"].strip()+"\n"))


		new_file = open(filename, 'w')
		for x in new_sorted:
			new_file.write(x)

def findAge(data):
	lst1 = []
	age = []
	for person in data:
	    lst1.append(person["DOB"])
	    p = person["DOB"]
	    x = p.split("/")

	lst2 = []
	for x in lst1:
	    y = x.split("/")
	    lst2.append(y)

	age = []
	for a in lst2:
	    if int(a[0]) < 10:
	        age.append(2018 - int(a[2]))
	    elif int(a[0]) > 10:
	        age.append(2017 - int(a[2]))
	    elif int(a[0]) == 10 and int(a[1]) <= 16:
	        age.append(2018 - int(a[2]))
	    elif int(a[0]) == 10 and int(a[1]) > 16:
	        age.append(2017 - int(a[2]))

	total = 0
	for num in age:
	    total = total + num
	print(total)
	average = total / len(age)

	return round(average)




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()