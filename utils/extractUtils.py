from datetime import datetime

def extract_user_features(data):

    # Extract the desired features
    created_at_str = data["created_at"]
    created_at_datetime = datetime.strptime(created_at_str, '%a %b %d %H:%M:%S %z %Y')
    count = data['statuses_count']
    # Getting today's date
    today_datetime = datetime.now(created_at_datetime.tzinfo)
    # Calculating the age of the account in days
    account_age_days = (today_datetime - created_at_datetime).days
    if account_age_days != 0:
        atpd = round(count / account_age_days)
    else:
        atpd = 0 
    features = {
        'default_profile': data['screen_name'] == 'default',  #'default_profile' means default screen name
        'default_profile_image': data['profile_image_url_https'].endswith('default_profile_normal.png'),
        'favourites_count': data['favourites_count'],
        'followers_count': data['followers_count'],
        'friends_count': data['friends_count'],
        'geo_enabled': data['geo_enabled'],
        'statuses_count': data['statuses_count'],
        'verified': data['verified'],
        'average_tweets_per_day' : atpd,
        'account_age_days' : account_age_days
    }
    #Returns a dictionnary of the features used for the training 
    return features

def extract_followers_features(data):
    print(data)
    user_followers = []
    #response = data.json()
    followers = data["data"]["user"]["timeline_response"]["timeline"]["instructions"][3]["entries"]
    #followers = data.json()["data"]["user"]["timeline_response"]["timeline"]["instructions"][3]["entries"]
    for f in followers:
        if (f["content"]["__typename"] == 'TimelineTimelineItem'):
            follower_data = f["content"]["content"]["userResult"]["result"]["legacy"]
            user_followers.append(extract_user_features(follower_data))
    ##returns a list of followers in a format similar to get_user end_point
    return user_followers
