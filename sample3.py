numbers=[1,2,3,4,5,6,7]
#print(5 in numbers)
numbers.append(8)
more_numbers=[9,10]
extra_numbers=[11,12,13]
numbers.extend(more_numbers)
#print(len(numbers+extra_numbers))
numbers_more=set(numbers)

colours=['a','b','c','d']
print(set(colours))