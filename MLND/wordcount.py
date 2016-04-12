"""Count words."""
#from operator import itemgetter

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s = s.split(" ")
    words_dict = {word: s.count(word) for word in s}

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    l = []

    for word in sorted(words_dict, key=words_dict.get, reverse=True):
    	l.append( (word, words_dict[word]) )

    l.sort(key=lambda tup: (-tup[1], tup[0]))
    
    #l.sort(key=itemgetter(1), reverse = True)
    #l.sort(key=itemgetter(0))
    

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    #return top_n
    return l[0:n]



def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()