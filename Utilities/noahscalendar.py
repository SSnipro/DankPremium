from icalevents.icalevents import events

url = "webcal://p21-caldav.icloud.com/published/2/MTczNjk0NjYxNTE3MzY5NCI4VvgO8d5bABgiqGFi4zClDgddjpLB5E6CykOqA35uDCfggM9Tbo2CIE2TV6rNNiQaVK2OuNAwgWSOr2MBS7Q" 
es = events(url, fix_apple=True)
for e in es:
    print(e)

