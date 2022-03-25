
# NLP Recommender System

The goal of this challenge is to predict which of the provided pairs of questions contain two questions with the same meaning and create some kind of recommender system. The ground truth is the set of labels that have been supplied by human experts. The ground truth labels are inherently subjective, as the true meaning of sentences can never be known with certainty. Human labeling is also a 'noisy' process, and reasonable people will disagree. As a result, the ground truth labels on this dataset should be taken to be 'informed' but not 100% accurate, and may include incorrect labeling. We believe the labels, on the whole, to represent a reasonable consensus, but this may often not be true on a case by case basis for individual items in the dataset.

## Data fields
- id - the id of a training set question pair
- qid1, qid2 - unique ids of each question (only available in train.csv)
- question1, question2 - the full text of each question
- is_duplicate - the target variable, set to 1 if question1 and question2 have essentially the same meaning, and 0 otherwise.

## Steps to complete
1. Create and NLP model to predict if "question1" has the same meaning as "question2", the goal is to predict the column "is_duplicated"
2. With the model implemented in 1. add the functionality of given a new question given by a human, show the most similar questions already in the dataset as a suggestion (like in a web search).
	- For example: 
		- New question: "How much money can I earn as a trader?"
		- Suggested questions already in the dataset: "Can I make 50,000 a month by day trading?", "Can I make 30,000 a month by day trading?"
3. Finally, with the given data create a non supervised model to categorize the text in a few categories and show, given a new question, other related questions in the same category.
	- For example:
		- New question: "How much money can I earn as a trader?"
		- Let's say that you have predicted that the previous question falls in the "economy" category (defined by you), so you can show questions in the same category that are already in the dataset.

Points 2. y 3. are pretty similar but are not the same, the 2. is focused in predict the most similar questions in the dataset (offering a replacement for the user query), and 3. is focused in giving alternative information to the user in the same category (if we want to maintain the user the maximum time possible in our website, for example).

Create a report of the models and algorithms used, and briefly explain the approach that you have coded. You can use external APIs or web scrapping techniques in order to deal with points 2. and 3.
You have to attach the code to the challenge, and you will be asked to explain the program in a next interview, so please keep in mind to not cheat in the challenge.

¡Good luck!