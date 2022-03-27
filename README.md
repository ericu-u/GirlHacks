# HackCWRU Submission
This project was created as a submission to [GirlHacks 2022](https://girlhacks2022.devpost.com/). The submission can be found [here](https://devpost.com/software/healthwealth).
**Team Members**: _Jonathan Lo and Eric Wang_

## HealthWealth
HealthWealth is designed to allow its users to gain awareness to potentially harmful lifestyle habits. By being aware of these dangers, users can make informed decisions to improve their quality of life. HealthWealth achieves this by providing an objective view of a persons life style and offers them different resources catered to their lifestyle. These resources range from an exercise plan to different diet options to even better sleep schedule management.


## Inspiration
Both of us used to be competitive swimmers but grew complacent due to COVID. We realized we had unknowingly slipped into bad habits that affected our lifestyle. Here, 


## Tech Stack
The backend is in Python utilizing the [Django](https://www.djangoproject.com/) framework. The front end is a mix of HTML/CSS and JavaScript. We use Jquery AJAX requests to asynchronously update the front end. Moreover, we use [Chart.js](https://www.chartjs.org/) to create a chart of spending over a period of time. We use Pandas and statistical analysis to make predictions and recommended actions.


Code Flow:<br>
![](https://cdn.discordapp.com/attachments/621553050766540820/957616787166486578/unknown.png)

## Running

 1. Clone the repository.
 2. Install `pipenv` and the dependencies in `Pipfile`.
 3. Launch `pipenv` enviroment using:
```bash
pipenv shell
```
 4. Create a `config.json` and input Client IDs, Secrets, and Tokens according to `config.json.example`. You will need PayPal and Discord credentials.(https://cloud.google.com/python/django/appengine).
 5. Start local server using: 
  ```
  python3 manage.py runserver
  ```
