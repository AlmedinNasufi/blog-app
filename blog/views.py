from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hiking-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Almedin",
        "date": date(2025, 1, 27),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains. And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sunt in culpa qui officia deserunt mollit anim id est laborum. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Almedin",
        "date": date(2025, 3, 15),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one bug in your code? I love that feeling when you finally find it!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sunt in culpa qui officia deserunt mollit anim id est laborum. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Almedin",
        "date": date(2025, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Sunt in culpa qui officia deserunt mollit anim id est laborum. Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
        """
    }
]


def get_date(post):
    return post['date']


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
