import re

haystack = "asdasdasdad<script src='cgdgb'>javascr\nipt\nhere</script>asdasdasdad"

needle = "<script(.|\n)*</script>"

re_match = re.search(needle, haystack)
matching_text = re_match.group(0)
print(matching_text)