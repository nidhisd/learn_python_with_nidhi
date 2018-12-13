def test_for_statement():
    
    #Iterating over the numbers:
    numbers = []
    for i in range(5):
        numbers.append(i)
    assert numbers == [0, 1, 2, 3, 4]



    
    #Nested Fors:
    #In the code snippet below, I am trying to explain the usage of nested For loops.
    
    sentence = "Here we go round the Mulberry bush"
    sentences = sentence.split()
    count = 0
    for words in sentences:      #This is for every word in the sentence.
        for letters in words:   #This is for every letter in the word.
            count += 1
    assert count == 28

    #We can further use range() and len() to make the sentence back.
    concatenated_sentence = ''
    for words in range(len(sentences)):
        concatenated_sentence += sentences[words] + ' '
    concatenated_sentence.rstrip()
    assert concatenated_sentence == "Here we go round the Mulberry bush "

    #Oe we can also achieve aboce using enumerate(). Let's see how?
    print(enumerate(sentence))

test_for_statement()