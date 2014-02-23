*************

In this folder we are trying to consolidate all the scripts and make the analysis pipeline

>> filtTwitNw.py - filter the twitter network using the id list give by Asmelash


-- 

>> Output - confField

>> mapTwitterUserDBLP.py: Input - dblp.ids, user.info; Output: authorNameIdList.txt

>> saxparser.py, saveToRawFiles.py: Input - dblp.xml ; Output: inproceedings.tsv 

>> mapAuthConf.py : Input - inproceedings.tsv, authNameIdList.txt ; Output: authConf.txt

>> mapAuthField.py : Input - authConf.txt, confField.txt ; Output: authField.txt

>> createInfoMap.py: Input - authField.txt, followNw.txt; Output: followInfoMap.net

>> followNw ->> Gephi ->> followNwData.txt

>> mapCommToField.py - Input - authorfield.txt, authorComm.txt; Output - commFieldDist.txt

>> followInfoMap ->> mapequations ->> followInfoMap.png

*************
