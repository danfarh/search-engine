# Search Engine 
This project aims to build a search engine for products on the Digikala e-commerce website. The project involves scraping product information from the website, building two search engines using ElasticSearch and BERT, and comparing their performance in retrieving relevant products based on user queries.

## Data Source
The data source for this project is the Digikala e-commerce website. The product information is scraped using web scraping techniques and stored in a structured format suitable for search engine indexing.

## Approach
The project will use two search algorithms to build search engines for products on the Digikala website:

- ElasticSearch: A fast and scalable search engine that uses Okapi BM25 algorithm, to retrieve relevant documents based on user queries.
- BERT: The BERT engine will encode the product descriptions and user queries into dense vectors using transformers, save all comments embeddings, and calculate cosine similarity between the query and all sentences to retrieve the most similar products by calculating cosine similarity.

The following steps will be taken:

- Data Collection: Product information will be scraped from the Digikala website using web scraping techniques.
- Data Preparation: The scraped data will be cleaned, preprocessed, and structured for search engine indexing.
- Search Engine Creation: Two search engines will be created using ElasticSearch and BERT.
- Model Evaluation: The performance of the two search engines will be compared on a held-out test set using metrics such as precision, recall, and F1-score.

## Requirements
- Python
- Scrapy
- Docker
- Elasticsearch
- Kibana
- Logstash
- Kafka
- Transformers
- BERT
