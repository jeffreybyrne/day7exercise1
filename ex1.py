# Think of a documentary, a drama, a comedy, and a dramedy. Store the titles of these films in variables. Ask the user if
#they enjoy 1. documentaries 2. dramas 3. comedies. If they answer yes to documentaries, display a message recommending the
#documentary to them. If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy. If they answer
#yes to only dramas, recommend the drama. If they say yes to only comedies, recommend the comedy. If they answer no to all
#three, recommend a good book instead.

#Setting the various things to recommend
documentary = 'FYRE: The Greatest Party That Never Happened'
drama = 'The Shawshank Redemption'
comedy = 'BASEketball'
dramedy = 'The Truman Show'

#Ask a series of questions, record the responses. I'm being sneaky and only storing the first character of the input
print('Do you like documentaries?')
doc_response = input().lower()[0]
print('Do you like dramas?')
drama_response = input().lower()[0]
print('Do you like comedies?')
com_response = input().lower()[0]


if (doc_response == 'y'): #If they like docs, recommend one
    print('You should check out {}!'.format(documentary))
elif (doc_response == 'n') and (drama_response == 'y') and (com_response == 'y'): #If they don't like docs, but like drama and comedy, recommend the dramedy
    print('You should check out {}!'.format(dramedy))
elif (drama_response == 'y') and (com_response == 'n'): #If they like dramas but not comedy, recommend the drama
    print('You should check out {}!'.format(drama))
elif (drama_response == 'n') and (com_response == 'y'): #If they like comedy but not dramas, recommend the comedy
    print('You should check out {}!'.format(comedy))
else: #Otherwise, suggest a book. All the books that came to mind while working on this are also movies, so I didn't give a specific recommendation
    print('Maybe try a book instead')
