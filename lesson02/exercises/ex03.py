# Danh sách user: list tuple (user_id, name)
users = [
    ("U01", "Alice"),
    ("U02", "Bob"),
    ("U03", "Charlie"),
]

# Dict bài viết: key là post_id, value là dict thông tin
posts = {
    "P01": {
        "title": "Hoc Python co ban",
        "author_id": "U01",
        "tags": {"python", "beginner"},
    },
    "P02": {
        "title": "Lam viec voi List va Dict",
        "author_id": "U01",
        "tags": {"python", "data-structure"},
    },
    "P03": {
        "title": "Gioi thieu HTML CSS",
        "author_id": "U02",
        "tags": {"web", "frontend"},
    },
}

# a
print("\na.")

user_map = {}

for user_id, name in users:
    user_map[user_id] = name

print(user_map)

# b
print("\nb.")
for post_id, post in posts.items():

    title = post["title"]
    author_id = user_map[post["author_id"]]
    tags_list = sorted(list(post["tags"]))

    print(f'[{post_id}] {title} - {author_id} - Tags: {", ".join(tags_list)}')

# c
print("\nc.")

all_tags = set()

for post_id, post in posts.items():
    all_tags.update(post["tags"])

print(all_tags)

# d
print("\nd.")

tag_counter = {}

for post_id, post in posts.items():
    tags = post["tags"]
    for tag in tags:
        tag_counter[tag] = tag_counter.get(tag, 0) + 1

print(tag_counter)
