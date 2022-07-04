from itertools import permutations

__author__ = 'codesse'


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def calculate_score_for_word_list(self)-> dict:
        """
        Compute the score for each words in valid_words
        :return: The dict of word list and its score.
        """
        all_score = {}
        for valid_word in self.valid_words: 
            score = 0 
            for letter in valid_word: 
                score += self.letter_values[letter]
            all_score[valid_word] = score

        return all_score
        _
    def build_leaderboard_for_word_list(self)-> list:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        all_score = self.calculate_score_for_word_list()
        all_score_sorted = {word: score for word, score in sorted(all_score.items(), reverse=True, key=lambda word_score_pair: word_score_pair[1])}
        return list(all_score_sorted)[:self.MAX_LEADERBOARD_LENGTH]

    def build_leaderboard_for_letters(self, starting_letters)-> list:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """

        all_score = self.calculate_score_for_word_list()
        starting_letters_permutations = [''.join(letter) for length in range(self.MIN_WORD_LENGTH, len(starting_letters) + 1) for letter in permutations(starting_letters, length)]
        starting_letters_valid_words = [word for word in starting_letters_permutations if word in self.valid_words]
        starting_letters_score = {word: all_score[word] for word in starting_letters_valid_words}
        starting_letters_score_sorted = {word: score for word, score in sorted(starting_letters_score.items(), reverse=True, key=lambda word_score_pair: word_score_pair[1])}

        return list(starting_letters_score_sorted)[:self.MAX_LEADERBOARD_LENGTH]

if __name__ == '__main__':
    high_scrore_words = HighScoringWords()
    high_scrore_words.build_leaderboard_for_word_list()
    # high_scrore_words.build_leaderboard_for_letters('adore')