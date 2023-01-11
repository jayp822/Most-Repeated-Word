text = """

"I can't remember," Huey P. Long reminisced in 1935, "back to a time when my mouth wasn't open whenever there was a chance to make a speech." Long's oratorical prowess was a powerful asset in a colorful and controversial political career that began with his election to the Louisiana Railroad Commission in 1918 and culminated in his election to the United States Senate in 1930. As governor of Louisiana (1929-1932), he instigated much needed reforms—the poll tax was abolished, roads and bridges constructed, and free textbooks supplied to all Louisiana schoolchildren—but exercised a near-dictatorial control over state politics and government that continued while he served in the Senate.

Long's rhetoric was a distinctive blend of humor and invective, scripture and profanity, brutal fact and absurd analogy, couched in a populist vernacular that made the impoverished citizens of rural Louisiana feel that he was one of them. "Better than any other politician I've known," one newsman recalled, "Huey knew what his audiences wanted to hear." In the Senate, Long employed his flamboyant declamation, loud attire, and irreverent antics—which made good copy for reporters and filled the Senate galleries whenever the "Terror of the Bayous" took to the floor—to advocate a serious agenda. "I had come to the United States Senate," he later explained, "with only one project in mind…that…I might do something to spread the wealth of the land among all of the people."

Long's February 23, 1934 "Every Man a King" (PDF) address, broadcast over the NBC radio network, signaled a new phase in his longstanding effort to secure a more equitable distribution of the nation's wealth. He had introduced legislation in the Senate in 1932 and 1933 to limit incomes and redistribute wealth, but even amid the widespread suffering of the Great Depression, his proposals died in committee because they were considered too radical to be taken seriously. President Franklin D. Roosevelt thought the Louisiana senator was "one of the two most dangerous men in the country" and handled him with care. Long had helped FDR secure the 1932 Democratic nomination but broke with the administration in 1934. Convinced that the New Deal would not effect a redistribution of wealth, outraged at the president's use of patronage to undercut him in Louisiana, and determined to fulfill his own presidential ambitions, Long took his cause to the American people with his "Every Man a King" radio address.

Long borrowed his title, which he also used for his 1933 autobiography, from a speech by 1896 Democratic presidential candidate and free silver advocate William Jennings Bryan. Suiting his style to his radio audience, Long explained his agenda in simple, repetitive phrases. In this and later broadcasts explaining the "Share Our Wealth" program, his style was, in Paul C. Gaske's words, "a combination of self-absurdness, intensity, and conviction" that made his "amalgam of populism, technocracy, the Bible, and Share Our Wealth, especially appealing."  "Every Man a King" was essentially a restatement of the redistribution proposals that the Senate had rejected in 1932 and 1933, buttressed by many of the same spurious arguments and homely analogies but animated by a new strategy. "Write me and let me send you data on this proposition," Long invited his listeners. "Share Our Wealth societies are now being organized," he urged—with more optimism than truth—"and people have it within their power to relieve themselves from this terrible situation."

Long was one of the first politicians to appreciate the power of radio, and his broadcasts won him a national following. By the spring of 1935, over seven million Americans had accepted his invitation to form local "Share Our Wealth" societies, providing a formidable base for his anticipated presidential bid. President Roosevelt's supporters feared that with Long as a third party candidate, the Republicans would win the 1936 election; Gerald L. K. Smith, head of the national "Share Our Wealth" organization, predicted that "the only way they will keep Huey Long from the White House is to kill him."

Long was assassinated by the son-in-law of a political rival in September 1935. Although he had portrayed himself as a poor man, his net worth at the time of his death exceeded $2 million. Long's proposals were never adopted, but the "Share Our Wealth" program did exert some measure of influence on an administration anxious to "steal Long's thunder." Roosevelt eventually conceded that the nation's tax laws had failed "to prevent an unjust concentration of wealth and economic power" and proposed legislation to increase inheritance taxes and impose a surtax on wealthy Americans. Long remains a controversial figure; but, while modern scholars question his motives and methods, all concur in the assessment of Roosevelt campaign strategist James Farley that Huey Long "put on a great show wherever he went."

"""

word_count = {}

for word in text.split():
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1

most_rep = None
most_rep_count = None

for word in word_count:
  if most_rep == None:
    most_rep = word
    most_rep_count = word_count.get(word)
  elif most_rep_count < word_count.get(word):
    most_rep = word
    most_rep_count = word_count.get(word)

print(most_rep, " ", most_rep_count)
