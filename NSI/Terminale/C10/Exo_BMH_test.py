assert recherche_BMH('abracadabra', 'dab')
assert recherche_BMH('abracadabra', 'abra')
assert recherche_BMH('abracadabra', 'obra') is False
assert recherche_BMH('abracadabra', 'bara') is False
assert recherche_BMH('maman est là', 'maman')
assert recherche_BMH('bonjour maman', 'maman')
assert recherche_BMH('bonjour maman', 'papa') is False
