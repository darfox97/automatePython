import re

# Cuando aparezca la palabra Agent, seguida de espacio y otro conjunto de letras o números:
namesRegex = re.compile(r'Agent \w+')
# sustituye por 'censored'
subNamesRegex = namesRegex.sub(
    'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(subNamesRegex)

# También pueden crearse grupos para llamarlos con \1, \2, \3, etc.
agentNamesRegex = re.compile(r'Agent (\w)\w(\w)\w*')
censoredAgentNames = agentNamesRegex.sub(
    r'\1*\2***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(censoredAgentNames)
