# Metroinfo-HA
Connect metroinfo api to Home assistant

You will need to edit your `configuration.yaml` see [this](https://www.home-assistant.io/docs/configuration/) if you need help

1. get api token from [here](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal'>
  Click on sign up.
</p>

2. enter your details
3. Add metroinfo.py to your config folder
4. change apitoken to your api token.
5. change stopcode to a stop found [here](https://go.metroinfo.co.nz/) 
6. change filter bus code to the bus code you would like to record list of bus route codes can be found [here](/metroinfo-data/routes.txt)
7. Open 'configuration.yaml' and add this code

```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```

