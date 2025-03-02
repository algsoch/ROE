import requests

def get_related_tags(tag):
    url = f"https://api.stackexchange.com/2.3/tags/{tag}/related?site=stackoverflow"
    response = requests.get(url)
    data = response.json()
    
    if 'items' not in data:
        return {}
    
    return {item['name']: item['count'] for item in data['items']}

def find_most_common_tag(tag1, tag2):
    tags1 = get_related_tags(tag1)
    tags2 = get_related_tags(tag2)
    
    common_tags = set(tags1.keys()) & set(tags2.keys())
    
    if not common_tags:
        return None, 0
    
    max_tag = max(common_tags, key=lambda tag: tags1[tag] + tags2[tag])
    max_count = tags1[max_tag] + tags2[max_tag]
    
    return max_tag, max_count

if __name__ == "__main__":
    tag1 = "windows"
    tag2 = "regex"
    common_tag, count = find_most_common_tag(tag1, tag2)
    
    if common_tag:
        print(f"The most commonly associated tag with both '{tag1}' and '{tag2}' is '{common_tag}' with a combined count of {count}.")
    else:
        print("No common tags found.")
