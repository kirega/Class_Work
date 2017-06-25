def print_lol(the_list):"""the name of the nesting function"""
for each_item in the_list:"""start the looping in the outer list"""
if isinstance(each_item, list):"""check if the element is also a list"""
print_lol(each_item)"""True:Recall the function again"""
else:
print(each_item)"""False: Print the element in the outer loop"""
