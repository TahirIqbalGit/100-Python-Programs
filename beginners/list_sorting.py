""" This file is create and managed by Tahir Iqbal
    ----------------------------------------------
       It can be use only for education purpose
"""

# Sorting List
developer = ['Web', 'Software', 'Data Science', 'Application']
print(developer)
developer.sort() # sort ascending, now list change into ascending
print(developer)
developer.sort(reverse=True) # sort descending, now list change into descending
print(developer)

developer = ['Web', 'Application']
print(sorted(developer)) # doesn't affect or change original list
print(developer)
