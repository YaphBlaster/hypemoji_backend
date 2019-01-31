from lambda_function import lambda_handler

testObject = [
    {
        "url": "https://render.bitstrips.com/v2/cpanel/10228207-775991c0-e4ac-4b90-8bd2-6ac44e655e3f-55465052-4fcc-40db-91a8-ad75e1162dc5-v1.png?palette=1",
        "uniqueIdentifier": 79867918,
        "comicId": "10228207",
        "text": "abcdefghij"
    },
    {
        "url": "https://render.bitstrips.com/v2/cpanel/10227317-775991c0-e4ac-4b90-8bd2-6ac44e655e3f-55465052-4fcc-40db-91a8-ad75e1162dc5-v1.png?palette=1",
        "uniqueIdentifier": 92452762,
        "comicId": "10227317",
        "text": "abcdefghijabcdefghij"
    },
    {
        "url": "https://render.bitstrips.com/v2/cpanel/20011476-775991c0-e4ac-4b90-8bd2-6ac44e655e3f-55465052-4fcc-40db-91a8-ad75e1162dc5-v1.png?palette=1",
        "uniqueIdentifier": 39339875,
        "comicId": "20011476",
        "text": "third"
    }
]

testObject2 = [
    {
        "url": "https://render.bitstrips.com/v2/cpanel/8165643-775991c0-e4ac-4b90-8bd2-6ac44e655e3f-55465052-4fcc-40db-91a8-ad75e1162dc5-v1.png?palette=1",
        "uniqueIdentifier": 74220169,
        "comicId": "8165643",
        "text": "first"
    }, {
        "url": "https://render.bitstrips.com/v2/cpanel/8165674-775991c0-e4ac-4b90-8bd2-6ac44e655e3f-55465052-4fcc-40db-91a8-ad75e1162dc5-v1.png?palette=1",
        "uniqueIdentifier": 30197382,
        "comicId": "8165674",
    }

]

print(lambda_handler(testObject, "test"))
