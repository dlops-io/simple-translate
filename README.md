# Simple Translate App

## Installing App on VM Manually
* Create a VM Instance from [GCP](https://console.cloud.google.com/compute/instances)
* SSH into your newly created instance
* Update OS packages: `sudo apt-get update`
* Install Git: `sudo apt install git`
* Clone App Repo: `git clone https://github.com/dlops-io/simple-translate.git`
* `cd simple-translate`
* Install Python: `sudo apt install python3-pip`
* Install packages: `pip3 install googletrans==4.0.0rc1 art`
Test out the translations:
* `python3 cli.py`
* `python3 cli.py -t "Good morning" -s "en" -d "es"`
* `python3 cli.py -t "Good afternoon" -s "en" -d "fr"`

Refer to language codes at the bottom of this page.

## Installing App on VM using Pipenv
* Create a VM Instance from [GCP](https://console.cloud.google.com/compute/instances)
* SSH into your newly created instance
* Update OS packages: `sudo apt-get update`
* Install Git: `sudo apt install git`
* Clone App Repo: `git clone https://github.com/dlops-io/simple-translate.git`
* `cd simple-translate`
* Install Pipenv: `sudo apt install pipenv`
* Install Pipenv environment from Pipfile: `pipenv install`
* Go into the newly created environment shell: `pipenv shell`
Test out the translations:
* `python cli.py`
* `python cli.py -t "Good morning" -s "en" -d "es"`
* `python cli.py -t "Good afternoon" -s "en" -d "fr"`

Refer to language codes at the bottom of this page.

## Running App on VM using Docker
* Create a VM Instance from [GCP](https://console.cloud.google.com/compute/instances)
* SSH into your newly created instance
Install Docker on the newly created instance by running
* `curl -fsSL https://get.docker.com -o get-docker.sh`
* `sudo sh get-docker.sh`  
Check version of installed Docker
* `sudo docker --version`  
Run the app using Docker
* `sudo docker run --rm -ti dlops/simple-translate`

## Developing App using Containers

### Prerequisites for Development using Containers
* Have Docker Desktop installed
* Cloned this repository to your local machine with a terminal up and running
* Check that your Docker is running with the following command

`docker run hello-world`


### Install VSCode  
Follow the [instructions](https://code.visualstudio.com/download) for your operating system.  
If you already have a preferred text editor, skip this step.  

### Make sure we do not have any running containers and clear up an unused images
* Run `docker container ls`
* Stop any container that is running
* Run `docker system prune`
* Run `docker image ls`

### Clone the github repository
- Clone or download from [here](https://github.com/dlops-io/simple-translate)

### Building Docker Image
Go into the app folder by running
* `cd simple-translate`
Build the docker container by running
* `docker build -t simple-translate -f Dockerfile .`

### Running Docker Container
Run the container using:
* `docker run --rm -ti simple-translate`
Running the translate code
* `python cli.py -t "Good morning" -s "en" -d "es"`
To exit from container
* Type `exit` from the Docker shell

### Pushing Docker Image to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag simple-translate <USER NAME>/simple-translate`
* Push to Docker Hub: `docker push <USER NAME>/simple-translate`


## Running App as Cloud Function
* In GCP go to [Cloud Functions](https://console.cloud.google.com/functions)
* Click the "+ CREATE FUNCTION" button
* If you have not enabled the required APIs, a popup will showup as shown

<img src="images/cloud-function-enable-apis.pngg"  width="500">

* Enable the required APIs. Click "ENABLE"



## Google Translate Two-Letter Language Codes
<table border="1">
<tbody>
<tr><td>No.</td><td>Language Name</td><td>Native Language Name</td><td>Code</td></tr>
<tr><td>1</td><td>Afrikaans</td><td><code>Afrikaans</code></td><td><code>af</code></td></tr>
<tr><td>2</td><td>Albanian</td><td><code>Shqip</code></td><td><code>sq</code></td></tr>
<tr><td>3</td><td>Arabic</td><td><code>عربي</code></td><td><code>ar</code></td></tr>
<tr><td>4</td><td>Armenian</td><td><code>Հայերէն</code></td><td><code>hy</code></td></tr>
<tr><td>5</td><td>Azerbaijani</td><td><code>آذربایجان دیلی</code></td><td><code>az</code></td></tr>
<tr><td>6</td><td>Basque</td><td><code>Euskara</code></td><td><code>eu</code></td></tr>
<tr><td>7</td><td>Belarusian</td><td><code>Беларуская</code></td><td><code>be</code></td></tr>
<tr><td>8</td><td>Bulgarian</td><td><code>Български</code></td><td><code>bg</code></td></tr>
<tr><td>9</td><td>Catalan</td><td><code>Català</code></td><td><code>ca</code></td></tr>
<tr><td>10</td><td>Chinese (Simplified)</td><td><code>中文简体</code></td><td><code>zh-CN</code></td></tr>
<tr><td>11</td><td>Chinese (Traditional)</td><td><code>中文繁體</code></td><td><code>zh-TW</code></td></tr>
<tr><td>12</td><td>Croatian</td><td><code>Hrvatski</code></td><td><code>hr</code></td></tr>
<tr><td>13</td><td>Czech</td><td><code>Čeština</code></td><td><code>cs</code></td></tr>
<tr><td>14</td><td>Danish</td><td><code>Dansk</code></td><td><code>da</code></td></tr>
<tr><td>15</td><td>Dutch</td><td><code>Nederlands</code></td><td><code>nl</code></td></tr>
<tr><td>16</td><td>English</td><td><code>English</code></td><td><code>en</code></td></tr>
<tr><td>17</td><td>Estonian</td><td><code>Eesti keel</code></td><td><code>et</code></td></tr>
<tr><td>18</td><td>Filipino</td><td><code>Filipino</code></td><td><code>tl</code></td></tr>
<tr><td>19</td><td>Finnish</td><td><code>Suomi</code></td><td><code>fi</code></td></tr>
<tr><td>20</td><td>French</td><td><code>Français</code></td><td><code>fr</code></td></tr>
<tr><td>21</td><td>Galician</td><td><code>Galego</code></td><td><code>gl</code></td></tr>
<tr><td>22</td><td>Georgian</td><td><code>ქართული</code></td><td><code>ka</code></td></tr>
<tr><td>23</td><td>German</td><td><code>Deutsch</code></td><td><code>de</code></td></tr>
<tr><td>24</td><td>Greek</td><td><code>Ελληνικά</code></td><td><code>el</code></td></tr>
<tr><td>25</td><td>Haitian Creole</td><td><code>Kreyòl ayisyen</code></td><td><code>ht</code></td></tr>
<tr><td>26</td><td>Hebrew</td><td><code>עברית</code></td><td><code>iw</code></td></tr>
<tr><td>27</td><td>Hindi</td><td><code>हिन्दी</code></td><td><code>hi</code></td></tr>
<tr><td>28</td><td>Hungarian</td><td><code>Magyar</code></td><td><code>hu</code></td></tr>
<tr><td>29</td><td>Icelandic</td><td><code>Íslenska</code></td><td><code>is</code></td></tr>
<tr><td>30</td><td>Indonesian</td><td><code>Bahasa Indonesia</code></td><td><code>id</code></td></tr>
<tr><td>31</td><td>Irish</td><td><code>Gaeilge</code></td><td><code>ga</code></td></tr>
<tr><td>32</td><td>Italian</td><td><code>Italiano</code></td><td><code>it</code></td></tr>
<tr><td>33</td><td>Japanese</td><td><code>日本語</code></td><td><code>ja</code></td></tr>
<tr><td>34</td><td>Korean</td><td><code>한국어</code></td><td><code>ko</code></td></tr>
<tr><td>35</td><td>Latvian</td><td><code>Latviešu</code></td><td><code>lv</code></td></tr>
<tr><td>36</td><td>Lithuanian</td><td><code>Lietuvių kalba</code></td><td><code>lt</code></td></tr>
<tr><td>37</td><td>Macedonian</td><td><code>Македонски</code></td><td><code>mk</code></td></tr>
<tr><td>38</td><td>Malay</td><td><code>Malay</code></td><td><code>ms</code></td></tr>
<tr><td>39</td><td>Maltese</td><td><code>Malti</code></td><td><code>mt</code></td></tr>
<tr><td>40</td><td>Norwegian</td><td><code>Norsk</code></td><td><code>no</code></td></tr>
<tr><td>41</td><td>Persian</td><td><code>فارسی</code></td><td><code>fa</code></td></tr>
<tr><td>42</td><td>Polish</td><td><code>Polski</code></td><td><code>pl</code></td></tr>
<tr><td>43</td><td>Portuguese</td><td><code>Português</code></td><td><code>pt</code></td></tr>
<tr><td>44</td><td>Romanian</td><td><code>Română</code></td><td><code>ro</code></td></tr>
<tr><td>45</td><td>Russian</td><td><code>Русский</code></td><td><code>ru</code></td></tr>
<tr><td>46</td><td>Serbian</td><td><code>Српски</code></td><td><code>sr</code></td></tr>
<tr><td>47</td><td>Slovak</td><td><code>Slovenčina</code></td><td><code>sk</code></td></tr>
<tr><td>48</td><td>Slovenian</td><td><code>Slovensko</code></td><td><code>sl</code></td></tr>
<tr><td>49</td><td>Spanish</td><td><code>Español</code></td><td><code>es</code></td></tr>
<tr><td>50</td><td>Swahili</td><td><code>Kiswahili</code></td><td><code>sw</code></td></tr>
<tr><td>51</td><td>Swedish</td><td><code>Svenska</code></td><td><code>sv</code></td></tr>
<tr><td>52</td><td>Thai</td><td><code>ไทย</code></td><td><code>th</code></td></tr>
<tr><td>53</td><td>Turkish</td><td><code>Türkçe</code></td><td><code>tr</code></td></tr>
<tr><td>54</td><td>Ukrainian</td><td><code>Українська</code></td><td><code>uk</code></td></tr>
<tr><td>55</td><td>Urdu</td><td><code>اردو</code></td><td><code>ur</code></td></tr>
<tr><td>56</td><td>Vietnamese</td><td><code>Tiếng Việt</code></td><td><code>vi</code></td></tr>
<tr><td>57</td><td>Welsh</td><td><code>Cymraeg</code></td><td><code>cy</code></td></tr>
<tr><td>58</td><td>Yiddish</td><td><code>ייִדיש</code></td><td><code>yi</code></td></tr>
</tbody>
</table>



## Accessing files from GCS Bucket
* You can download a file from GCS using `https://storage.googleapis.com/ac215-test-bucket/tips.txt` (path of file in GCS)
* You can upload a file to GCS using `curl --upload-file tips2.txt https://storage.googleapis.com/ac215-test-bucket/` (provided you have write access)
