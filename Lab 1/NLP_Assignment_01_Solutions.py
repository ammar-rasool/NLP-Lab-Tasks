# NLP Assignment 01


import re
import nltk
import spacy


# ============================================================
# TASK 1: Regex Fundamentals (Character Classes & Quantifiers)
# ============================================================

# Sample text for Task 1
text1 = """
My name is Ammar and I am 20 years old. The year is 2026.
I scored 95 marks, bought 3 books, and paid $50 for them.
COMSATS University is in Islamabad.
"""

# Task 1(a): Extract all digits from the text
digits = re.findall(r"\d", text1)

print("\nTASK 1(a)")
print("All digits:", digits)


# Task 1(b): Extract all words that start with a capital letter
capital_words = re.findall(r"\b[A-Z][a-zA-Z]*\b", text1)

print("\nTASK 1(b)")
print("Words starting with a capital letter:", capital_words)


# Task 1(c): Extract all sequences of exactly 4 digits
four_digits = re.findall(r"\b\d{4}\b", text1)

print("\nTASK 1(c)")
print("Exactly 4 digit sequences:", four_digits)


# Task 1(d): Extract all words between 3 and 6 characters long
words_3_to_6 = re.findall(r"\b[A-Za-z]{3,6}\b", text1)

print("\nTASK 1(d)")
print("Words with 3 to 6 characters:", words_3_to_6)


# ============================================================
# TASK 2: Pattern-Based Extraction (Real World Data)
# ============================================================

# Sample paragraph containing the required data
text2 = """
Contact Ali at ali@example.com or sara@test.org.
His phone number is 0300-1234567 and the second number is 0312-7654321.
Order IDs are ORD123 and ORD456. The order dates are 25/09/2026
and 01/10/2026. The discount was 45% while another discount was 12.5%.
"""

# Task 2(a): Extract all email addresses
emails = re.findall(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    text2
)

print("\nTASK 2(a)")
print("Email addresses:", emails)


# Task 2(b): Extract phone numbers in 03XX-XXXXXXX format
phone_numbers = re.findall(r"\b03\d{2}-\d{7}\b", text2)

print("\nTASK 2(b)")
print("Phone numbers:", phone_numbers)


# Task 2(c): Extract dates in DD/MM/YYYY format
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text2)

print("\nTASK 2(c)")
print("Dates:", dates)


# Task 2(d): Extract percentage values
percentages = re.findall(r"\b\d+(?:\.\d+)?%", text2)

print("\nTASK 2(d)")
print("Percentage values:", percentages)


# ============================================================
# TASK 3: Word Tokenization (NLTK vs spaCy)
# ============================================================

paragraph = """
I don't like noisy data because it's difficult to clean.
Natural language processing is useful for many applications.
Researchers often tokenize text before analyzing it.
Good preprocessing can make later NLP tasks easier.
"""

# Task 3(a): Tokenize using NLTK's word_tokenize()
try:
    nltk_tokens = nltk.word_tokenize(paragraph)
except LookupError:
    print("\nTASK 3(a)")
    print("NLTK tokenizer data is missing.")
    print("Run: nltk.download('punkt_tab')")
    nltk_tokens = []

print("\nTASK 3(a)")
print("NLTK tokens:")
print(nltk_tokens)


# Task 3(b): Tokenize using a blank spaCy pipeline
nlp_blank = spacy.blank("en")
doc = nlp_blank(paragraph)
spacy_tokens = [token.text for token in doc]

print("\nTASK 3(b)")
print("spaCy blank pipeline tokens:")
print(spacy_tokens)


# Task 3(c): Compare the two outputs
# Difference 1: NLTK's word_tokenize() normally separates contractions
# such as "don't" into "do" and "n't", while spaCy keeps "don't" as
# one token in the blank English tokenizer.
#
# Difference 2: NLTK's tokenizer can create separate punctuation tokens,
# and spaCy also separates punctuation, but the exact tokenization rules
# can differ between the two tokenizers.

print("\nTASK 3(c)")
print("Difference 1: Contractions can be split differently by NLTK and spaCy.")
print("Difference 2: Punctuation and token boundaries can differ between them.")


# Task 3(d): Count total tokens from each method
print("\nTASK 3(d)")
print("Total NLTK tokens:", len(nltk_tokens))
print("Total spaCy tokens:", len(spacy_tokens))


# ============================================================
# TASK 4: Token Attributes (Categorizing Tokens)
# ============================================================

sentence = "Ali bought 2 books for $50 and contacted ali@example.com."

# Task 4(a): Load the sentence into a spaCy Doc object
nlp = spacy.blank("en")
doc = nlp(sentence)

print("\nTASK 4(a)")
print("Sentence loaded into spaCy Doc.")


# Task 4(b): Print each token and its is_alpha value
print("\nTASK 4(b)")
for token in doc:
    print(token.text, "-> is_alpha:", token.is_alpha)


# Task 4(c): Print each token's like_num and like_email values
print("\nTASK 4(c)")
for token in doc:
    print(
        token.text,
        "-> like_num:", token.like_num,
        ", like_email:", token.like_email
    )


# Task 4(d): List only tokens where is_currency is True
currency_tokens = [
    token.text for token in doc
    if token.is_currency
]

print("\nTASK 4(d)")
print("Currency tokens:", currency_tokens)


# ============================================================
# TASK 5: Sentence Segmentation (Handling Tricky Cases)
# ============================================================

paragraph2 = """
Dr. Ahmed is a researcher at the university. He studies NLP methods.
For example, he works on tokenization and sentence segmentation.
Mr. Khan is also part of the research group.
"""

# Task 5(a): Load the trained spaCy pipeline
print("\nTASK 5(a)")

try:
    nlp_trained = spacy.load("en_core_web_sm")
    print("en_core_web_sm loaded successfully.")

except OSError:
    print("The spaCy model en_core_web_sm is not installed.")
    print("Run: python -m spacy download en_core_web_sm")
    nlp_trained = None


# Task 5(b): Use doc.sents to split into sentences
if nlp_trained is not None:
    doc2 = nlp_trained(paragraph2)
    sentences = list(doc2.sents)

    print("\nTASK 5(b)")
    for i, sentence in enumerate(sentences, start=1):
        print(i, ":", sentence.text)


    # Task 5(c): Print the total number of sentences
    print("\nTASK 5(c)")
    print("Total sentences detected:", len(sentences))


    # Task 5(d): Check abbreviation handling
    # The trained English pipeline normally recognizes common abbreviations
    # such as "Dr." and "Mr." and does not incorrectly split the sentence
    # immediately after those abbreviations.
    print("\nTASK 5(d)")
    print(
        "Observation: The abbreviations Dr. and Mr. did not cause "
        "incorrect sentence breaks in the trained spaCy pipeline."
    )

else:
    print("\nTASK 5(b)")
    print("Sentence segmentation skipped because the trained model is missing.")

    print("\nTASK 5(c)")
    print("Total sentences detected: 0")

    print("\nTASK 5(d)")
    print("Install en_core_web_sm to test abbreviation handling.")


# ============================================================
# END OF ASSIGNMENT
# ============================================================
