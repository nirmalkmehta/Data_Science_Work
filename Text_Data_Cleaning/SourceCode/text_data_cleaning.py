'''Text data cleaning (with case study using Python)'''
import re
import html
import itertools

text_sample = "I luv your &lt;3 camera &amp; you’re an awsm man. I am so happyyyyyyy because SheIsAwesomeToo 🙂 http://www.google.com"

'''Escaping HTML characters'''
text = html.unescape(text_sample)

'''Decoding data: To keep the complete data in standard encoding format, here I have used UTF8'''
text = text.decode("utf8").encode('ascii', 'ignore')

'''Apostrophe Lookup'''
apos_dict = {"'s": " is", "'re": " are"} #more key value pair can be made

text_words = text.split()
reformed_text = [apos_dict[text_words] if word in apos_dict for word in text_words]
text = " ".join(reformed_text)

'''Removing emoji from text'''
emoji_pattern_is = re.compile("["
		"\<+\d*" #<3(heart)
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
text = emoji_pattern_is.sub(r'', text) # no emoji

'''Split attached word'''
text = " ".join(re.findall('[A-Z][^A-Z]*', text))

'''Standardizing words'''
text = ''.join(''.join(s)[:2] for _, s in itertools.groupby(text))

'''Removal of URL'''
cleaned_text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)




#Note: emoji_pattern matches only some emoji (not all). 
#For more details, See "http://unicode.org/reports/tr51/tr51-12.html#Identification"

