Prologue
You have graduated from your three year program and you are trying to make it as a Junior Full Stack Developer. You are excited for the road ahead as you have landed a short term gig to develop a Web Application for a private organization. You have assembled the Team for this project.

You have designed an API that aggregates data from all over the web and displays relevant information based on the user request. Here is the list of data types that need to be extracted from hundreds of pages of strings:

*Movie Titles
*Song Lyrics
*Twitter Usernames
*ISBN numbers
*Jokes
*TV Episode Titles
*Weirdly Formatted Dates
*Hex Color Code
*IP Address
*The Task

In order to extract the required data from the hundreds of thousands of pages of string response you get from your API, you have decided to unleash the raw power of Regular Expressions. You already know how the specific types of data you are looking for appear in the string. This is how you have summarized that information, now all you have to do is write your Regular Expressions:

1. The movie titles should match the pattern "Title (yyyy)", where "Title" is any string of characters, and "yyyy" is a four-digit year.
2. The song lyrics should match the pattern "[Verse X] some lyrics", where X is a number, and "some lyrics" can be any string of characters.
3. The twitter handles should match the pattern "@username", where "username" can be any string of letters and digits.
4. The ISBN numbers should match the pattern "ISBN xxx-x-xxx-xxxxx-x", where x is a digit.
5. The jokes should match the pattern "Why did the ... ? Because...", where the first part of the pattern can be any string of characters, and the second part can be any string of characters.
6. The episode titles should match the pattern "Show Name SXXEXX: Episode Title", where "Show Name" is any string of characters, SXX is a two-digit season number and EXX is a two-digit episode number, and "Episode Title" is any string of characters.
7. The dates should match the pattern dd-MMM-yyyy, where dd is a two-digit day, MMM is a three-letter month abbreviation, and yyyy is a four-digit year.
8. The hex color codes should match the pattern "#XXXXXX" where X is any letter or digit.
9. The IP addresses should match the pattern "xxx.xxx.xxx.xxx" where x is a digit between 0 and 255.
