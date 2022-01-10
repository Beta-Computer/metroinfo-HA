# Metroinfo-HA
Connect metroinfo api to Home assistant

You will need to edit your `configuration.yaml` see [this](https://www.home-assistant.io/docs/configuration/) if you need help

1. get api token from [here](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal' height= "1086" width= "2874">
  Click on sign up.
</p>
3. Add metroinfo.py to your config folder
4. Open 'configuration.yaml' and add this code
```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```
3. change stopcode to a stop found [here](https://go.metroinfo.co.nz/) 
