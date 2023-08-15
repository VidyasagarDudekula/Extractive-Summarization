# Extractive-Summarization with TF-IDF Scoring

This project employs Term Frequency-Inverse Document Frequency (TF-IDF) scoring to summarize textual content. The code cleans and tokenizes the input text, computes TF-IDF scores for individual sentences, and selects the top-ranked sentences to generate a concise summary.



## Overview

### 1. Data Cleaning and Preparation

The raw textual data undergoes several pre-processing steps to improve the quality of the summarization:

* Removal of extra spaces and unnecessary characters.
* Sentence tokenization to split the text into individual sentences.
* Word tokenization of sentences and filtering to remove stop words.

### 2. Computing Sentence Scores

Using the tokenized and cleaned sentences:

* A dictionary of all unique tokens across the content is created.
* Each sentence's Term Frequency (TF) and Inverse Document Frequency (IDF) scores are computed.
* Sentences are ranked based on their TF-IDF scores.

## 3. Generating Summary

The top-ranked sentences based on their TF-IDF scores are selected to produce the summary. The number of sentences in the summary can be adjusted using the sent_count parameter.

## File Structure

The config.yaml file contains various configuration parameters that control the behavior of the summarization * __src__: Contains the main Python script (main.py) for the project.
* __data__: Houses the textual content (content.txt) that needs to be summarized.


## Configurations

You can adjust the following parameters in the code:

* __content__: The input textual content. If not provided, the content will be read from content.txt.
* __sent_count__: Number of top-ranked sentences to be included in the summary. The default value is 4.

## Requirements

Please ensure that all dependencies are installed by running the following command:

```bash
  pip install -r requirements.txt
```
Also, ensure that the NLTK corpora for stopwords is downloaded:
```python
  import nltk
  nltk.download('stopwords')
```

## Usage

To generate a summary using the default configurations:
### 1. Navigate to the src directory.
### 2. Run the main.py script:

```bash
  cd src
  python main.py
```
## Examples
### Input Text

A key component of fruit juice may be behind our current obesity epidemic. This common sugar has been shown to flick a metabolic switch in our bodies that increases our hunger, thirst and fat accumulation, as well as insulin resistance, systemic inflammation and increased blood pressure. The compound in question is fructose, a sugar found naturally in fruit and honey. However, in the modern Western diet fruits provide only a small percentage of our overall fructose intake. 

"Most of the fructose we have comes from high-fructose corn syrup and table sugar and added sugar, which are made of glucose and fructose," Richard Johnson, a professor of medicine at the University of Colorado Anschutz Medical Campus, told Newsweek. "Soft drinks can have as much as 30 grams of fructose in them, while a kiwi may have just 2 to 3 grams.". 

In fact, the comparatively low levels of fructose found in fruit are largely negated by the small intestine, as shown by a 2018 study published in the journal Cell Metabolism. "When you eat moderate amounts of fructose in natural fruit, the body deactivates the fructose so you don't get a lot of the sugar going into your system," Johnson said. 

"Actual fruits contain so many things besides fructose that are good for us, like potassium and vitamin C, fiber which slows absorption, and the flavanols which can actually counter the effect of fructose.". The problem comes when we eat high volumes of fructose in one sitting. "If you ate 100 fruits at a time, like an animal going into hibernation, you will get a large dose of fructose," Johnson said. 

"And likewise if you drink fruit juice, you can get a lot of concentrated fructose because you get, like, five or six fruits combined into one glass.". Fruit juice contains less fiber than raw fruits, and so its sugars are more easily absorbed into the blood. It is also easier to gulp down large quantities of fructose in a short space of time. Many fruit juices also contain added sugars, which ramps up the fructose concentration even higher. In fact, many fruit juices contain as much sugar as a can of Coke. But why is fructose a problem?. 

"Fructose turns out to have a very powerful way to activate a biological switch that activates a range of processes that includes hunger, eating, leptin resistance—the satiety hormone—and a series of events that make you want to store fat," Johnson said. "And we actually showed that it's unique to fructose. And that it works by tricking the cells into thinking it doesn't have enough energy.". 

Fructose does this by lowering the concentration of the body's main energy currency, ATP. This is thought to activate the body's survival response and disrupt weight regulation, Johnson said. "This stimulates foraging, hunger and thirst but it also blocks satiety and fullness," Johnson said. Low cellular levels of ATP are also a characteristic of obesity, diabetes, nonalcoholic fatty liver disease and Alzheimer's. But even if you avoid fructose in your diet, you may still see these effects. 

"It isn't just the fructose that we eat but also fructose made by the body from carbs like potatoes and rice," Johnson said. "Carbs raise our blood glucose, and that glucose can then be converted into fructose by the body.". This type of fructose production is higher in people with high-sugar and high-salt diets. It is also stimulated by alcohol consumption. Unfortunately, humans are even more sensitive to fructose than other animals, probably as a result of our evolution through periods of near starvation that lasted for millions of years. 

"Of course, this genetic adaptation backfires in a world of plenty," Johnson said. Johnson emphasized that this research does not indicate a need to reduce our fruit intake but rather to reduce our excessive consumption of foods and drinks artificially high in fructose. These high-fructose diets may, in turn, be driving the obesity epidemic. A full review of the evidence for the fructose hypothesis for obesity was published in May by Johnson and his team in the journal Philosophical Transactions B. .

### Generated Summary

Summary is:- 

Fructose turns out to have a very powerful way to activate a biological switch that activates a range of processes that includes hunger, eating, leptin resistance—the satiety hormone—and a series of events that make you want to store fat, Johnson said. 
Most of the fructose we have comes from high-fructose corn syrup and table sugar and added sugar, which are made of glucose and fructose, Richard Johnson, a professor of medicine at the University of Colorado Anschutz Medical Campus, told Newsweek. 
This common sugar has been shown to flick a metabolic switch in our bodies that increases our hunger, thirst and fat accumulation, as well as insulin resistance, systemic inflammation and increased blood pressure. Actual fruits contain so many things besides fructose that are good for us, like potassium and vitamin C, fiber which slows absorption, and the flavanols which can actually counter the effect of fructose.


## Improve

For any issues or improvements, feel free to open an issue or a pull request.
