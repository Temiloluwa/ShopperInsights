# Mock data for API responses
challenges = [
    {
        "id": "c1",
        "title": "Weekly Savings Challenge",
        "description": "Save as much as you can on groceries this week!",
        "participants": 42,
        "duration": "7 days",
        "reward": "$50 Gift Card",
        "category": "Savings",
    },
    {
        "id": "c2",
        "title": "Healthy Eating Challenge",
        "description": "Buy at least 5 healthy items in your next grocery trip.",
        "participants": 28,
        "duration": "5 days",
        "reward": "Badge + $20",
        "category": "Health",
    },
]

posts = [
    {
        "id": "1",
        "author": {"name": "Sarah Johnson", "avatar": "/api/placeholder/32/32", "level": 5},
        "content": "Just saved $200 on groceries using the new budget tool! 🎉",
        "timestamp": "2025-07-14T09:00:00Z",
        "likes": 34,
        "comments": 12,
        "category": "Savings",
        "savings": 200,
    },
    {
        "id": "2",
        "author": {"name": "Mike Lee", "avatar": "/api/placeholder/32/32", "level": 3},
        "content": "Joined the weekly challenge and cut my snack spending by 30%!",
        "timestamp": "2025-07-13T15:30:00Z",
        "likes": 21,
        "comments": 5,
        "category": "Challenge",
    },
]

receipts = [
    {
        "id": "1",
        "store": "SuperMart",
        "date": "2025-07-10T14:48:00.000Z",
        "total": 75.5,
        "items": 5,
        "status": "success",
        "imageUrl": "/receipt-sample.png",
    },
    {
        "id": "2",
        "store": "MegaStore",
        "date": "2025-07-12T18:20:00.000Z",
        "total": 120.0,
        "items": 8,
        "status": "success",
        "imageUrl": "/receipt-sample.png",
    },
    {
        "id": "3",
        "store": "Corner Shop",
        "date": "2025-07-13T10:05:00.000Z",
        "total": 25.0,
        "items": 3,
        "status": "processing",
        "imageUrl": "/receipt-sample.png",
    },
]

recommendations = [
    "You can save an average of 15% by shopping at 'Budget Foods' for groceries.",
    "Consider buying 'Brand X' coffee, which is cheaper and highly rated.",
    "Your spending on 'Dining Out' has increased by 20% this month. Set a budget to manage it.",
]

users = [
    {
        "id": "u1",
        "name": "Sarah Johnson",
        "email": "sarah.johnson@email.com",
        "avatar": "/api/placeholder/32/32",
        "role": "admin",
        "createdAt": "2025-07-01T10:00:00Z",
    },
    {
        "id": "u2",
        "name": "Mike Lee",
        "email": "mike.lee@email.com",
        "avatar": "/api/placeholder/32/32",
        "role": "user",
        "createdAt": "2025-07-05T14:30:00Z",
    },
    {
        "id": "u3",
        "name": "Emily Chen",
        "email": "emily.chen@email.com",
        "avatar": "/api/placeholder/32/32",
        "role": "user",
        "createdAt": "2025-07-10T09:45:00Z",
    },
]
