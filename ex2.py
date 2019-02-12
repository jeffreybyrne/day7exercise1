# Let's take a different approach to film recommendations: create the same variables containing your potential film
#recommendations and then ask the user to rate their appreciation for 1. documentaries 2. dramas 3. comedies on a scale
#from one to five. If they rate documentaries four or higher, recommend the documentary. If they rate documentaries 3 or
#lower but both comedies and dramas 4 or higher, recommend the dramedy. If they rate only dramas 4 or higher, recommend the
#drama. If they rate just comedies 4 or higher, recommend the comedy. Otherwise, recommend a good book.

#Setting the various things to recommend
documentary = 'FYRE: The Greatest Party That Never Happened'
drama = 'The Shawshank Redemption'
comedy = 'BASEketball'
dramedy = 'The Truman Show'

#Ask for user input
print('On a scale from 1-5, how much do you like documentaries?')
doc_response = int(input())
print('On a scale from 1-5, how much do you like dramas?')
drama_response = int(input())
print('On a scale from 1-5, how much do you like comedies?')
com_response = int(input())

#I tried to find an easy way to validate the input, but wasn't able to figure it out easily. Might try to add that later

if (doc_response >= 4 ): #If they like docs a lot, recommend a doc
    print('You should check out {}!'.format(documentary))
elif (doc_response <= 3) and (drama_response >= 4) and (com_response >= 4): #If they like dramas and comedies a lot and don't like docs as much, recommend a dramedy
    print('You should check out {}!'.format(dramedy))
elif (doc_response < 4) and (drama_response >= 4) and (com_response < 4): #If they like dramas the most, recommend a drama
    print('You should check out {}!'.format(drama))
elif (doc_response < 4) and (drama_response < 4) and (com_response >= 4): #If they like comedy the most, recommend a comedy
    print('You should check out {}!'.format(comedy))
else: #Otherwise, suggest a book. All the books that came to mind while working on this are also movies, so I didn't give a specific recommendation
    print('Maybe try a book instead')
