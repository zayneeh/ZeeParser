# ZeeParser

## Project Overview
This project develops a specialized resume parsing tool designed for the computer science field, utilizing Named Entity Recognition (NER) enhanced by RoBERTa with attention mechanisms. It aims to efficiently extract relevant information from resumes, such as skills, experience, education, and personal details.

## Features
- **RoBERTa Integration**: Leverages the robust RoBERTa model for deep understanding of context.
- **Attention Mechanisms**: Implements attention mechanisms to focus on key entities.
- **Field Specific**: Optimized for computer science resumes.

## Installation

### Prerequisites
- Python 3.x
- pip



graph TD
    A[User] -->|HTTP Request| B[FastAPI]
    B --> C{Endpoint}
    C -->|/process-data| D[Data Loading]
    C -->|/benchmark| E[Performance Comparison]
    C -->|/download| F[File Delivery]
    D --> G[Pandas/Polars Selection]
    G --> H[Data Cleaning]
    H --> I[Data Aggregation]
    I --> J[Return JSON]
    E --> K[Time Metrics]
    K --> L[Return Benchmark Results]
    F --> M[File Generation]
    M --> N[Parquet/JSON Download]
