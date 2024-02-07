def update_user_document(users, userid, username, profile_pic_url):
    # Check if the user exists; if not, insert new, otherwise update
    existing_user = users.find_one({'id': userid})

    if existing_user:
        # User exists, update their profile picture URL
        users.update_one({'id': userid}, {'$set': {'profile_pic_url': profile_pic_url}})
    else:
        # User doesn't exist, insert as new
        new_user = {
            'id': userid,
            'username': username,
            'profile_pic_url': profile_pic_url,
            'friends': [],
            'friendRequests': [],
            'playlists': []
        }
        users.insert_one(new_user)