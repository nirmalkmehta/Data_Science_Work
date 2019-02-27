## Text data cleaning
These days data more than 80% of the data is unstructured – it is either present in data silos or scattered around the digital archives. In order to produce any meaningful actionable insight from data, it is important to know how to work with it in its unstructured form.

One of the first steps in working with text data is to pre-process it. It is an essential step before the data is ready for analysis.For example, social media data is highly unstructured – it is an informal communication – typos, bad grammar, usage of slang, presence of unwanted content like URLs, Stopwords, Expressions etc. are the usual suspects.

 **Few important points for text data cleaning:**
 - Escaping HTML characters
 >Data obtained from web usually contains a lot of html entities like &lt; &gt; &amp; which gets embedded in the original data. It is thus necessary to get rid of these entities. One approach is to directly remove them by the use of specific regular expressions. Another approach is to use appropriate packages and modules (for example htmlparser of Python), which can convert these entities to standard html tags. For example: &lt; is converted to “<” and &amp; is converted to “&”.
 - Decoding Data
 > This is the process of transforming information from complex symbols to simple and easier to understand characters. Text data may be subject to different forms of decoding like “Latin”, “UTF8” etc. Therefore, for better analysis, it is necessary to keep the complete data in standard encoding format. UTF-8 encoding is widely accepted and is recommended to use.
 - Apostrophe Lookup
 > To avoid any word sense disambiguation in text, it is recommended to maintain proper structure in it and to abide by the rules of context free grammar. When apostrophes are used, chances of disambiguation increases.
 > For example “it’s is a contraction for it is or it has”.
 > All the apostrophes should be converted into standard lexicons. One can use a lookup table of all possible keys to get rid of disambiguates.
- Removal of stop words
> When data analysis needs to be data driven at the word level, the commonly occurring words (stop-words) should be removed. One can either create a long list of stop-words or one can use predefined language specific libraries.
- Removal of punctuation
> All the punctuation marks according to the priorities should be dealt with. For example: “.”, “,”,”?” are important punctuations that should be retained while others need to be removed.
- Removal of expressions
> Textual data (usually speech transcripts) may contain human expressions like [laughing], [Crying], [Audience paused]. These expressions are usually non relevant to content of the speech and hence need to be removed. Simple regular expression can be useful in this case.
- Split attached words
> We humans in the social forums generate text data, which is completely informal in nature. Most of the tweets are accompanied with multiple attached words like RainyDay, PlayingInTheCold etc. These entities can be split into their normal forms using simple rules and regex.
- Slang look up
> Again, social media comprises of a majority of slang words. These words should be transformed into standard words to make free text. The words like luv will be converted to love, Helo to Hello. The similar approach of apostrophe look up can be used to convert slangs to standard words. A number of sources are available on the web, which provides lists of all possible slangs, this would be your holy grail and you could use them as lookup dictionaries for conversion purposes.
- Standardising words
> Sometimes words are not in proper formats. For example: “I looooveee you” should be “I love you”. Simple rules and regular expressions can help solve these cases.
- Removal of URLs
> URLs and hyperlinks in text data like comments, reviews, and tweets should be removed.

 **Advanced data cleaning:**

- **Grammar checking:** Grammar checking is majorly learning based, huge amount of proper text data is learned and models are created for the purpose of grammar correction. There are many online tools that are available for grammar correction purposes.
- **Spelling correction**: In natural language, misspelled errors are encountered. Companies like Google and Microsoft have achieved a decent accuracy level in automated spell correction. One can use algorithms like the **Levenshtein Distances**, **Dictionary Lookup** etc. or other modules and packages to fix these errors.

## Text data cleaning
These days data more than 80% of the data is unstructured – it is either present in data silos or scattered around the digital archives. In order to produce any meaningful actionable insight from data, it is important to know how to work with it in its unstructured form.

One of the first steps in working with text data is to pre-process it. It is an essential step before the data is ready for analysis.For example, social media data is highly unstructured – it is an informal communication – typos, bad grammar, usage of slang, presence of unwanted content like URLs, Stopwords, Expressions etc. are the usual suspects.

 **Few important points for text data cleaning:**
 - Escaping HTML characters
 >Data obtained from web usually contains a lot of html entities like &lt; &gt; &amp; which gets embedded in the original data. It is thus necessary to get rid of these entities. One approach is to directly remove them by the use of specific regular expressions. Another approach is to use appropriate packages and modules (for example htmlparser of Python), which can convert these entities to standard html tags. For example: &lt; is converted to “<” and &amp; is converted to “&”.
 - Decoding Data
 > This is the process of transforming information from complex symbols to simple and easier to understand characters. Text data may be subject to different forms of decoding like “Latin”, “UTF8” etc. Therefore, for better analysis, it is necessary to keep the complete data in standard encoding format. UTF-8 encoding is widely accepted and is recommended to use.
 - Apostrophe Lookup
 > To avoid any word sense disambiguation in text, it is recommended to maintain proper structure in it and to abide by the rules of context free grammar. When apostrophes are used, chances of disambiguation increases.
 > For example “it’s is a contraction for it is or it has”.
 > All the apostrophes should be converted into standard lexicons. One can use a lookup table of all possible keys to get rid of disambiguates.
- Removal of stop words
> When data analysis needs to be data driven at the word level, the commonly occurring words (stop-words) should be removed. One can either create a long list of stop-words or one can use predefined language specific libraries.
- Removal of punctuation
> All the punctuation marks according to the priorities should be dealt with. For example: “.”, “,”,”?” are important punctuations that should be retained while others need to be removed.
- Removal of expressions
> Textual data (usually speech transcripts) may contain human expressions like [laughing], [Crying], [Audience paused]. These expressions are usually non relevant to content of the speech and hence need to be removed. Simple regular expression can be useful in this case.
- Split attached words
> We humans in the social forums generate text data, which is completely informal in nature. Most of the tweets are accompanied with multiple attached words like RainyDay, PlayingInTheCold etc. These entities can be split into their normal forms using simple rules and regex.
- Slang look up
> Again, social media comprises of a majority of slang words. These words should be transformed into standard words to make free text. The words like luv will be converted to love, Helo to Hello. The similar approach of apostrophe look up can be used to convert slangs to standard words. A number of sources are available on the web, which provides lists of all possible slangs, this would be your holy grail and you could use them as lookup dictionaries for conversion purposes.
- Standardising words
> Sometimes words are not in proper formats. For example: “I looooveee you” should be “I love you”. Simple rules and regular expressions can help solve these cases.
- Removal of URLs
> URLs and hyperlinks in text data like comments, reviews, and tweets should be removed.

 **Advanced data cleaning:**

- **Grammar checking:** Grammar checking is majorly learning based, huge amount of proper text data is learned and models are created for the purpose of grammar correction. There are many online tools that are available for grammar correction purposes.
- **Spelling correction**: In natural language, misspelled errors are encountered. Companies like Google and Microsoft have achieved a decent accuracy level in automated spell correction. One can use algorithms like the **Levenshtein Distances**, **Dictionary Lookup** etc. or other modules and packages to fix these errors.
