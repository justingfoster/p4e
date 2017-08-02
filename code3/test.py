import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

text = ['<script class="js-map-config" id="js-map-config-dir-map-location-map" type="text/data">{"config": {"apiID":"gme-yextinc","baseUrl":"../../","channelId":"stores.advanceautoparts.com","disableMapControl":true,"extraData":null,"linkToGetDirections":true,"mapId":"dir-map-location-map","mapboxMapIdentifier":null,"maxNumberOfLocationsToDisplay":1,"provider":"Google","source":null,"zoom":10}, "locs": [{"altTagText":"Advance Auto Parts at 969 N Daleville Avenue Daleville, AL","get_directions_url":"https://maps.google.com/maps?cid=17109494347283599600","id":3924561,"latitude":31.32064395326026,"longitude":-85.71085675621816,"type":"main","url":""}], "nearbyLocs": [{"altTagText":"Advance Auto Parts at 908 Rucker Blvd. Enterprise, AL","get_directions_url":"https://maps.google.com/maps?cid=15873234181324296589","id":3924708,"latitude":31.323102523571194,"longitude":-85.82880808981827,"type":"nearby","url":"al/enterprise/908-rucker-blvd-"},{"altTagText":"Advance Auto Parts at 2718 Montgomery Highway Dothan, AL","get_directions_url":"https://maps.google.com/maps?cid=3076131048064701794","id":3924894,"latitude":31.246485573167057,"longitude":-85.42104176711524,"type":"nearby","url":"al/dothan/2718-montgomery-highway"},{"altTagText":"Advance Auto Parts at 2590 Ross Clark Circle Dothan, AL","get_directions_url":"https://maps.google.com/maps?cid=6274075309125967097","id":3924562,"latitude":31.20460124840663,"longitude":-85.41972442536462,"type":"nearby","url":"al/dothan/2590-ross-clark-circle"},{"altTagText":"Advance Auto Parts at 1024 South Oates Street Dothan, AL","get_directions_url":"https://maps.google.com/maps?cid=12055100324922286678","id":3921462,"latitude":31.21091351433848,"longitude":-85.39367750287056,"type":"nearby","url":"al/dothan/1024-south-oates-street"},{"altTagText":"Advance Auto Parts at 711 East Town Avenue Geneva, AL","get_directions_url":"https://maps.google.com/maps?cid=14947243416995061618","id":3921493,"latitude":31.032539756513728,"longitude":-85.8664745092392,"type":"nearby","url":"al/geneva/711-east-town-avenue"},{"altTagText":"Advance Auto Parts at 101 West Cummings Avenue Opp, AL","get_directions_url":"https://maps.google.com/maps?cid=9182423075591035139","id":3922451,"latitude":31.2803595125938,"longitude":-86.25616461038595,"type":"nearby","url":"al/opp/101-west-cummings-avenue"},{"altTagText":"Advance Auto Parts at 1212 Highway 231 S Troy, AL","get_directions_url":"https://maps.google.com/maps?cid=14758407937310541268","id":3924606,"latitude":31.78234836732219,"longitude":-85.95055095390757,"type":"nearby","url":"al/troy/1212-highway-231-s"},{"altTagText":"Advance Auto Parts at 811 N Waukesha St. Bonifay, FL","get_directions_url":"https://maps.google.com/maps?cid=3309256993203027343","id":3924588,"latitude":30.799899390335558,"longitude":-85.67988301813506,"type":"nearby","url":"fl/bonifay/811-n-waukesha-st-"},{"altTagText":"Advance Auto Parts at 604 North Three Notch Street Troy, AL","get_directions_url":"https://maps.google.com/maps?cid=13872806241691390306","id":3921860,"latitude":31.812477464711485,"longitude":-85.9722152352333,"type":"nearby","url":"al/troy/604-north-three-notch-street"},{"altTagText":"Advance Auto Parts at 1160 Main Street Chipley, FL","get_directions_url":"https://maps.google.com/maps?cid=16952411950774342936","id":3924609,"latitude":30.76764462509219,"longitude":-85.53961380387136,"type":"nearby","url":"fl/chipley/1160-main-street"}]}</script>']

string = str(text)

loc = re.search('<script(.+?){"apiID',string).group(0)


print(loc)
