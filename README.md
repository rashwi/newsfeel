# Timely
Timely is a simple data scraping tool designed to pull data from the new york times streaming API and conduct sentiment analysis on select articles.


## Requirements

### NYTimes API Key
The main function (timely.py) will look for a valid API Key in 'times-api.json' located at the same level as the main function. the json file should be formatted as follows:

```
{
    "api-key" : "Your API Key"
}
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
* tqdm


## Setup
1. Clone the repository
2. Install google cloud packages for your operating system
   * Install packages using a package manager appropriate for your distribution.
     * Note that the google cloud packages will require you to add additional repositories to your package manager repo list. For more detail, see the google cloud documentation at https://cloud.google.com/python/docs/setup

## Infrastructure for deployment
Code to deploy the infrastructure necessary to run this project is available as a separate project at https://github.com/rashwi/timely-iac




