# Think of a documentary, a drama, a comedy, and a dramedy. Store the titles of these films in variables. Ask the user if
#they enjoy 1. documentaries 2. dramas 3. comedies. If they answer yes to documentaries, display a message recommending the
#documentary to them. If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy. If they answer
#yes to only dramas, recommend the drama. If they say yes to only comedies, recommend the comedy. If they answer no to all
#three, recommend a good book instead.

documentary = 'FYRE: The Greatest Party That Never Happened'
drama = 'The Shawshank Redemption'
comedy = 'BASEketball'
dramedy = 'The Truman Show'

print('Do you like documentaries?')
doc_response = input().lower()
print('Do you like dramas?')
drama_response = input().lower()
print('Do you like comedies?')
com_response = input().lower()


if (doc_response == 'y' or doc_response == 'yes'):
    print('You should check out {}!'.format(documentary))
elif (doc_response == 'n' or doc_response == 'no') and (drama_response == 'y' or drama_response == 'yes') and (com_response == 'y' or com_response == 'yes'):
    print('You should check out {}!'.format(dramedy))
elif (drama_response == 'y' or drama_response == 'yes') and (com_response == 'n' or com_response == 'no'):
    print('You should check out {}!'.format(drama))
elif (drama_response == 'n' or drama_response == 'no') and (com_response == 'y' or com_response == 'y'):
    print('You should check out {}!'.format(comedy))
else:
    print('Maybe try a book instead')
