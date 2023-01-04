# Intuition
Crying in the club

# Approach
Everything is broken down as follows:
- init(): 
    - Contains a time variable that will be associated with a tweet when it's posted
    - Contains a hashmap of sets called followees that will hold all users a followee follows. We use a set because we don't want duplicate followers for one user
    - Contains a hashmap of lists called tweets that will store tweets by a user

- follow()
    - Adds the given followee ID to the follower's list 

- unfollow()
    - Removes the given followee ID from the follower's list IF it exists

- postTweet()
    - We add the tweetId and current time to the list of tweets for that user. Also decrement the time after (note we're decrementing because the larger negatives are the most recent tweets and should be removed from the heap first) 

- getNewsFeed()
    - We first get the users the user is following and add the user to its own list, since we want to add the user's own tweets to the feed if necessary
    - We then go through each follower's most RECENT tweet, and add it to the heap. We store the time it was posted, the ID, who it was posted by, and the index its located at. We do this because when we pop first, we'll get the most recent tweet from all the users. However, we have to replace that tweet with that user's next recent tweet (if it exists). By storing the followee ID and index, we can decrement the index by 1 and fetch that tweet, then add it to the heap.
    - Once the heap has the most recent tweet from each user, we start the popping/adding process that was mentioned above. We do this until there's no more tweets to get, or we've gotten the most 10 recent tweets

# Complexity
- Time complexity:
    - follow(), unfollow(), and postTweet() are all $O(1)$
    - getNewsFeed(): Let k represent the number of people the user is following. Adding the user's latest tweets to the heap is $O(k)$. Heapify is $O(k)$. Popping/pushing tweets from the heap a max of 10 times is $O(log(k))$. Thus the overall time complexity is $O(k)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
    - If we have n followers and they all follow each other, we'll have $n$ sets with $n$ users which is $O(n^2)$
    - If we have t total tweets, $O(t)$ 
    - Heap is $O(k)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3
class Twitter:

    def __init__(self):
        self.time = 0
        self.followees = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.followees[userId]
        followees.add(userId)

        for followee in followees:
            tweets = self.tweets[followee]
            index = len(tweets) - 1

            if index >= 0:
                time, tweetId = tweets[index]
                heap.append((time, tweetId, followee, index))

        heapq.heapify(heap)
        
        ids = []

        while len(heap) and len(ids) < 10:
            time, tweetId, followee, index = heapq.heappop(heap)
            ids.append(tweetId)

            if index > 0:
                time, tweetId = self.tweets[followee][index - 1]
                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        return ids

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```
