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

#Just leaving this here, this was my first attempt at figuring out the max response but it didn't go well
# all_responses = {'documentary': doc_response, 'drama': drama_response, 'comedy': com_response}
# print(all_responses)
# best_guess = max(all_responses, key=all_responses.get)
# print(best_guess)
# print('{}'.format(best_guess))

#I tried to find an easy way to validate the input, but wasn't able to figure it out easily. Might try to add that later

if (doc_response >= 4 ): #If they like docs a lot, recommend a doc
    print('You should check out {}!'.format(documentary))
elif (doc_response <= 3) and (drama_response >= 4) and (com_response >= 4): #If they like dramas and comedies a lot and don't like docs as much, recommend a dramedy
    print('You should check out {}!'.format(dramedy))
elif (doc_response < 4) and (drama_response >= 4) and (com_response < 4): #If they like dramas the most, recommend a drama
    print('You should check out {}!'.format(drama))
elif (doc_response < 4) and (drama_response < 4) and (com_response >= 4): #If they like comedy the most, recommend a comedy
    print('You should check out {}!'.format(comedy))
#If they didn't rate any genre higher than 3 but they did rate one genre higher than the other two, recommend the film from that genre.
elif (doc_response < 4) and (drama_response < 4) and (com_response < 4): #If all responses are less than 4...
    if (doc_response > drama_response) and (doc_response > com_response): #and doc is the highest, recommend a doc
        print('You should check out {}!'.format(documentary))
    elif (drama_response > doc_response) and (drama_response > com_response): #and drama is the highest, recommend a drama
        print('You should check out {}!'.format(drama))
    elif (com_response > doc_response) and (com_response > drama_response): #and comedy is the highest, recommend a comedy
        print('You should check out {}!'.format(comedy))
    elif (com_response == drama_response) and (com_response > doc_response): #and comedy & drama have the same rating which is higher than docs, recommend a dramedy
        print('You should check out {}!'.format(dramedy))
    else:
        print('Maybe try a book instead')
else: #Otherwise, suggest a book. All the books that came to mind while working on this are also movies, so I didn't give a specific recommendation
    print('Maybe try a book instead')
