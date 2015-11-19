"""
Prints out all the melons in our inventory
"""

from melons import melon_info

def print_melon_info(melon_data):
	for melon, attributes in melon_data.items():
		print melon

		for attributes, value in attributes.items():
			print "%s: %s" % (attributes, value)
		print 

def add_attribute(melon_data, attribute, initial_value = None):
	for melon, attributes in melon_data.items():
		attributes[attribute] = initial_value


add_attribute(melon_info, "weight")


print_melon_info(melon_info)

# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "%ss %s seeds and are $%0.2f" % (name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
