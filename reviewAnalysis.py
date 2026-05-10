# Review Analysis -> product -> (product_name, rating, sentiment, is_fake_review)

from pydantic import BaseModel, ValidationError 

class ReviewAnalysis(BaseModel):
    product_name: str
    rating: float 
    sentiment: str 
    is_fake_review: bool 

mock_data = {
    "product_name": "12",
    "rating": "2.5",
    "sentiment": "positive",
    "is_fake_review": "false"
}

review = ReviewAnalysis(**mock_data)

print(review)

if(review.rating<3):
    print("Bad product alert")
