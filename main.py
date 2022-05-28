# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        contents = f.read()
    return contents


print(read_file_content('story.txt'))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    divide_text = text.split()
    count ={}
    for t in divide_text:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    return count

print(count_words())