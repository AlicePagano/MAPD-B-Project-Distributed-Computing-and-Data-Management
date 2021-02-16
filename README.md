# Management and Analysis of Physics Datasets - Part B

## Authors

* [**Rocco Ardino**](https://github.com/RoccoA97) (University of Padua)
* [**Alice Pagano**](https://github.com/AlicePagano) (University of Padua)
* [**Alessandro Valente**](https://github.com/mastrovalentz) (University of Padua)

In this submission, there are two folders:

* Data_Management: it contains the assignment on the part of Dr. Andreas Peters (3 exercises done in python).

* Distributed_Computing: distributed analysis of Covid-19 papers using Dask.

### Distributed analysis of Covid-19 papers using Dask

In response to the COVID-19 pandemic, the White House and a coalition of leading research groups have prepared the COVID-19 Open Research Dataset (CORD-19). CORD-19 is a resource of over 192,000 scholarly articles, including over 84,000 with full text, about COVID-19, SARS-CoV-2, and related coronaviruses. This freely available dataset is provided to the global research community to apply recent advances in natural language processing and other AI techniques to generate new insights in support of the ongoing fight against this infectious disease. There is a growing urgency for these approaches because of the rapid acceleration in new coronavirus literature, making it difficult for the medical research community to keep up. The research and related challenges are available on the [**dedicated page on Kaggle**](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

In this work, we consider as dataset a sub-sample of 1000 items taken from the original dataset that is composed of more than 75000 papers. In order:
* we implement a distributed algorithm to count the occurrences of all the words inside a list of documents using Bag data-structure of Dask;
* we take the documents and convert them in a dataframe data structure in order to figure out the countries that are most and less active in the research;
* lastly, we the cosine similarity between each pair of papers, figuring out some couples of papers with the highest cosine similarity score.


###
