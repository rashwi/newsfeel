# Newsfeel
Newsfeel is a simple data scraping tool designed to pull data from the new york times streaming API and conduct sentiment analysis on select articles.


## Requirements

### Required environment variables
This module takes advantage of multiple APIs that require authentication. As a result, the following API secrets are expected to be in the environment.
Please note that the variables are case sensitive

### NYTimes API Key
The NYTimes API should be stored in the environment variable `NYTIMES_API_KEY`. Set the variable as shown here before running the script:

```bash
export NYTIMES_API_KEY="YOUR_KEY_HERE"
```
You can sign up for an API key at [developer.nytimes.com](https://wwww.developer.nytimes.com)

#### GCP IAM file
The main function will also require gcp authentication credentials. Follow the directions provided at https://cloud.google.com/iam/docs/creating-managing-service-account-keys

The path to the resulting *iam.json file should be stored in the environment variable `GOOGLE_APPLICATION_CREDENTIALS` :
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/iam-file.json"
```

#### Bing API Key
You will need an Azure resource setup to use the bing search API. See directions provided at [docs.microsoft.com](https://docs.microsoft.com/en-us/azure/cognitive-services/bing-news-search/python) to get instructions on how to setup a new resource.

Once your resource is setup, you can see your keys by going to your resource management page in the Azure dashboard and clicking on "Manage Keys". Assign the value of "key1" to the environment variable "BING_API_KEY":
```bash
export BING_API_KEY="YOUR_KEY_HERE"
```


### Additional Packages
The following packages are required:
* google-cloud-sdk
* google-cloud-sdk-app-engine-python
* google-cloud-language

### Python dependencies
python3 is recommended for the usage of this software. In addition, the following packages should be installed:
* google-cloud-storage
* google-cloud-language
* pandas


## Setup
1. Clone the repository
2. Install google cloud packages for your operating system
   * Install packages using a package manager appropriate for your distribution.
     * Note that the google cloud packages will require you to add additional repositories to your package manager repo list. For more detail, see the google cloud documentation at https://cloud.google.com/python/docs/setup
3. Install python packages necessary
   * All python dependencies can be installed with pip


## Running 
Use `main.py` as an example of how to use the Newsfeel package




