# Receipt Processor

A REST API service that processes store receipts and awards points based on specific rules.

## Overview

The Receipt Processor is a web service that:
- Accepts receipt data via a POST endpoint
- Processes receipts according to a defined set of rules
- Returns a unique ID for each receipt
- Allows point lookups using the receipt ID

## Getting Started

### Prerequisites
- Docker
- Docker Compose (optional)
- Python 3.11+ (if running locally)

### Running with Docker

1. Build the Docker image:
```bash
docker build -t receipt-processor .
```

2. Run the container:
```bash
docker run -p 8000:8000 receipt-processor
```

The API will be available at `http://localhost:8000`

### Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Process Receipt
```
POST /receipts/process
```
Submit a receipt for processing and receive a unique ID.

Example request:
```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    }
  ],
  "total": "6.49"
}
```

Example response:
```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```

### Get Points
```
GET /receipts/{id}/points
```
Retrieve the points awarded for a receipt.

Example response:
```json
{
  "points": 32
}
```

## Points Rules

Points are awarded based on the following rules:
1. One point for every alphanumeric character in the retailer name
2. 50 points if the total is a round dollar amount with no cents
3. 25 points if the total is a multiple of 0.25
4. 5 points for every two items on the receipt
5. If the trimmed length of an item description is a multiple of 3, multiply the price by 0.2 and round up
6. 6 points if the day in the purchase date is odd
7. 10 points if the time of purchase is between 2:00pm and 4:00pm

## Documentation

API documentation is available at `http://localhost:8000/docs` when the service is running.

## Data Validation

The service validates:
- Retailer name (alphanumeric characters, spaces, hyphens, and '&' symbol)
- Purchase date (YYYY-MM-DD format)
- Purchase time (HH:MM format, 24-hour)
- Item descriptions (alphanumeric characters, spaces, and hyphens)
- Prices (valid dollar amounts with exactly two decimal places)

## Storage

Receipts are stored in-memory and will be cleared when the service restarts.