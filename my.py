text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
def get_most_frequent_word(text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    for symbol in punctuation_list:
        text = text.replace(symbol, "")
    text = new_func(text)
    words_list = text.split()
    unique_words = list(set(words_list))
    unique_words.sort()
    word_count = 0
    most_frequent_word = ''
    for word in unique_words:
        if words_list.count(word) > word_count:
            word_count = words_list.count(word)
            most_frequent_word = word
    return most_frequent_word

def new_func(text):
    text = text.lwer()
    return text
print(get_most_frequent_word(text_example))
if __name__ == '__main__':
    score_game(get_most_frequent_word)