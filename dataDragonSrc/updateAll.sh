curl -useBasicParsing http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/champion.json -o champion.json
curl -useBasicParsing http://static.developer.riotgames.com/docs/lol/queues.json -o queues.json
curl -useBasicParsing http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/runesReforged.json -o runesReforged.json
curl -useBasicParsing http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/summoner.json -o summoner.json
python3 getChampIds.py
python3 getItemIds.py
python3 getQueueIds.py
python3 getRuneIds.py
python3 getSummonerSpellIds.py