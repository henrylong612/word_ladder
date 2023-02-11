#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    from collections import deque
    import copy

    dictionary = []
    with open(dictionary_file, 'r') as f:
        pre_dictionary = f.read()
        dictionary = pre_dictionary.split()

    start_stack = []
    start_stack.append(start_word)
    queue = deque()
    queue.append(start_stack)
    visited_words = []

    if start_word == end_word:
        return start_stack
    if len(start_word) != len(end_word):
        return None

    while queue:
        stack = queue.popleft()
        for word in dictionary:
            if _adjacent(word, stack[-1]):
                if word == end_word:
                    stack.append(word)
                    return stack
                if word not in visited_words:
                    stack_copy = copy.copy(stack)
                    stack_copy.append(word)
                    queue.append(stack_copy)
                    visited_words.append(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if not ladder:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    changes = 0
    for i, c in enumerate(word1):
        if c != word2[i]:
            changes += 1
    if changes == 1:
        return True
    else:
        return False
